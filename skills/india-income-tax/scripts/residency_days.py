#!/usr/bin/env python3
"""
India residential-status checker for individuals.

Counts days physically present in India per Indian financial year (1 April to
31 March) from a list of trips, then applies the residence tests of section 6
of the Income-tax Act, 1961 (carried into section 6 of the Income-tax Act,
2025 with renumbered sub-sections; the substance is unchanged).

It prints a worksheet: days this FY, days in the 4 and 7 preceding FYs, the
status (NR / RNOR / ROR), and the rule chain that produced it. It is a
calculator, not advice: the "visit" and "left for employment" facts and the
Rs 15 lakh test need human judgment.

Usage:
    python3 residency_days.py input.json
    python3 residency_days.py --example     # prints a sample input file

Input JSON:
{
  "fy": "2025-26",                       # FY being determined (April-March)
  "trips": [                             # every stay in India, oldest first
      {"arrive": "2025-04-17", "depart": "2025-04-28"},
      ...
  ],
  "lived_in_india_until": "2021-12-05",  # optional: last day of continuous residence;
                                         # all days from history_start to this date count
  "history_start": "2014-04-01",         # optional: earliest date the trip list is complete from
  "indian_citizen": true,
  "person_of_indian_origin": false,
  "came_on_visit": true,                 # outside India and came to India on visit(s) this FY
  "left_for_employment_this_fy": false,  # citizen who left India this FY for a job abroad / as crew
  "indian_income_excl_foreign": 450000,  # total income other than income from foreign sources (Rs)
  "liable_to_tax_elsewhere": true,       # tax resident somewhere else (e.g. UK) by domicile/residence
  "prior_statuses": {"2016-17": "R"},    # optional overrides for years the trip list cannot cover
  "count_mode": "both_days"              # "both_days" (arrival and departure both count; default)
                                         # or "exclude_travel_days"
}
"""
import json
import sys
from datetime import date, timedelta

EXAMPLE = {
    "fy": "2025-26",
    "trips": [
        {"arrive": "2022-04-10", "depart": "2022-05-05"},
        {"arrive": "2023-12-20", "depart": "2024-01-10"},
        {"arrive": "2024-10-01", "depart": "2024-10-20"},
        {"arrive": "2025-04-15", "depart": "2025-04-30"},
        {"arrive": "2025-12-01", "depart": "2025-12-20"},
    ],
    "lived_in_india_until": "2021-11-30",
    "history_start": "2012-04-01",
    "indian_citizen": True,
    "person_of_indian_origin": False,
    "came_on_visit": True,
    "left_for_employment_this_fy": False,
    "indian_income_excl_foreign": 450000,
    "liable_to_tax_elsewhere": True,
    "prior_statuses": {},
    "count_mode": "both_days",
}

FIFTEEN_LAKH = 1_500_000


def d(s):
    return date.fromisoformat(s)


def fy_bounds(fy):
    start_year = int(fy.split("-")[0])
    return date(start_year, 4, 1), date(start_year + 1, 3, 31)


def fy_label(start_year):
    return f"{start_year}-{str(start_year + 1)[-2:]}"


def shift_fy(fy, n):
    return fy_label(int(fy.split("-")[0]) + n)


def india_days(cfg):
    """Return the set of dates the person was in India."""
    days = set()
    mode = cfg.get("count_mode", "both_days")
    start = d(cfg["history_start"]) if cfg.get("history_start") else None
    if cfg.get("lived_in_india_until"):
        if start is None:
            raise SystemExit("lived_in_india_until needs history_start")
        cur = start
        end = d(cfg["lived_in_india_until"])
        while cur <= end:
            days.add(cur)
            cur += timedelta(days=1)
    for t in cfg.get("trips", []):
        a, b = d(t["arrive"]), d(t["depart"])
        if b < a:
            raise SystemExit(f"trip departs before it arrives: {t}")
        if mode == "exclude_travel_days":
            a, b = a + timedelta(days=1), b - timedelta(days=1)
        cur = a
        while cur <= b:
            days.add(cur)
            cur += timedelta(days=1)
    return days


def count_in(days, fy):
    s, e = fy_bounds(fy)
    return sum(1 for x in days if s <= x <= e)


def covered(cfg, fy):
    """True if the trip history is complete for this FY."""
    if not cfg.get("history_start"):
        return False
    return d(cfg["history_start"]) <= fy_bounds(fy)[0]


