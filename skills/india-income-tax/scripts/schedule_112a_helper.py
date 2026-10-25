#!/usr/bin/env python3
"""
Schedule 112A / 111A helper for listed equity shares and equity-oriented
mutual fund units (STT paid), FY 2025-26 rules (transfers after 23 Jul 2024).

Reads a lot-level CSV (one row per purchase lot sold) and prints:
  * each lot classified short-term (111A) or long-term (112A),
  * the ONE consolidated "acquired after 31 Jan 2018" (AE) row the portal wants,
  * one row per pre-1 Feb 2018 (BE) holding with the section 55(2)(ac)
    grandfathered cost  = max(actual cost, min(FMV on 31 Jan 2018, sale value)),
  * Table F (quarter of accrual) totals.

Why consolidated: on the e-filing portal, Schedule 112A rows for units bought
after 31 Jan 2018 are entered as a single line (ISIN "INNOTREQUIRD", name
"CONSOLIDATED"); a per-fund CSV upload skipped rows ("common.errors.csv_row_skip")
in a real filing. Whole rupees only. Enter BE rows individually with their ISIN.

CSV columns (header required):
  isin,name,units,buy_date,sell_date,sale_value,cost,fmv_31jan2018_per_unit,transfer_expenses
Dates ISO (YYYY-MM-DD). fmv_31jan2018_per_unit only for lots bought on or before
31 Jan 2018 (find it on the exchange's 31 Jan 2018 closing price / the AIS).

Do NOT put non-equity funds here (international FoFs, index funds tracking
foreign indices, debt, gold, most FoFs): those go in Schedule CG under section
112 / slab rate. Check the fund's classification in AIS and the AMC factsheet.

Usage: python3 schedule_112a_helper.py lots.csv
"""
import csv
import sys
from datetime import date

CUTOFF = date(2018, 1, 31)


def add_months(d, n):
    y, m = divmod(d.month - 1 + n, 12)
    y += d.year
    m += 1
    for day in (d.day, 30, 29, 28):
        try:
            return date(y, m, day)
        except ValueError:
            continue


def quarter(d):
    """Table F bucket for an FY: up to 15/6, 16/6-15/9, 16/9-15/12, 16/12-15/3, 16/3-31/3."""
    md = (d.month, d.day)
    if (4, 1) <= md <= (6, 15):
        return 0
    if (6, 16) <= md <= (9, 15):
        return 1
    if (9, 16) <= md <= (12, 15):
        return 2
    if md >= (12, 16) or md <= (3, 15):
        return 3
    return 4


def f(x):
    return float(x) if str(x).strip() not in ("", "None") else 0.0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")))
    ae = {"sale": 0.0, "cost": 0.0, "exp": 0.0}
    be_rows, st, lt_q, st_q = [], 0.0, [0.0] * 5, [0.0] * 5
    print("Lot classification:")
    for r in rows:
        buy, sell = date.fromisoformat(r["buy_date"]), date.fromisoformat(r["sell_date"])
        sale, cost, exp = f(r["sale_value"]), f(r["cost"]), f(r.get("transfer_expenses", 0))
        long_term = sell > add_months(buy, 12)
        q = quarter(sell)
        if not long_term:
            gain = sale - cost - exp
            st += gain
            st_q[q] += gain
            print(f"  ST 111A  {r['name'][:40]:40} gain {gain:12,.2f}  (held {buy} -> {sell})")
            continue
        if buy <= CUTOFF:
            units = f(r["units"])
            fmv_total = units * f(r.get("fmv_31jan2018_per_unit", 0))
            col9 = min(sale, fmv_total)
            col7 = max(cost, col9)
            gain = sale - col7 - exp
            be_rows.append({"isin": r["isin"], "name": r["name"], "units": units,
                            "sale_price_per_unit": round(sale / units, 2) if units else 0,
                            "col6_sale": round(sale), "col8_cost": round(cost),
                            "col10_fmv_per_unit": f(r.get("fmv_31jan2018_per_unit", 0)),
                            "col11_fmv_total": round(fmv_total), "col9_lower_of_6_11": round(col9),
                            "col7_cost_used": round(col7), "col12_exp": round(exp),
                            "col14_gain": round(gain)})
        else:
            ae["sale"] += sale
            ae["cost"] += cost
            ae["exp"] += exp
            gain = sale - cost - exp
        lt_q[q] += gain
        print(f"  LT 112A  {r['name'][:40]:40} gain {gain:12,.2f}  ({'BE' if buy <= CUTOFF else 'AE'})")

    ae_gain = round(ae["sale"]) - round(ae["cost"]) - round(ae["exp"])
    print("\nSchedule 112A - consolidated AE row (enter by hand, whole rupees):")
    print(f"  1a: After 31st January 2018 | ISIN: INNOTREQUIRD | Name: CONSOLIDATED")
    print(f"  (6) Full value of consideration: {round(ae['sale'])}")
    print(f"  (8) Cost of acquisition:         {round(ae['cost'])}")
    print(f"  (12) Expenditure on transfer:    {round(ae['exp'])}")
    print(f"  (14) Balance should read:        {ae_gain}")
    for b in be_rows:
        print(f"\nSchedule 112A - BE row: {b}")
    total_lt = ae_gain + sum(b["col14_gain"] for b in be_rows)
    print(f"\n112A total (before the Rs 1.25 lakh exemption, which the portal applies itself): {total_lt}")
    print(f"111A short-term total: {round(st)}")
    labels = ["up to 15/6", "16/6-15/9", "16/9-15/12", "16/12-15/3", "16/3-31/3"]
    print("\nTable F (Schedule CG, item F) - enter whole rupees:")
    print("  STCG 111A @20%: " + ", ".join(f"{l}: {round(v)}" for l, v in zip(labels, st_q)))
    print("  LTCG 112A @12.5% (combine with any 112 gains in the same row): " +
          ", ".join(f"{l}: {round(v)}" for l, v in zip(labels, lt_q)))
    print("\nCheck: these totals must equal Schedule CG / BFLA lines exactly or validation fails.")


if __name__ == "__main__":
    main()
