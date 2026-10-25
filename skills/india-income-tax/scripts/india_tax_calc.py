#!/usr/bin/env python3
"""
India individual income-tax estimator: old vs new regime, special-rate capital
gains, residency effects, and late-filing interest (234A/234B/234C) and fee
(234F).

Built for checking the portal's Part B-TI / B-TTI, not replacing it. The
portal's figure is the one that counts; use this to know what to expect and
to catch a wrong entry (a figure that is off by thousands means a schedule is
wrong).

Supported years (Indian FY, April-March):
  2024-25  (AY 2025-26)  - assumes all capital gains arose on/after 23 Jul 2024
  2025-26  (AY 2026-27)
  2026-27  (tax year 2026-27 under the Income-tax Act, 2025; Budget 2026 left
            slabs and rates unchanged - re-check before relying on it)

Not modelled: surcharge marginal relief, agricultural income, AMT, losses
set-off/carry-forward, grandfathering (enter the already-computed gain),
DTAA-rate income, VDA (crypto) 30% income, lottery 30% income, 115AD/FII rates.

Usage:
    python3 india_tax_calc.py input.json
    python3 india_tax_calc.py --example
"""
import json
import math
import sys
from datetime import date, timedelta

# ---------------------------------------------------------------- tables
NEW_SLABS = {
    "2024-25": [(300000, 0), (700000, .05), (1000000, .10), (1200000, .15), (1500000, .20), (None, .30)],
    "2025-26": [(400000, 0), (800000, .05), (1200000, .10), (1600000, .15), (2000000, .20), (2400000, .25), (None, .30)],
}
NEW_SLABS["2026-27"] = NEW_SLABS["2025-26"]
NEW_REBATE = {"2024-25": (700000, 25000), "2025-26": (1200000, 60000), "2026-27": (1200000, 60000)}
OLD_REBATE = (500000, 12500)
STD_DED = {"new": 75000, "old": 50000}
LTCG_112A_EXEMPT = 125000
RATE_111A, RATE_112A, RATE_112 = .20, .125, .125
CESS = .04


def old_slabs(age, resident):
    base = 250000
    if resident and age >= 80:
        base = 500000
    elif resident and age >= 60:
        base = 300000
    return [(base, 0), (500000, .05), (1000000, .20), (None, .30)] if base < 500000 else \
        [(500000, 0), (1000000, .20), (None, .30)]


def slab_tax(income, slabs):
    tax, lower = 0.0, 0
    for upper, rate in slabs:
        if upper is None or income <= upper:
            tax += max(0, income - lower) * rate
            return tax
        tax += (upper - lower) * rate
        lower = upper
    return tax


def surcharge_rate(total, regime):
    if total > 50_000_000:
        return .37 if regime == "old" else .25
    if total > 20_000_000:
        return .25
    if total > 10_000_000:
        return .15
    if total > 5_000_000:
        return .10
    return 0.0