def basic_status(cfg, days, fy, is_target):
    """Resident (R) or Non-resident (NR) for one FY, with reasons."""
    reasons = []
    n = count_in(days, fy)
    prev4 = sum(count_in(days, shift_fy(fy, -k)) for k in range(1, 5))
    citizen = cfg.get("indian_citizen", False)
    pio = cfg.get("person_of_indian_origin", False)
    income = cfg.get("indian_income_excl_foreign", 0) if is_target else cfg.get(
        "indian_income_excl_foreign_prior", cfg.get("indian_income_excl_foreign", 0))

    if n >= 182:
        reasons.append(f"{n} days in India >= 182: resident under s.6(1)(a)")
        return "R", reasons, n, prev4, False

    # Second test: 60 days (or 120 / 182 for the special cases) plus 365 in 4 preceding FYs
    threshold, label = 60, "60"
    via_120 = False
    if is_target and citizen and cfg.get("left_for_employment_this_fy"):
        threshold, label = 182, "182 (citizen leaving India for employment / as crew)"
    elif is_target and (citizen or pio) and cfg.get("came_on_visit"):
        if income > FIFTEEN_LAKH:
            threshold, label = 120, "120 (citizen/PIO on visit, Indian income > Rs 15 lakh)"
            via_120 = True
        else:
            threshold, label = 182, "182 (citizen/PIO on visit, Indian income <= Rs 15 lakh)"

    if n >= threshold and prev4 >= 365:
        reasons.append(f"{n} days >= {label} and {prev4} days in 4 preceding FYs >= 365: resident under s.6(1)(c)")
        return "R", reasons, n, prev4, via_120
    reasons.append(f"{n} days < 182; second test fails ({n} vs threshold {label}; {prev4} days in 4 preceding FYs vs 365)")
    return "NR", reasons, n, prev4, False


def status_for_prior(cfg, days, fy):
    override = cfg.get("prior_statuses", {}).get(fy)
    if override:
        return ("R" if override.upper().startswith("R") else "NR"), "given"
    if covered(cfg, fy) and covered(cfg, shift_fy(fy, -4)):
        s, _, _, _, _ = basic_status(cfg, days, fy, is_target=False)
        return s, "computed (60-day test used; visit/employment exceptions not modelled for past years)"
    return None, "unknown (trip history does not cover this year: add prior_statuses)"


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--example":
        print(json.dumps(EXAMPLE, indent=2))
        return
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cfg = json.load(open(sys.argv[1]))
    fy = cfg["fy"]
    days = india_days(cfg)
    out = {"fy": fy, "assessment_year_1961_act": shift_fy(fy, 1),
           "count_mode": cfg.get("count_mode", "both_days")}

    status, reasons, n, prev4, via_120 = basic_status(cfg, days, fy, is_target=True)
    out["days_in_india_this_fy"] = n
    out["days_in_4_preceding_fys"] = prev4
    out["days_by_fy"] = {shift_fy(fy, -k): count_in(days, shift_fy(fy, -k)) for k in range(0, 10)}
    prev7 = sum(count_in(days, shift_fy(fy, -k)) for k in range(1, 8))
    out["days_in_7_preceding_fys"] = prev7
    warnings = []
    for k in range(1, 5):
        if not covered(cfg, shift_fy(fy, -k)):
            warnings.append(f"Trip history does not cover FY {shift_fy(fy, -k)}: the 4-year total may be understated.")
            break

    # Deemed residence s.6(1A)
    deemed = False
    if status == "NR" and cfg.get("indian_citizen") and \
            cfg.get("indian_income_excl_foreign", 0) > FIFTEEN_LAKH and \
            not cfg.get("liable_to_tax_elsewhere", True):
        deemed = True
        status = "R"
        reasons.append("Deemed resident under s.6(1A): citizen, Indian income > Rs 15 lakh, not liable to tax in any other country")

    if status == "NR":
        out["status"] = "NR"
        out["status_long"] = "Non-Resident"
    else:
        # RNOR tests s.6(6)
        rnor_reasons = []
        if deemed:
            rnor_reasons.append("deemed resident under s.6(1A) is always RNOR (s.6(6)(d))")
        if via_120:
            rnor_reasons.append("resident only via the 120-day rule is RNOR (s.6(6)(c))")
        if prev7 <= 729:
            rnor_reasons.append(f"{prev7} days in 7 preceding FYs <= 729 (s.6(6)(a))")
        nr_count, unknown = 0, []
        for k in range(1, 11):
            pfy = shift_fy(fy, -k)
            s, how = status_for_prior(cfg, days, pfy)
            if s is None:
                unknown.append(pfy)
            elif s == "NR":
                nr_count += 1
        if nr_count >= 9:
            rnor_reasons.append(f"non-resident in {nr_count} of 10 preceding FYs (s.6(6)(a))")
        elif unknown:
            warnings.append(f"Status unknown for {', '.join(unknown)}; the 9-of-10-years RNOR test could not be completed.")
        if not covered(cfg, shift_fy(fy, -7)):
            warnings.append("Trip history does not cover all 7 preceding FYs; the 729-day RNOR test may be wrong.")
        if rnor_reasons:
            out["status"] = "RNOR"
            out["status_long"] = "Resident but Not Ordinarily Resident"
            reasons += rnor_reasons
        else:
            out["status"] = "ROR"
            out["status_long"] = "Resident and Ordinarily Resident"
            reasons.append(f"no RNOR condition met (NR in {nr_count}/10 preceding FYs; {prev7} days in 7 preceding FYs > 729)")

    out["reasons"] = reasons
    out["warnings"] = warnings + [
        "Confirm the 'came on visit' / 'left for employment' facts and the Rs 15 lakh figure yourself; they change the thresholds.",
        "Enter the two day counts in ITR-2 Part A (Residential Status) exactly as worked here; keep the trip list as evidence.",
    ]
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
