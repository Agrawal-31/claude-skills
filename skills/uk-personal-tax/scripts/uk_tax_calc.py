#!/usr/bin/env python3
"""
uk_tax_calc.py: deterministic arithmetic for the uk-personal-tax skill.

Do the sums here, not in prose. Every figure in RATES must match
references/rates-and-thresholds.md, which cites GOV.UK. If they disagree, the
reference file wins and this script needs fixing. Confirm the current year's
figures on GOV.UK before relying on any output.

Subcommands
  income-tax  Income tax in the statutory order (non-savings, savings,
              dividends): personal allowance taper, Scottish bands for
              non-savings income, starting rate for savings, personal savings
              allowance, dividend allowance, Gift Aid / relief-at-source band
              extension, FIG/OWR claim (no allowance), High Income Child
              Benefit Charge, and the balance against tax already paid.
  ftcr        Foreign tax credit relief, source by source: credit is the lower
              of the creditable foreign tax and the UK tax on that item
              (measured as the tax that disappears if the item is removed).
  cgt         Capital gains tax on a year's net gains with the annual exempt
              amount, losses brought forward and the band left over from income.
  owr         Overseas Workday Relief by workday apportionment with the cap.
  rsu-owr     OWR on one RSU vest: daily accrual over grant-to-vest, only the
              part inside the qualifying tax year, then the workday ratio.
  workdays    Working days in a period less bank holidays and leave.
  paye        What cumulative PAYE should have deducted to date for a tax
              code (L codes, 0T, BR, NT, with W1/M1 non-cumulative), so an
              emergency-code or wrong-code overpayment can be sized.
  poa         Payments on account for next year from this year's figures.
  taper       Personal allowance after the GBP 100,000 taper.

Add --json to any subcommand for machine-readable output.

Limits. An estimate for preparing and checking a return, not a filing figure.
Not covered: National Insurance, student loans, marriage allowance, married
couple's allowance, pension annual allowance charges, trust or partnership
income, the 2027-28 property/savings rate changes, Welsh rates (currently the
same as England), and HMRC's whole-pound rounding of return boxes. Savings and
dividends use UK-wide bands even for Scottish taxpayers. It does not decide
residence or eligibility for any relief.
"""

import argparse
import datetime as dt
import json

# ---------------------------------------------------------------------------
# Rates. Keep in step with references/rates-and-thresholds.md (GOV.UK, checked
# October 2026). Limits are on TAXABLE income (after the personal allowance).
# ---------------------------------------------------------------------------

UK_BANDS = [(37700.0, 0.20), (125140.0, 0.40), (None, 0.45)]
COMMON = {
    "personal_allowance": 12570.0,
    "taper_start": 100000.0,
    "basic_rate_limit": 37700.0,
    "higher_rate_limit": 125140.0,
    "ruk_bands": UK_BANDS,
    "savings_rates": UK_BANDS,
    "starting_rate_band": 5000.0,
    "psa": {"basic": 1000.0, "higher": 500.0, "additional": 0.0},
    "dividend_allowance": 500.0,
    "cgt_aea": 3000.0,
    "owr_cap_fraction": 0.30,
    "owr_cap_amount": 300000.0,
    "hicbc_start": 60000.0,
    "hicbc_end": 80000.0,
}

RATES = {
    "2024-25": dict(COMMON, **{
        "scotland_bands": [(2306.0, 0.19), (13991.0, 0.20), (31092.0, 0.21),
                           (62430.0, 0.42), (125140.0, 0.45), (None, 0.48)],
        "dividend_rates": [(37700.0, 0.0875), (125140.0, 0.3375), (None, 0.3935)],
        # Shares/other assets: 10/20 to 29 Oct 2024, 18/24 from 30 Oct 2024.
        "cgt_rates": {"basic": 0.18, "higher": 0.24},
        "cgt_rates_pre_30oct2024": {"basic": 0.10, "higher": 0.20},
        "badr_rate": 0.10,
    }),
    "2025-26": dict(COMMON, **{
        "scotland_bands": [(2827.0, 0.19), (14921.0, 0.20), (31092.0, 0.21),
                           (62430.0, 0.42), (125140.0, 0.45), (None, 0.48)],
        "dividend_rates": [(37700.0, 0.0875), (125140.0, 0.3375), (None, 0.3935)],
        "cgt_rates": {"basic": 0.18, "higher": 0.24},
        "badr_rate": 0.14,
    }),
    "2026-27": dict(COMMON, **{
        "scotland_bands": [(3967.0, 0.19), (16956.0, 0.20), (31092.0, 0.21),
                           (62430.0, 0.42), (125140.0, 0.45), (None, 0.48)],
        "dividend_rates": [(37700.0, 0.1075), (125140.0, 0.3575), (None, 0.3935)],
        "cgt_rates": {"basic": 0.18, "higher": 0.24},
        "badr_rate": 0.18,
    }),
}