# ---------------------------------------------------------------- core
def compute(cfg, regime):
    fy = cfg["fy"]
    status = cfg.get("residential_status", "NR").upper()
    resident = status in ("ROR", "RNOR", "R")
    inc = cfg.get("income", {})
    age = cfg.get("age", 30)
    notes = []

    salary = inc.get("salary_gross", 0)
    hp = inc.get("house_property", 0)
    os_slab = inc.get("other_sources_slab", 0)
    stcg_slab = inc.get("stcg_slab", 0)
    stcg_111a = inc.get("stcg_111a", 0)
    ltcg_112a = inc.get("ltcg_112a", 0)
    ltcg_112 = inc.get("ltcg_112", 0)

    # deductions
    ded = 0
    if salary:
        ded += min(salary, STD_DED[regime])
    if regime == "old":
        od = cfg.get("old_regime_deductions", {})
        ded += min(od.get("80C", 0), 150000)
        ded += od.get("80D", 0)
        if od.get("80TTA"):
            if resident and age >= 60:
                notes.append("80TTA ignored: resident senior citizens use 80TTB instead")
            else:
                ded += min(od["80TTA"], 10000)
        if od.get("80TTB"):
            if resident and age >= 60:
                ded += min(od["80TTB"], 50000)
            else:
                notes.append("80TTB ignored: only resident senior citizens")
        ded += od.get("hra_exemption", 0) + od.get("professional_tax", 0) + od.get("other", 0)
    else:
        ded += cfg.get("new_regime_deductions", {}).get("80CCD2", 0)

    # chapter VI-A deductions cannot reduce special-rate CG; cap at normal income
    normal_gross = salary + hp + os_slab + stcg_slab
    normal_income = max(0, normal_gross - ded)
    if ded > normal_gross:
        notes.append("Deductions exceed normal-rate income; excess is lost (cannot reduce special-rate gains)")

    ltcg_112a_taxable = max(0, ltcg_112a - LTCG_112A_EXEMPT)
    total_income = normal_income + stcg_111a + ltcg_112a + ltcg_112

    slabs = NEW_SLABS[fy] if regime == "new" else old_slabs(age, resident)
    exemption_limit = slabs[0][0]

    # unused basic exemption absorbs special-rate income: residents only
    unused = max(0, exemption_limit - normal_income)
    s111a, s112, s112a = stcg_111a, ltcg_112, ltcg_112a_taxable
    if resident and unused:
        take = min(s111a, unused); s111a -= take; unused -= take   # highest rate first
        take = min(s112, unused); s112 -= take; unused -= take
        take = min(s112a, unused); s112a -= take; unused -= take
    elif not resident and normal_income < exemption_limit and (stcg_111a or ltcg_112 or ltcg_112a_taxable):
        notes.append("Non-resident: unused basic exemption cannot absorb special-rate gains (111A/112/112A provisos)")

    tax_slab = slab_tax(normal_income, slabs)
    tax_special = s111a * RATE_111A + s112 * RATE_112 + s112a * RATE_112A

    # 87A rebate: residents only
    rebate = 0.0
    if resident:
        limit, cap = NEW_REBATE[fy] if regime == "new" else OLD_REBATE
        if total_income <= limit:
            if regime == "new":
                rebate = min(tax_slab, cap)  # from FY 2025-26 not available against special-rate tax
                if fy == "2024-25":
                    notes.append("FY 2024-25: rebate against 111A tax was disputed; this estimate allows slab tax only")
            else:
                rebate = min(tax_slab + s111a * RATE_111A, cap)  # never against 112A
        elif regime == "new":
            # marginal relief: tax on slab income cannot exceed income above the limit
            excess = total_income - limit
            if tax_slab > excess and normal_income == total_income:
                rebate = tax_slab - excess
                notes.append(f"87A marginal relief applied ({rebate:,.0f})")
    else:
        notes.append("Non-resident: no 87A rebate")

    tax_after_rebate = max(0, tax_slab + tax_special - rebate)
    sr_total = surcharge_rate(total_income, regime)
    special_share = tax_special / (tax_slab + tax_special) if (tax_slab + tax_special) else 0
    surcharge = tax_after_rebate * ((1 - special_share) * sr_total + special_share * min(sr_total, .15))
    if surcharge:
        notes.append("Surcharge applied without marginal relief; check the portal")
    cess = (tax_after_rebate + surcharge) * CESS
    gross_tax = tax_after_rebate + surcharge + cess

    return {
        "regime": regime,
        "total_income": round(total_income),
        "total_income_rounded_to_10": int(round(total_income / 10.0) * 10),
        "normal_rate_income": round(normal_income),
        "deductions_used": round(min(ded, normal_gross)),
        "tax_at_slab_rates": round(tax_slab, 2),
        "tax_at_special_rates": round(tax_special, 2),
        "special_rate_detail": {"111A@20%": round(s111a * RATE_111A, 2),
                                 "112A@12.5% after 1.25L": round(s112a * RATE_112A, 2),
                                 "112@12.5%": round(s112 * RATE_112, 2)},
        "rebate_87A": round(rebate, 2),
        "surcharge": round(surcharge, 2),
        "cess_4pct": round(cess, 2),
        "tax_liability": round(gross_tax, 2),
        "notes": notes,
    }


