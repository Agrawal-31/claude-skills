#!/usr/bin/env python3
"""Self-test for india_tax_calc.py and residency_days.py on generic scenarios.

Run: python3 selftest.py   (exits non-zero on any failure)
All figures are hand-computed for FY 2025-26 (AY 2026-27) rules.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, cfg):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(cfg, f)
        path = f.name
    try:
        out = subprocess.run([sys.executable, "-I", os.path.join(HERE, script), path],
                             capture_output=True, text=True, check=True).stdout
    finally:
        os.unlink(path)
    return json.loads(out)


FAILS = []


def check(name, got, want, tol=1.0):
    ok = abs(got - want) <= tol if isinstance(want, (int, float)) else got == want
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got}, want {want}")
    if not ok:
        FAILS.append(name)


def base(**kw):
    cfg = {"fy": "2025-26", "residential_status": "ROR", "age": 35, "income": {},
           "tds": 0, "advance_tax": [], "due_date": "2026-07-31", "filing_date": "2026-07-20"}
    cfg.update(kw)
    return cfg


# A: resident salaried, both regimes, filed on time
r = run("india_tax_calc.py", base(income={"salary_gross": 1500000},
                                  old_regime_deductions={"80C": 150000, "80D": 25000}))
check("A new-regime tax 15L salary", r["regimes"]["new"]["tax_liability"], 97500)
check("A old-regime tax 15L salary with 80C+80D", r["regimes"]["old"]["tax_liability"], 202800)
check("A cheaper regime", r["cheaper_available_regime"], "new")

# B: salary 12.75L -> taxable 12L -> full 87A rebate in new regime
r = run("india_tax_calc.py", base(income={"salary_gross": 1275000}))
check("B new-regime tax at 12L taxable", r["regimes"]["new"]["tax_liability"], 0)

# C: marginal relief just above 12L
r = run("india_tax_calc.py", base(income={"salary_gross": 1285000}))
check("C marginal relief at 12.10L taxable", r["regimes"]["new"]["tax_liability"], 10400)

# D: resident uses unused basic exemption against 112A gains; non-resident cannot
inc = {"other_sources_slab": 100000, "ltcg_112a": 325000}
r = run("india_tax_calc.py", base(income=inc))
check("D resident 112A absorbed by exemption", r["regimes"]["new"]["tax_liability"], 0)
r = run("india_tax_calc.py", base(income=inc, residential_status="NR"))
check("D non-resident pays 12.5% on 2L", r["regimes"]["new"]["tax_liability"], 26000)

# E: belated return locks old regime; 234A/B/F on a generic NRI case
cfg = base(residential_status="NR", income={"other_sources_slab": 20000, "ltcg_112a": 525000},
           tds=6240, filing_date="2026-11-10")
r = run("india_tax_calc.py", cfg)
n = r["regimes"]["new"]
check("E old regime unavailable when belated", r["regimes"]["old"]["available"], False)
check("E tax 4L x 12.5% + cess", n["tax_liability"], 52000)
# assessed 45,760 -> 45,700; 234A Aug-Nov = 4 months; 234B Apr-Nov = 8 months
check("E 234A", n["interest_and_fee"]["234A"], 1828)
check("E 234B", n["interest_and_fee"]["234B"], 3656)
check("E 234F (income > 5L)", n["interest_and_fee"]["234F"], 5000)

# F: advance tax paid on time after a September gain -> proviso removes 234C
cfg = base(residential_status="NR", income={"ltcg_112a": 525000},
           accrual={"ltcg_112a": [0, 525000, 0, 0, 0]},
           advance_tax=[{"date": "2025-09-15", "amount": 52000}])
r = run("india_tax_calc.py", cfg)
check("F 234C nil under capital-gains proviso", r["regimes"]["new"]["interest_and_fee"]["234C"], 0)
check("F 234B nil (advance tax >= 90%)", r["regimes"]["new"]["interest_and_fee"]["234B"], 0)

# ---- residency
res = {"fy": "2025-26", "indian_citizen": True, "came_on_visit": True,
       "liable_to_tax_elsewhere": True, "history_start": "2012-04-01",
       "lived_in_india_until": "2021-11-30", "indian_income_excl_foreign": 400000,
       "trips": [{"arrive": "2025-04-15", "depart": "2025-04-30"},
                 {"arrive": "2025-12-01", "depart": "2025-12-20"}]}
r = run("residency_days.py", res)
check("R1 days this FY (both travel days counted)", r["days_in_india_this_fy"], 36)
check("R1 status NR", r["status"], "NR")

res2 = dict(res, indian_income_excl_foreign=2000000,
            trips=[{"arrive": "2023-04-01", "depart": "2023-08-31"},
                   {"arrive": "2024-04-01", "depart": "2024-08-31"},
                   {"arrive": "2025-04-01", "depart": "2025-08-15"}])
r = run("residency_days.py", res2)
check("R2 137 days, income > 15L, 365+ in 4 yrs -> RNOR", r["status"], "RNOR")

res3 = dict(res, indian_income_excl_foreign=2000000, liable_to_tax_elsewhere=False)
r = run("residency_days.py", res3)
check("R3 deemed resident -> RNOR", r["status"], "RNOR")

res4 = {"fy": "2025-26", "indian_citizen": True, "came_on_visit": False,
        "liable_to_tax_elsewhere": False, "history_start": "2010-04-01",
        "indian_income_excl_foreign": 300000,
        "trips": [{"arrive": "2025-05-01", "depart": "2026-03-31"}]}
r = run("residency_days.py", res4)
check("R4 returning after 10+ yrs abroad: 335 days -> RNOR", r["status"], "RNOR")

res5 = dict(res4, history_start="2010-04-01", lived_in_india_until="2026-03-31", trips=[])
r = run("residency_days.py", res5)
check("R5 lifelong resident -> ROR", r["status"], "ROR")

# ---- 112A helper: grandfathered cost = max(cost, min(FMV, sale))
csv_text = """isin,name,units,buy_date,sell_date,sale_value,cost,fmv_31jan2018_per_unit,transfer_expenses
INF000X01001,Example Large Cap Fund,1000,2021-05-10,2025-09-02,150000,100000,,0
INE000Y01011,Example Ltd,10,2016-03-01,2025-10-06,25000,12000,2000,0
INF000X01003,Example Flexi Cap Fund,200,2025-03-01,2025-11-20,30000,28000,,0
"""
with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
    fh.write(csv_text)
    cpath = fh.name
txt = subprocess.run([sys.executable, "-I", os.path.join(HERE, "schedule_112a_helper.py"), cpath],
                     capture_output=True, text=True, check=True).stdout
os.unlink(cpath)
check("H 112A total incl. grandfathered BE row", "112A total (before the Rs 1.25 lakh exemption, which the portal applies itself): 55000" in txt, True)
check("H 111A short-term total", "111A short-term total: 2000" in txt, True)

print("\nALL PASS" if not FAILS else f"\n{len(FAILS)} FAILED: {FAILS}")
sys.exit(1 if FAILS else 0)