TAX_YEAR_DATES = {
    "2024-25": ("2024-04-06", "2025-04-05"),
    "2025-26": ("2025-04-06", "2026-04-05"),
    "2026-27": ("2026-04-06", "2027-04-05"),
}

# Verify at https://www.gov.uk/bank-holidays before relying on a count.
BANK_HOLIDAYS = {
    "england-and-wales": [
        "2024-05-06", "2024-05-27", "2024-08-26", "2024-12-25", "2024-12-26",
        "2025-01-01", "2025-04-18", "2025-04-21", "2025-05-05", "2025-05-26",
        "2025-08-25", "2025-12-25", "2025-12-26",
        "2026-01-01", "2026-04-03", "2026-04-06", "2026-05-04", "2026-05-25",
        "2026-08-31", "2026-12-25", "2026-12-28",
        "2027-01-01", "2027-03-26", "2027-03-29",
    ],
    "scotland": [
        "2024-05-06", "2024-05-27", "2024-08-05", "2024-12-02", "2024-12-25",
        "2024-12-26", "2025-01-01", "2025-01-02",
        "2025-04-18", "2025-05-05", "2025-05-26", "2025-08-04", "2025-12-01",
        "2025-12-25", "2025-12-26",
        "2026-01-01", "2026-01-02", "2026-04-03", "2026-05-04", "2026-05-25",
        "2026-08-03", "2026-11-30", "2026-12-25", "2026-12-28",
        "2027-01-01", "2027-01-04", "2027-03-26",
    ],
}


def money(x):
    sign = "-" if x < 0 else ""
    return f"{sign}£{abs(x):,.2f}"


def r2(x):
    return round(x + 0.0, 2)


def personal_allowance(year, adjusted_net_income, no_allowance=False):
    """£1 lost per £2 of adjusted net income over £100,000; nil from £125,140.
    A FIG or OWR claim removes it for the year (RFIG43000)."""
    r = RATES[year]
    if no_allowance:
        return 0.0
    excess = max(0.0, adjusted_net_income - r["taper_start"])
    return max(0.0, r["personal_allowance"] - excess / 2.0)


def slice_bands(amount, start, bands, shift=0.0, shift_from=0):
    """Tax `amount` sitting on top of `start` of used band. Each band is
    (upper limit of taxable income, rate). Limits from index `shift_from`
    onward are widened by `shift` (Gift Aid / relief-at-source)."""
    out, remaining, lower = [], amount, start
    for i, (upper, rate) in enumerate(bands):
        if remaining <= 1e-9:
            break
        cap = None if upper is None else upper + (shift if i >= shift_from else 0.0)
        if cap is not None and lower >= cap:
            continue
        room = remaining if cap is None else min(remaining, cap - lower)
        if room > 0:
            out.append((room, rate, room * rate))
            remaining -= room
            lower += room
    return out


# ---------------------------------------------------------------------------
# income-tax
# ---------------------------------------------------------------------------