# ---------------------------------------------------------------- interest
def months_between(start, end):
    """Months or part of a month from start (inclusive) to end (inclusive)."""
    if end < start:
        return 0
    m = (end.year - start.year) * 12 + (end.month - start.month) + 1
    return m


def floor100(x):
    return max(0, math.floor(x / 100.0) * 100)


def interest(cfg, liability, tax_by_quarter):
    fy = cfg["fy"]
    y = int(fy.split("-")[0])
    tds = cfg.get("tds", 0)
    adv = [(date.fromisoformat(p["date"]), p["amount"]) for p in cfg.get("advance_tax", [])]
    adv_total = sum(a for _, a in adv)
    assessed = max(0, liability - tds)
    due = date.fromisoformat(cfg.get("due_date", f"{y + 1}-07-31"))
    filing = date.fromisoformat(cfg.get("filing_date", due.isoformat()))
    sat_date = date.fromisoformat(cfg.get("self_assessment_date", filing.isoformat()))
    out = {"assessed_tax_after_tds": round(assessed, 2)}

    # 234B: advance tax < 90% of assessed tax
    i234b = 0
    if assessed >= 10000 and adv_total < 0.9 * assessed:
        short = floor100(assessed - adv_total)
        months = months_between(date(y + 1, 4, 1), sat_date)
        i234b = short * 0.01 * months
        out["234B_months"] = months
    elif assessed < 10000:
        out["234B_note"] = "assessed tax under Rs 10,000: no advance tax liability, no 234B/234C"
    out["234B"] = round(i234b)

    # 234A: filed after due date, on tax unpaid by due date
    i234a = 0
    if filing > due:
        paid_by_due = adv_total + sum(cfg.get("self_assessment_paid_before_due", []) or [0])
        short = floor100(assessed - paid_by_due)
        months = months_between(due + timedelta(days=1), filing)  # from the day after the due date
        i234a = short * 0.01 * months
        out["234A_months"] = months
    out["234A"] = round(i234a)

    # 234C: deferment of instalments
    # Standard method: 15/45/75/100% of assessed tax by 15 Jun/15 Sep/15 Dec/15 Mar.
    # Capital-gains proviso: shortfall caused by gains is excused only if the tax on those
    # gains was actually paid in the remaining instalments. If (almost) nothing was paid
    # as advance tax, the proviso does not help and the standard method applies - this is
    # what the portal did on a real belated NRI return.
    def c_interest(bases):
        inst = [(date(y, 6, 15), .15, 3, .12), (date(y, 9, 15), .45, 3, .36),
                (date(y, 12, 15), .75, 3, None), (date(y + 1, 3, 15), 1.0, 1, None)]
        total, detail = 0, []
        for k, (dt, pct, months, safe) in enumerate(inst):
            base = bases[k]
            required = pct * base
            paid = sum(a for t, a in adv if t <= dt)
            if safe is not None and paid >= safe * base:
                amt = 0
            else:
                amt = floor100(required - paid) * 0.01 * months
            total += amt
            detail.append({"date": dt.isoformat(), "required": round(required), "paid": paid,
                           "interest": round(amt)})
        return total, detail

    i234c = 0
    if assessed >= 10000:
        i234c, detail = c_interest([assessed] * 4)
        out["234C_method"] = "standard"
        if tax_by_quarter and adv_total >= 0.9 * assessed:
            alt, alt_detail = c_interest([max(0, t - tds) for t in tax_by_quarter])
            if alt < i234c:
                i234c, detail = alt, alt_detail
                out["234C_method"] = "capital-gains proviso (tax on gains paid in later instalments)"
        out["234C_detail"] = detail
    out["234C"] = round(i234c)

    # 234F
    fee = 0
    total_income = cfg.get("_total_income", 0)
    if filing > due:
        fee = 1000 if total_income <= 500000 else 5000
        if cfg.get("_below_exemption"):
            fee = 0
    out["234F"] = fee
    out["interest_and_fee_total"] = out["234A"] + out["234B"] + out["234C"] + fee
    out["note"] = ("Estimate; the portal's figure prevails. 234C uses the capital-gains proviso only when "
                   "accrual dates are given AND advance tax actually covered the tax on the gains.")
    return out


