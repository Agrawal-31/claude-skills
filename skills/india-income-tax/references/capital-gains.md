# Capital gains: classify, compute, enter

Rates and holding periods are in `rates-and-limits.md`. This file is the method.

## Step 1: classify every lot

For each sale, record: security/fund, ISIN, units, purchase date, sale date, sale value,
cost, expenses, and the fund type.

**Mutual funds are the trap.** A statement may label every fund "equity". Indian tax
classes them by what they hold:

| Fund type (examples) | Tax class | Long-term after | Where |
|---|---|---|---|
| Indian equity funds: large/mid/small cap, flexi cap, ELSS, sector funds, index funds on Indian indices, "balanced advantage"/dynamic asset allocation funds that keep >= 65% Indian equity, arbitrage funds | Equity-oriented (STT paid) | 12 months | 111A / 112A |
| International funds and FoFs (Nasdaq 100 FoF, S&P 500 index fund, global FoFs), gold/silver ETFs and FoFs, hybrids with < 65% equity that are not debt-heavy | Other units: s.112 / slab | 24 months | Schedule CG "other assets" |
| Debt funds, liquid funds, FoFs investing >= 65% in debt funds - bought on/after 1 Apr 2023 | "Specified mutual fund" (s.50AA): always short-term | never | Schedule CG short-term, slab rate |
| Debt funds bought before 1 Apr 2023 | Other units | 24 months | s.112 at 12.5% without indexation |

How to check: AIS often splits "equity units" from "other units"; the AMC factsheet and the
fund's own tax note say whether it is equity-oriented. When AIS and the broker statement
disagree, follow the law (what the fund holds) and say which you used and why; flag it for a
CA if the amount matters.

**Shares:** listed shares sold on an exchange with STT -> 111A/112A. Check the purchase date
in the broker's transaction/DP statement, not from the AIS FMV column.

**Holding period:** count from purchase (allotment) date to sale date; "more than 12 months"
means at least 12 months and a day. Each SIP instalment is its own lot, so one redemption
can produce both long- and short-term gains (a common source of a small slab-rate STCG line
alongside a big LTCG line).

## Step 2: compute

1. 111A STCG: sale - cost - expenses, taxed 20%.
2. 112A LTCG: sum of all equity LT gains and losses in the year (net), then the portal
   subtracts Rs 1.25 lakh; 12.5% on the rest. Grandfathered lots (bought on/before 31 Jan
   2018): cost = max(actual cost, min(FMV on 31 Jan 2018 x units, sale value)).
3. Section 112 LTCG on other assets: 12.5% without indexation (property bought before
   23 Jul 2024 by a resident individual: choice of 20% with indexation).
4. STCG on non-equity assets: add to slab income.
5. Set-off: STCL against STCG or LTCG; LTCL only against LTCG; carry forward 8 years only if
   the return is filed by the 139(1) due date.
6. Non-residents: no basic-exemption absorption and no 87A against these gains.

`scripts/schedule_112a_helper.py lots.csv` does 1-2 from a lot CSV and prints the portal
rows and Table F. `scripts/india_tax_calc.py` then gives the tax.

## Step 3: enter in Schedule CG and 112A (ITR-2, AY 2026-27 layout)

Short-term (Part A):

| Item | Use for | Fields |
|---|---|---|
| A2 "equity share / unit of equity oriented fund on which STT is paid" -> section **111A** (the "for others" option; 115AD is for FIIs) | equity STCG | Full value of consideration, cost without indexation, cost of improvement 0, expenses, loss to be disallowed 0 |
| A3 | shares of Indian companies bought in foreign currency (NR, s.48 first proviso) | skip for MF units |
| A4 | FIIs only | skip |
| **A5 "sale of assets other than at A1-A4"** | non-equity fund STCG (slab rate) | Sale value goes in **(a)(ii) "assets other than unquoted shares"**; (a)(i)/(c) unquoted-share lines stay 0 |