def compute_income_tax(year, region="ruk", employment=0.0, other_nonsavings=0.0,
                       savings=0.0, dividends=0.0, gift_aid_net=0.0,
                       pension_ras_net=0.0, no_allowance=False, owr_exempt=0.0,
                       fig_relieved=0.0, tax_paid=None, child_benefit=0.0,
                       ftcr=0.0):
    """fig_relieved: foreign non-savings income that is included in
    other_nonsavings but relieved under a FIG claim; it is removed from taxable
    income but added back for adjusted net income (RFIG43000). For FIG-relieved
    foreign interest or dividends, simply leave them out of savings/dividends.
    A FIG claim also needs no_allowance=True."""
    r = RATES[year]
    if owr_exempt > employment + 1e-9:
        raise SystemExit("OWR exempt amount cannot exceed employment income")
    nonsavings = employment - owr_exempt + other_nonsavings
    nonsavings_after_fig = max(0.0, nonsavings - fig_relieved)
    total_income = nonsavings_after_fig + savings + dividends

    gross_ga = gift_aid_net / 0.8
    gross_pen = pension_ras_net / 0.8
    shift = gross_ga + gross_pen
    # Adjusted net income: FIG relief is disregarded for ANI (RFIG43000), so
    # add the relieved amount back.
    ani = total_income + fig_relieved - shift
    pa = personal_allowance(year, ani, no_allowance)

    pa_left = pa
    ns_tax = max(0.0, nonsavings_after_fig - pa_left)
    pa_left = max(0.0, pa_left - nonsavings_after_fig)
    sav_tax = max(0.0, savings - pa_left)
    pa_left = max(0.0, pa_left - savings)
    div_tax = max(0.0, dividends - pa_left)
    taxable = ns_tax + sav_tax + div_tax

    lines = []
    scot = region == "scotland"
    bands = r["scotland_bands"] if scot else r["ruk_bands"]
    # Scottish band extension: applied to limits above the starter band
    # (approximation, see references). rUK: basic and higher limits.
    for portion, rate, tax in slice_bands(ns_tax, 0.0, bands, shift, 1 if scot else 0):
        lines.append(("Non-savings", portion, rate, tax))

    # Savings and dividends stack on top of non-savings in the UK bands.
    used = ns_tax
    if sav_tax > 0:
        srb = max(0.0, r["starting_rate_band"] - ns_tax)
        srb_used = min(srb, sav_tax)
        if srb_used > 0:
            lines.append(("Savings, starting rate", srb_used, 0.0, 0.0))
        rest = sav_tax - srb_used
        if taxable <= r["basic_rate_limit"] + shift:
            psa = r["psa"]["basic"]
        elif taxable <= r["higher_rate_limit"] + shift:
            psa = r["psa"]["higher"]
        else:
            psa = r["psa"]["additional"]
        psa_used = min(psa, rest)
        if psa_used > 0:
            lines.append(("Savings, personal savings allowance", psa_used, 0.0, 0.0))
        rest -= psa_used
        for portion, rate, tax in slice_bands(rest, used + srb_used + psa_used,
                                              r["savings_rates"], shift):
            lines.append(("Savings", portion, rate, tax))
        used += sav_tax
    if div_tax > 0:
        da = min(r["dividend_allowance"], div_tax)
        lines.append(("Dividends, dividend allowance", da, 0.0, 0.0))
        for portion, rate, tax in slice_bands(div_tax - da, used + da,
                                              r["dividend_rates"], shift):
            lines.append(("Dividends", portion, rate, tax))

    income_tax = sum(t for *_, t in lines)
    ftcr_used = min(ftcr, income_tax)
    hicbc = 0.0
    if child_benefit > 0 and ani > r["hicbc_start"]:
        frac = min(1.0, (ani - r["hicbc_start"]) / (r["hicbc_end"] - r["hicbc_start"]))
        hicbc = int(frac * 100) / 100.0 * child_benefit  # 1% per £200, whole %
    total = income_tax - ftcr_used + hicbc

    res = {
        "year": year, "region": region,
        "total_income": r2(total_income), "adjusted_net_income": r2(ani),
        "personal_allowance": r2(pa), "band_extension": r2(shift),
        "taxable_income": r2(taxable),
        "lines": [{"slice": s, "amount": r2(a), "rate": rt, "tax": r2(t)} for s, a, rt, t in lines],
        "income_tax_before_credits": r2(income_tax),
        "foreign_tax_credit": r2(ftcr_used),
        "hicbc": r2(hicbc),
        "total_liability": r2(total),
        "inputs": {"employment": employment, "owr_exempt": owr_exempt,
                   "other_nonsavings": other_nonsavings, "savings": savings,
                   "dividends": dividends, "fig_relieved": fig_relieved,
                   "no_allowance": no_allowance},
    }
    if tax_paid is not None:
        res["tax_paid"] = tax_paid
        res["balance"] = r2(total - tax_paid)
    return res