EXAMPLE = {
    "fy": "2025-26",
    "residential_status": "NR",
    "age": 35,
    "income": {"salary_gross": 0, "house_property": 0, "other_sources_slab": 40000,
               "stcg_slab": 0, "stcg_111a": 50000, "ltcg_112a": 300000, "ltcg_112": 0},
    "accrual": {"stcg_111a": [0, 0, 50000, 0, 0], "ltcg_112a": [0, 300000, 0, 0, 0],
                "ltcg_112": [0, 0, 0, 0, 0], "stcg_slab": [0, 0, 0, 0, 0]},
    "old_regime_deductions": {"80C": 0, "80D": 0, "80TTA": 10000},
    "tds": 12480,
    "advance_tax": [],
    "due_date": "2026-07-31",
    "filing_date": "2026-10-15",
    "has_business_income": False,
}


def tax_by_quarter(cfg, regime):
    acc = cfg.get("accrual")
    if not acc:
        return None
    res = []
    for k in range(4):  # instalments: 15 Jun, 15 Sep, 15 Dec, 15 Mar
        sub = json.loads(json.dumps(cfg))
        for key in ("stcg_111a", "ltcg_112a", "ltcg_112", "stcg_slab"):
            if key in acc:
                sub["income"][key] = sum(acc[key][:k + 1])
        res.append(compute(sub, regime)["tax_liability"])
    return res


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--example":
        print(json.dumps(EXAMPLE, indent=2))
        return
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cfg = json.load(open(sys.argv[1]))
    if cfg["fy"] not in NEW_SLABS:
        raise SystemExit(f"Unsupported FY {cfg['fy']}; supported: {', '.join(NEW_SLABS)}")
    y = int(cfg["fy"].split("-")[0])
    due = date.fromisoformat(cfg.get("due_date", f"{y + 1}-07-31"))
    filing = date.fromisoformat(cfg.get("filing_date", due.isoformat()))
    belated = filing > due
    out = {"fy": cfg["fy"], "residential_status": cfg.get("residential_status", "NR"),
           "belated": belated, "regimes": {}}
    for regime in ("new", "old"):
        r = compute(cfg, regime)
        if regime == "old" and belated and not cfg.get("has_business_income"):
            r["available"] = False
            r["why_unavailable"] = ("Old regime can only be chosen in a return filed by the 139(1) due date "
                                    "(115BAC(6)); a belated return is taxed under the new regime.")
        else:
            r["available"] = True
        cfg["_total_income"] = r["total_income"]
        cfg["_below_exemption"] = r["total_income"] <= (NEW_SLABS[cfg["fy"]][0][0] if regime == "new"
                                                         else old_slabs(cfg.get("age", 30), False)[0][0])
        r["interest_and_fee"] = interest(cfg, r["tax_liability"], tax_by_quarter(cfg, regime))
        r["total_payable_before_self_assessment"] = round(
            r["tax_liability"] - cfg.get("tds", 0) - sum(p["amount"] for p in cfg.get("advance_tax", []))
            + r["interest_and_fee"]["interest_and_fee_total"])
        out["regimes"][regime] = r
    avail = {k: v for k, v in out["regimes"].items() if v["available"]}
    best = min(avail, key=lambda k: avail[k]["tax_liability"])
    out["cheaper_available_regime"] = best
    out["reminder"] = ("Pay the balance by Challan 280 / minor head 300 (self-assessment) before submitting; "
                       "round up to the next Rs 10. Portal figures prevail over this estimate.")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