Long-term (Part B):

| Item | Use for |
|---|---|
| B2 | residents only (property etc. with indexation) |
| **B3 "LTCG u/s 112A"** | opens Schedule 112A; its total pulls back here |
| B4, B5 | unlisted shares / bonds |
| B6 | FIIs |
| B7 | Chapter XII-A (optional NRI special scheme on specified foreign-exchange assets; rarely used) |
| **B8 "assets where B1-B7 don't apply"** | non-equity fund LTCG at 12.5% (s.112, no indexation). Again, sale value in **"assets other than unquoted shares"** |

**Schedule 112A, as the portal actually behaved (AY 2026-27):**

- Rows for shares/units acquired **after 31 Jan 2018** collapse into **one row**: column 1a
  "After 31st January 2018", ISIN `INNOTREQUIRD`, name `CONSOLIDATED`, units and price 0.
  Only full value of consideration (6), cost (8) and expenses (12) are editable. Enter the
  combined totals of all AE lots, whole rupees.
- Rows for holdings acquired **on or before 31 Jan 2018** are one per ISIN: ISIN, name,
  units, sale price per unit, cost (8), FMV per unit on 31 Jan 2018 (10). Columns 7, 9, 11,
  13, 14 compute themselves.
- CSV upload: the portal's template exists, but a per-fund CSV was rejected with
  `common.errors.csv_row_skip` (AE rows must have FMV columns blank, not 0; whole rupees;
  no quotes; latest template only). Manual entry of one AE row plus BE rows was faster and
  worked. If uploading, delete any existing row first or it double counts.
- Line b (54F deduction) stays 0 unless reinvesting in a house.

**Table F "information about accrual/receipt of capital gain"** (bottom of Schedule CG):
gains by the quarter of the sale date - up to 15/6, 16/6-15/9, 16/9-15/12, 16/12-15/3,
16/3-31/3 - in rows by rate: STCG 20% (111A), STCG 30%, STCG applicable rate, STCG DTAA rate,
LTCG 12.5% (112A and 112 share one row), LTCG DTAA rate, VDA. Rules:

- Each row's total must equal that gain type after set-off (BFLA lines) **exactly**; the
  Rs 1.25 lakh exemption is applied later, so enter the full gain.
- After editing any CG entry, re-check the cost field: in a real filing, moving a sale value
  from the unquoted line to "other assets" silently changed the cost by a few rupees,
  making the gain differ from Table F and failing validation with "Table F Sl. No. 3
  breakup is not equal to item 3v of BFLA".
- Table F drives 234C interest, so dates matter.

## NRI-specific

- **TDS on redemption:** fund houses and brokers deduct TDS from NRI sales (20% STCG, 12.5%
  LTCG etc.). If no TDS appears, the folio is probably tagged resident; the person pays by
  self-assessment and should fix the tag.
- **Treaty:** under the India-UK DTAA, gains on Indian shares and funds are taxable in India
  under Indian law. The India-Singapore DTAA (Article 13) was held by the Mumbai ITAT in
  Anushka Sanjay Shah v ITO (March 2025, AY 2022-23) to make a Singapore resident's Indian
  mutual-fund gains taxable only in Singapore (units are not "shares"). One tribunal ruling,
  needs a TRC and Form 10F, open to challenge: check before relying on it for a large
  redemption.
- **Planning note for next time:** the Rs 1.25 lakh 112A exemption is annual. Selling a
  large equity portfolio in one FY uses it once; spreading sales across FYs (where the
  person's other constraints allow) saves up to Rs 15,625 of tax per extra year used. Paying
  the tax as advance tax in the instalment after each sale avoids 234B/234C interest.
- **The other country:** many residence countries tax the same gains (the UK treats most
  Indian mutual funds as non-reporting offshore funds, taxing gains as income). Give the
  residence-country return each gain with purchase and sale dates and the Indian tax by
  gain type; see the sibling skill uk-personal-tax for the UK side.