def print_income_tax(res):
    print(f"Income tax {res['year']} ({res['region']})")
    print(f"  Total income (after OWR/FIG)  {money(res['total_income'])}")
    print(f"  Adjusted net income           {money(res['adjusted_net_income'])}")
    if res["band_extension"]:
        print(f"  Band extension (gross)        {money(res['band_extension'])}")
    note = " (nil: FIG/OWR claim)" if res["inputs"]["no_allowance"] else ""
    print(f"  Personal allowance            {money(res['personal_allowance'])}{note}")
    print(f"  Taxable income                {money(res['taxable_income'])}")
    for ln in res["lines"]:
        print(f"    {ln['slice']:<36} {money(ln['amount']):>14} @ {ln['rate']*100:5.2f}% = {money(ln['tax']):>12}")
    print(f"  Income tax                    {money(res['income_tax_before_credits'])}")
    if res["foreign_tax_credit"]:
        print(f"  Less foreign tax credit       {money(-res['foreign_tax_credit'])}")
    if res["hicbc"]:
        print(f"  High Income Child Benefit Chg {money(res['hicbc'])}")
    print(f"  Total liability               {money(res['total_liability'])}")
    if "tax_paid" in res:
        b = res["balance"]
        print(f"  Tax already paid              {money(res['tax_paid'])}")
        print(f"  {'To pay' if b > 0 else 'Refund due':<29} {money(abs(b))}")
    print("  Estimate. HMRC rounds box entries to whole pounds, so expect pennies to pounds of difference.")


# ---------------------------------------------------------------------------
# ftcr
# ---------------------------------------------------------------------------

def compute_ftcr(year, region, base, items):
    """base: dict of UK-side inputs for compute_income_tax (without the foreign
    items). items: list of dicts {name, kind: nonsavings|savings|dividends,
    amount, foreign_tax, treaty_rate (optional)}. Items are treated as the top
    slice in the order given; give the highest foreign-rate item first
    (HS263 ordering)."""
    def tax_with(extra):
        kw = dict(base)
        for it in extra:
            key = {"nonsavings": "other_nonsavings", "savings": "savings",
                   "dividends": "dividends"}[it["kind"]]
            kw[key] = kw.get(key, 0.0) + it["amount"]
        return compute_income_tax(year, region, **kw)["income_tax_before_credits"]

    out, total_credit = [], 0.0
    full = tax_with(items)
    remaining = list(items)
    # Peel items off from the top: the first item listed is the top slice.
    for it in items:
        without = [x for x in remaining if x is not it]
        uk_on_item = tax_with(remaining) - tax_with(without)
        creditable = it["foreign_tax"]
        if it.get("treaty_rate") is not None:
            creditable = min(creditable, it["amount"] * it["treaty_rate"])
        credit = max(0.0, min(creditable, uk_on_item))
        out.append({"name": it["name"], "amount": it["amount"],
                    "foreign_tax_paid": it["foreign_tax"],
                    "creditable_foreign_tax": r2(creditable),
                    "uk_tax_on_item": r2(uk_on_item), "credit": r2(credit),
                    "unrelieved_foreign_tax": r2(it["foreign_tax"] - credit)})
        total_credit += credit
        remaining = without
    return {"year": year, "uk_tax_including_foreign_items": r2(full),
            "items": out, "total_credit": r2(total_credit),
            "uk_tax_after_credit": r2(full - total_credit),
            "note": "Credit is the lower of the creditable (treaty-rate) foreign tax and the UK tax on that item, "
                    "source by source (HS263). Excess foreign tax is not refunded by HMRC; reclaim it from the "
                    "foreign authority if the treaty rate was exceeded. No credit on income relieved under FIG."}


# ---------------------------------------------------------------------------
# cgt
# ---------------------------------------------------------------------------

def compute_cgt(year, gains, losses_in_year, losses_bf, taxable_income,
                no_aea=False, gift_aid_ras_gross=0.0, pre_oct_gains=0.0):
    """gains: total chargeable gains in the year before losses. pre_oct_gains:
    for 2024-25 only, the part of gains realised before 30 Oct 2024 (shares and
    other non-residential assets) taxed at 10/20. Losses are set first against
    the higher-rate gains in practice; here they reduce gains in aggregate and
    the AEA is set against gains taxed at the highest rate first."""
    r = RATES[year]
    net = max(0.0, gains - losses_in_year)
    # Brought-forward losses only reduce net gains down to the AEA.
    aea = 0.0 if no_aea else r["cgt_aea"]
    bf_used = min(losses_bf, max(0.0, net - aea))
    net_after_bf = net - bf_used
    chargeable = max(0.0, net_after_bf - aea)
    basic_left = max(0.0, r["basic_rate_limit"] + gift_aid_ras_gross - taxable_income)
    lines = []
    if year == "2024-25" and pre_oct_gains > 0:
        # Allocate AEA/losses pro rata is not statutory; HMRC lets you allocate
        # to give the lowest tax. Allocate the reduction to post-30-Oct gains
        # first (they carry the higher rates).
        reduce = gains - chargeable
        post = max(0.0, gains - pre_oct_gains)
        post_c = max(0.0, post - reduce)
        pre_c = chargeable - post_c
        # Basic band is used by pre-Oct gains first only if that helps; keep
        # simple: fill basic band with post-Oct gains first (larger rate gap).
        b1 = min(basic_left, post_c)
        lines += [("Post 29 Oct 2024 at basic", b1, r["cgt_rates"]["basic"]),
                  ("Post 29 Oct 2024 at higher", post_c - b1, r["cgt_rates"]["higher"])]
        basic_left -= b1
        b2 = min(basic_left, pre_c)
        pre = r["cgt_rates_pre_30oct2024"]
        lines += [("Pre 30 Oct 2024 at basic", b2, pre["basic"]),
                  ("Pre 30 Oct 2024 at higher", pre_c - b2, pre["higher"])]
    else:
        b = min(basic_left, chargeable)
        lines += [("Gains at basic rate", b, r["cgt_rates"]["basic"]),
                  ("Gains at higher rate", chargeable - b, r["cgt_rates"]["higher"])]
    lines = [(n, a, rt, a * rt) for n, a, rt in lines if a > 1e-9]
    tax = sum(t for *_, t in lines)
    return {"year": year, "gains_before_losses": r2(gains),
            "losses_in_year": r2(losses_in_year), "losses_bf_used": r2(bf_used),
            "losses_cf": r2(losses_bf - bf_used),
            "annual_exempt_amount": aea, "chargeable_gains": r2(chargeable),
            "basic_band_available": r2(max(0.0, r["basic_rate_limit"] + gift_aid_ras_gross - taxable_income)),
            "lines": [{"slice": n, "amount": r2(a), "rate": rt, "tax": r2(t)} for n, a, rt, t in lines],
            "cgt": r2(tax),
            "note": "Residential property gains need a 60-day return if UK land. BADR not modelled. "
                    "In a FIG claim year there is no AEA and foreign losses are not allowable."}


# ---------------------------------------------------------------------------
# owr, rsu-owr, workdays
# ---------------------------------------------------------------------------

def compute_owr(year, employment, foreign_workdays, total_workdays):
    r = RATES[year]
    if total_workdays <= 0 or not 0 <= foreign_workdays <= total_workdays:
        raise SystemExit("need 0 <= foreign workdays <= total workdays, total > 0")
    frac = foreign_workdays / total_workdays
    apportioned = employment * frac
    cap = min(r["owr_cap_fraction"] * employment, r["owr_cap_amount"])
    return {"year": year, "qualifying_employment_income": employment,
            "foreign_workdays": foreign_workdays, "total_workdays": total_workdays,
            "fraction": round(frac, 6), "apportioned": r2(apportioned),
            "cap": r2(cap), "relief": r2(min(apportioned, cap)),
            "note": "Use only for pay that accrues evenly over the year (salary, most allowances). "
                    "Pay tied to UK duties (e.g. a commuting allowance) is not apportioned. Apportion a bonus "
                    "over its earning period and RSUs with rsu-owr. Exclude from qualifying income anything "
                    "earned in a non-qualifying year. A workday abroad is one with substantive duties "
                    "performed wholly outside the UK; leave abroad never counts. The claim removes the "
                    "personal allowance and CGT annual exempt amount."}


def compute_rsu_owr(vest_value, grant, vest, qy_start, qy_end, overseas_days, total_days):
    """Daily accrual over grant -> vest; keep the slice inside [qy_start, qy_end];
    then multiply by overseas workdays / total workdays within that slice."""
    period = (vest - grant).days
    if period <= 0:
        raise SystemExit("vest must be after grant")
    a = max(grant, qy_start)
    b = min(vest, qy_end)
    in_year_days = max(0, (b - a).days)
    accrued = vest_value * in_year_days / period
    relief = accrued * overseas_days / total_days if total_days else 0.0
    return {"vest_value": vest_value, "period_days": period,
            "days_in_qualifying_year": in_year_days,
            "accrued_in_qualifying_year": r2(accrued),
            "excluded_non_qualifying": r2(vest_value - accrued),
            "overseas_workdays": overseas_days, "total_workdays": total_days,
            "relief": r2(relief),
            "note": "Day convention follows the worked method used in practice (EIM43575: securities income "
                    "accrues evenly over the relevant period). Count workdays only inside the in-year slice. "
                    "Later vests of the same award carry slices for this year's overseas days: claim them in "
                    "the year of the vest."}


def parse_date(s):
    return dt.date.fromisoformat(s)


def compute_workdays(start, end, region, leave_days, extra_workdays, exclude):
    hols = {parse_date(d) for d in BANK_HOLIDAYS[region]}
    excl = {parse_date(d) for d in exclude}
    weekdays, hol_hits, ex_hits = 0, [], 0
    d = start
    while d <= end:
        if d.weekday() < 5:
            weekdays += 1
            if d in hols:
                hol_hits.append(d.isoformat())
            elif d in excl:
                ex_hits += 1
        d += dt.timedelta(days=1)
    working = weekdays - len(hol_hits) - ex_hits - leave_days + extra_workdays
    return {"start": start.isoformat(), "end": end.isoformat(), "region": region,
            "weekdays": weekdays, "bank_holidays": hol_hits, "excluded": ex_hits,
            "leave_days": leave_days, "extra_workdays": extra_workdays,
            "working_days": working,
            "note": "extra_workdays = weekend/holiday days actually worked (e.g. business travel days "
                    "under EIM77020, or weekend work that earned time off in lieu)."}


# ---------------------------------------------------------------------------
# paye
# ---------------------------------------------------------------------------

def parse_code(code):
    c = code.upper().replace(" ", "")
    noncum = c.endswith(("W1", "M1", "X"))
    for suf in ("W1", "M1", "X"):
        if c.endswith(suf):
            c = c[: -len(suf)]
    scot = c.startswith("S")
    if c.startswith(("S", "C")):
        c = c[1:]
    return c, scot, noncum


def compute_paye(year, code, pay_to_date, period, periods=12, tax_paid=None):
    """Cumulative (or W1/M1) PAYE an employer should have deducted by `period`
    for rUK L/M/N/T codes, 0T, BR, D0, D1, NT. Scottish codes use Scottish bands.
    Approximation of HMRC tables (free pay = code x 10 + 9)."""
    r = RATES[year]
    c, scot, noncum = parse_code(code)
    bands = r["scotland_bands"] if scot else r["ruk_bands"]
    n = 1 if noncum else period
    frac = n / periods
    pay = pay_to_date if not noncum else pay_to_date  # caller passes this-period pay for W1/M1
    if c == "NT":
        return {"code": code, "tax_due": 0.0}
    if c == "BR":
        tax = pay * 0.20
    elif c == "D0":
        tax = pay * 0.40
    elif c == "D1":
        tax = pay * 0.45
    else:
        digits = "".join(ch for ch in c if ch.isdigit())
        num = int(digits) if digits else 0
        free = 0.0 if c == "0T" else (num * 10 + 9) * frac
        taxable = max(0.0, pay - free)
        prorated = [(None if u is None else u * frac, rt) for u, rt in bands]
        tax = sum(t for *_, t in slice_bands(taxable, 0.0, prorated))
    res = {"year": year, "code": code, "basis": "non-cumulative" if noncum else "cumulative",
           "period": period, "pay": pay, "tax_due": r2(tax)}
    if tax_paid is not None:
        res["tax_paid"] = tax_paid
        res["difference"] = r2(tax_paid - tax)
    res["note"] = ("PAYE splits the bands by period, so it never matches the annual liability when pay is "
                   "uneven or the year is cut short (leaving mid-year). Compare with income-tax for the "
                   "real annual figure.")
    return res


# ---------------------------------------------------------------------------
# poa
# ---------------------------------------------------------------------------

def compute_poa(total_liability, deducted_at_source):
    """Payments on account: none if the SA balance (liability less tax deducted
    at source) is under £1,000, or if more than 80% of the liability was
    deducted at source. Otherwise two payments of 50% of the balance."""
    balance = max(0.0, total_liability - deducted_at_source)
    pct = deducted_at_source / total_liability if total_liability else 1.0
    due = balance >= 1000 and pct <= 0.80
    each = balance / 2 if due else 0.0
    return {"liability": total_liability, "deducted_at_source": deducted_at_source,
            "sa_balance": r2(balance), "share_at_source": round(pct, 4),
            "payments_on_account_due": due, "each_payment": r2(each),
            "note": "If due: first POA 31 Jan with the balancing payment, second 31 Jul. Reduce with SA303 "
                    "(or online) if next year's income will be lower; interest runs if reduced too far."}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def out(res, as_json, printer=None):
    if as_json or printer is None:
        print(json.dumps(res, indent=2))
    else:
        printer(res)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    years = list(RATES)

    a = sub.add_parser("income-tax")
    a.add_argument("--year", choices=years, required=True)
    a.add_argument("--region", choices=["ruk", "scotland"], default="ruk")
    a.add_argument("--employment", type=float, default=0.0, help="P60/P45 pay (incl. payrolled benefits) + P11D benefits")
    a.add_argument("--other-nonsavings", type=float, default=0.0, help="self-employment, rent, pensions, foreign employment/pension, offshore income gains")
    a.add_argument("--savings", type=float, default=0.0, help="UK + foreign interest (outside ISAs)")
    a.add_argument("--dividends", type=float, default=0.0, help="UK + foreign dividends (outside ISAs)")
    a.add_argument("--gift-aid", type=float, default=0.0, help="net Gift Aid paid")
    a.add_argument("--pension-ras", type=float, default=0.0, help="net relief-at-source pension contributions")
    a.add_argument("--no-allowance", "--fig-claim", dest="no_allowance", action="store_true", help="FIG or OWR claim made: no personal allowance")
    a.add_argument("--owr-exempt", type=float, default=0.0)
    a.add_argument("--fig-relieved", type=float, default=0.0, help="foreign non-savings income included above but relieved under FIG")
    a.add_argument("--ftcr", type=float, default=0.0, help="foreign tax credit relief (from the ftcr subcommand)")
    a.add_argument("--child-benefit", type=float, default=0.0, help="Child Benefit received in the year (for HICBC)")
    a.add_argument("--tax-paid", type=float, default=None)
    a.add_argument("--json", action="store_true")

    f = sub.add_parser("ftcr", help="foreign tax credit relief")
    f.add_argument("--year", choices=years, required=True)
    f.add_argument("--region", choices=["ruk", "scotland"], default="ruk")
    f.add_argument("--employment", type=float, default=0.0)
    f.add_argument("--other-nonsavings", type=float, default=0.0)
    f.add_argument("--savings", type=float, default=0.0)
    f.add_argument("--dividends", type=float, default=0.0)
    f.add_argument("--item", action="append", required=True,
                   help="name:kind:amount:foreign_tax[:treaty_rate] e.g. 'IN interest:savings:2000:300:0.15'. "
                        "List the highest foreign-rate item first.")
    f.add_argument("--json", action="store_true")

    c = sub.add_parser("cgt")
    c.add_argument("--year", choices=years, required=True)
    c.add_argument("--gains", type=float, required=True, help="total gains before losses")
    c.add_argument("--losses", type=float, default=0.0, help="allowable losses in the year")
    c.add_argument("--losses-bf", type=float, default=0.0)
    c.add_argument("--taxable-income", type=float, required=True, help="taxable income from income-tax")
    c.add_argument("--band-extension", type=float, default=0.0, help="gross Gift Aid + relief-at-source pension")
    c.add_argument("--no-aea", action="store_true", help="FIG/OWR claim year")
    c.add_argument("--pre-30oct-gains", type=float, default=0.0, help="2024-25 only")
    c.add_argument("--json", action="store_true")

    o = sub.add_parser("owr")
    o.add_argument("--year", choices=years, required=True)
    o.add_argument("--employment", type=float, required=True)
    o.add_argument("--foreign-workdays", type=float, required=True)
    o.add_argument("--total-workdays", type=float, required=True)
    o.add_argument("--json", action="store_true")

    ro = sub.add_parser("rsu-owr")
    ro.add_argument("--vest-value", type=float, required=True)
    ro.add_argument("--grant", type=parse_date, required=True)
    ro.add_argument("--vest", type=parse_date, required=True)
    ro.add_argument("--year", choices=years, required=True, help="qualifying tax year")
    ro.add_argument("--overseas-workdays", type=float, required=True, help="inside the in-year slice")
    ro.add_argument("--total-workdays", type=float, required=True, help="inside the in-year slice")
    ro.add_argument("--json", action="store_true")

    w = sub.add_parser("workdays")
    w.add_argument("--start", type=parse_date)
    w.add_argument("--end", type=parse_date)
    w.add_argument("--year", choices=list(TAX_YEAR_DATES))
    w.add_argument("--region", choices=list(BANK_HOLIDAYS), default="england-and-wales")
    w.add_argument("--leave-days", type=float, default=0.0)
    w.add_argument("--extra-workdays", type=float, default=0.0)
    w.add_argument("--exclude", nargs="*", default=[])
    w.add_argument("--json", action="store_true")

    pp = sub.add_parser("paye")
    pp.add_argument("--year", choices=years, required=True)
    pp.add_argument("--code", required=True)
    pp.add_argument("--pay-to-date", type=float, required=True, help="taxable pay to date (or this period's pay for W1/M1)")
    pp.add_argument("--period", type=int, required=True, help="tax month (1-12) or week (1-52)")
    pp.add_argument("--periods", type=int, default=12, help="12 monthly, 52 weekly")
    pp.add_argument("--tax-paid", type=float, default=None)
    pp.add_argument("--json", action="store_true")

    q = sub.add_parser("poa")
    q.add_argument("--liability", type=float, required=True)
    q.add_argument("--at-source", type=float, required=True, help="PAYE and other tax deducted at source")
    q.add_argument("--json", action="store_true")

    t = sub.add_parser("taper")
    t.add_argument("--year", choices=years, required=True)
    t.add_argument("--adjusted-net-income", type=float, required=True)
    t.add_argument("--json", action="store_true")

    args = p.parse_args(argv)

    if args.cmd == "income-tax":
        res = compute_income_tax(args.year, args.region, args.employment, args.other_nonsavings,
                                 args.savings, args.dividends, args.gift_aid, args.pension_ras,
                                 args.no_allowance, args.owr_exempt, args.fig_relieved,
                                 args.tax_paid, args.child_benefit, args.ftcr)
        out(res, args.json, print_income_tax)
    elif args.cmd == "ftcr":
        items = []
        for spec in args.item:
            parts = spec.split(":")
            if len(parts) not in (4, 5):
                raise SystemExit(f"bad --item {spec}")
            items.append({"name": parts[0], "kind": parts[1], "amount": float(parts[2]),
                          "foreign_tax": float(parts[3]),
                          "treaty_rate": float(parts[4]) if len(parts) == 5 else None})
        base = {"employment": args.employment, "other_nonsavings": args.other_nonsavings,
                "savings": args.savings, "dividends": args.dividends}
        out(compute_ftcr(args.year, args.region, base, items), True)
    elif args.cmd == "cgt":
        out(compute_cgt(args.year, args.gains, args.losses, args.losses_bf, args.taxable_income,
                        args.no_aea, args.band_extension, args.pre_30oct_gains), True)
    elif args.cmd == "owr":
        out(compute_owr(args.year, args.employment, args.foreign_workdays, args.total_workdays), True)
    elif args.cmd == "rsu-owr":
        s, e = TAX_YEAR_DATES[args.year]
        out(compute_rsu_owr(args.vest_value, args.grant, args.vest, parse_date(s),
                            parse_date(e) + dt.timedelta(days=1), args.overseas_workdays,
                            args.total_workdays), True)
    elif args.cmd == "workdays":
        if args.year:
            s, e = map(parse_date, TAX_YEAR_DATES[args.year])
        elif args.start and args.end:
            s, e = args.start, args.end
        else:
            raise SystemExit("give --year or --start and --end")
        out(compute_workdays(s, e, args.region, args.leave_days, args.extra_workdays, args.exclude), True)
    elif args.cmd == "paye":
        out(compute_paye(args.year, args.code, args.pay_to_date, args.period, args.periods, args.tax_paid), True)
    elif args.cmd == "poa":
        out(compute_poa(args.liability, args.at_source), True)
    elif args.cmd == "taper":
        pa = personal_allowance(args.year, args.adjusted_net_income)
        out({"year": args.year, "adjusted_net_income": args.adjusted_net_income,
             "personal_allowance": r2(pa),
             "marginal_note": "Between £100,000 and £125,140 of adjusted net income each extra £2 also removes £1 of "
                              "allowance: an effective 60% rate (rUK, 40% band) or 67.5% (Scotland, 45% advanced "
                              "band). Relief-at-source pension contributions and Gift Aid reduce adjusted net "
                              "income; salary sacrifice reduces pay itself."}, True)


if __name__ == "__main__":
    main()
