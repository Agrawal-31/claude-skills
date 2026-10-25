# Rates, limits and dates (labelled by year)

Checked October 2026. Each row says which year it is for. **Confirm the current year's
figures** on incometax.gov.in / incometaxindia.gov.in or the latest Finance Act before relying
on them; Budget speeches are proposals until enacted.

Year labels: FY = financial year the income is earned in. AY = assessment year (FY + 1)
under the 1961 Act. "Tax year 2026-27" = FY 2026-27 under the Income-tax Act, 2025.

## Slabs

### New regime (default)

| Taxable income (Rs) | FY 2024-25 (AY 2025-26) | FY 2025-26 (AY 2026-27) and tax year 2026-27 |
|---|---|---|
| 0 - 3,00,000 | 0% | 0% |
| 3,00,001 - 4,00,000 | 5% | 0% |
| 4,00,001 - 7,00,000 | 5% | 5% (to 8 lakh) |
| 7,00,001 - 8,00,000 | 10% | 5% |
| 8,00,001 - 10,00,000 | 10% | 10% |
| 10,00,001 - 12,00,000 | 15% | 10% |
| 12,00,001 - 15,00,000 | 20% | 15% (to 16 lakh) |
| 15,00,001 - 16,00,000 | 30% | 15% |
| 16,00,001 - 20,00,000 | 30% | 20% |
| 20,00,001 - 24,00,000 | 30% | 25% |
| above 24,00,000 | 30% | 30% |

Budget 2026 left slabs and rates unchanged for tax year 2026-27 (per Grant Thornton and
ClearTax summaries; confirm against the Finance Act 2026).

### Old regime (all years shown)

| Taxable income (Rs) | Below 60 / any NR | Resident 60-79 | Resident 80+ |
|---|---|---|---|
| 0 - 2,50,000 | 0% | 0% | 0% |
| 2,50,001 - 3,00,000 | 5% | 0% | 0% |
| 3,00,001 - 5,00,000 | 5% | 5% | 0% |
| 5,00,001 - 10,00,000 | 20% | 20% | 20% |
| above 10,00,000 | 30% | 30% | 30% |

Non-residents always use the "below 60" column regardless of age.

## Rebate u/s 87A (residents only; 2025 Act s.156)

| Year | New regime | Old regime |
|---|---|---|
| FY 2024-25 | up to Rs 25,000 if total income <= Rs 7 lakh | up to Rs 12,500 if <= Rs 5 lakh |
| FY 2025-26 on | up to Rs 60,000 if total income <= Rs 12 lakh, with marginal relief just above | same as above |

- Not available to non-residents.
- From FY 2025-26 the new-regime rebate applies to tax on slab-rate income only, not to tax
  on special-rate income (111A, 112, 112A etc.); total income including those gains still
  counts for the Rs 12 lakh test. 112A tax was never eligible for the rebate.
- Salaried resident with only salary: up to Rs 12.75 lakh gross is tax-free in the new
  regime (Rs 75,000 standard deduction + Rs 12 lakh rebate limit).

## Surcharge and cess

| Total income | Surcharge | Notes |
|---|---|---|
| > Rs 50 lakh | 10% | |
| > Rs 1 crore | 15% | |
| > Rs 2 crore | 25% | |
| > Rs 5 crore | 37% old regime; capped at 25% new regime | |
| Cap on 111A/112/112A gains and dividends | 15% max | |

Health and education cess: 4% on tax plus surcharge. Marginal relief applies at each
threshold (not modelled by the script).

## Capital gains rates (transfers on or after 23 July 2024; FY 2025-26 throughout)

| Asset | Long-term if held | STCG | LTCG |
|---|---|---|---|
| Listed equity shares, equity-oriented MF units, business trust units (STT paid) | > 12 months | 20% (111A) | 12.5% above Rs 1.25 lakh per year (112A) |
| Other listed securities (listed bonds etc.) | > 12 months | slab | 12.5% (112), no indexation |
| Non-equity MF units other than "specified mutual funds" (international FoFs, foreign-index funds, gold/silver funds, hybrids under 65% equity and not debt-heavy) | > 24 months | slab | 12.5% (112), no indexation |
| "Specified mutual fund" units bought on/after 1 Apr 2023 (from FY 2025-26: fund with > 65% in debt and money-market instruments, or a fund investing >= 65% in such funds; s.50AA, 2025 Act s.76) | never long-term | slab, any holding period | n/a |
| Unlisted shares | > 24 months | slab | 12.5% (112); NR gets no indexation or forex protection |
| Land / building | > 24 months | slab | 12.5% without indexation; resident individuals/HUFs who acquired before 23 Jul 2024 may choose 20% with indexation (not available to NRs) |
| Virtual digital assets | n/a | 30% flat | 30% flat |

- FY 2024-25 is split: transfers before 23 Jul 2024 at 15% STCG / 10% LTCG over Rs 1 lakh
  (equity); later transfers at the rates above. The calculator assumes all FY 2024-25 gains
  are post-23 July.
- The Rs 1.25 lakh 112A exemption applies to residents and non-residents alike, once per year.
- Unused basic exemption can absorb 111A/112/112A gains for **residents only**.
- Grandfathering for equity bought on or before 31 Jan 2018: cost = higher of actual cost and
  the lower of (FMV on 31 Jan 2018, sale value). s.55(2)(ac); 2025 Act s.90.
- Budget 2026 (per commentary): capital-gains rates unchanged; buyback proceeds now taxed as
  capital gains in shareholders' hands; SGB redemption exemption limited to original
  subscribers.

## TDS rates on payments to non-residents (s.195 / 196A etc.; 2025 Act s.393)

All plus surcharge and 4% cess; treaty rate applies instead if lower and the payer has the
TRC + Form 10F + PAN.

| Payment | Domestic rate |
|---|---|
| NRO interest | 30% (about 31.2% with cess) |
| Dividends / MF income distribution | 20% |
| STCG 111A | 20% |
| LTCG 112A (above Rs 1.25 lakh) | 12.5% |
| LTCG 112 (property, unlisted, non-equity funds) | 12.5% |
| STCG at slab (non-equity funds etc.) | 30% |
| Rent | 30% |

A lower or nil deduction certificate (s.197, Form 13; 2025 Act s.395) is available on
application where actual liability is lower, e.g. on a property sale.

## Deductions (old regime unless stated)

| Section (1961 / 2025 Act) | Limit | NR? |
|---|---|---|
| 80C / 123 | Rs 1.5 lakh | Yes (some instruments, e.g. new PPF accounts, not open to NRs) |
| 80D / 126 | Rs 25,000 self+family (Rs 50,000 if senior), + parents Rs 25,000/50,000 | Yes |
| 80TTA / 153 | Rs 10,000 savings interest (non-seniors) | Yes (NRO savings) |
| 80TTB / 153 | Rs 50,000 deposit interest | Resident seniors only |
| 80CCD(2) | employer NPS: 14% of salary new regime, 10% old | Both regimes |

## Advance tax (s.208-211; 2025 Act s.404-408)

- Required if tax for the year after TDS is Rs 10,000 or more. Resident seniors (60+) with
  no business income are exempt.
- Instalments: 15% by 15 June, 45% by 15 Sept, 75% by 15 Dec, 100% by 15 March.
- Capital gains / dividends arising after an instalment date: no 234C interest if the tax on
  them is paid in the remaining instalments. If nothing is paid, the proviso doesn't help:
  a real belated NRI return was charged 234C on the standard 15/45/75/100% schedule.
- Payment: Challan 280, minor head 100 (advance tax), AY = FY + 1.

## Interest and fees (1961 Act; 2025 Act numbers per commentary mapping)

| | Rule | 2025 Act |
|---|---|---|
| 234A | 1% per month or part month on tax unpaid at the due date, from the day after the due date to the filing date | s.423 |
| 234B | 1% per month or part month on the shortfall if advance tax < 90% of assessed tax, from 1 April of the AY to the date of payment | s.424 |
| 234C | 1% per month on instalment shortfalls: 3 months for each of the first three, 1 month for March; 12% / 36% safe harbours for June / September | s.425 |
| 234F fee | Rs 5,000 if filed after the 139(1) due date; Rs 1,000 if total income does not exceed Rs 5 lakh; nil if total income is within the basic exemption | s.428 |
| 244A refund interest | 0.5% per month on refunds (reduced/denied for delay attributable to the taxpayer) | s.437 |

- Interest is computed on the amount rounded down to the nearest Rs 100; part of a month
  counts as a full month. Total income and tax are rounded to the nearest Rs 10.
- "Assessed tax" = tax on total income less TDS/TCS and relief.
- Month counting example: due 31 July, filed and paid in early October -> 234A runs
  August-October (3 months), 234B April-October (7 months). The calculator's 234A/B/C/F
  matched the portal to the rupee on a real belated NRI return with no advance tax.

## Key dates for AY 2026-27 (FY 2025-26)

| Date | What | Source/status |
|---|---|---|
| 31 Jul 2026 | 139(1) due date: no business income (ITR-1, ITR-2) | not extended |
| 31 Aug 2026 | Non-audit business/professional income (ITR-3/ITR-4) | Finance Act 2026, per commentary |
| 31 Oct 2026 | Audit cases | |
| 30 Nov 2026 | Transfer-pricing cases | |
| 31 Dec 2026 | Belated return 139(4) last date (or before assessment completes) | |
| 31 Mar 2027 | Revised return 139(5) outer limit (extended from 31 Dec by Finance Act 2026; fee for revisions after 9 months reported as Rs 1,000 / Rs 5,000) | commentary; verify |
| 31 Mar 2031 | ITR-U 139(8A) outer limit (48 months from end of AY) | Finance Act 2025 |
| 30 days from upload | e-verification | CBDT notification 5/2022 |

For tax year 2026-27 (return filed in 2027) the same calendar applies: 31 July 2027 for
returns without business income.

## Updated return (ITR-U) additional tax

| Filed within (from end of the AY) | Additional tax on (tax + interest) |
|---|---|
| 12 months | 25% |
| 24 months | 50% |
| 36 months | 60% |
| 48 months | 70% |

Finance Act 2025 extended the window from 24 to 48 months. Budget 2026 reportedly allows
ITR-U after a reassessment notice with a further 10% (unverified; check before relying).

## Black Money Act (foreign assets of residents)

- Penalty for non-disclosure / wrong disclosure of foreign assets in Schedule FA: Rs 10 lakh
  (s.43 BMA). Tribunal (Mumbai Special Bench, Oct 2025) held it discretionary, not automatic.
- No penalty where the aggregate value of non-immovable foreign assets (e.g. bank balances)
  is Rs 20 lakh or less (Finance (No. 2) Act 2024, from 1 Oct 2024; previously Rs 5 lakh).
  Still disclose: the threshold excuses the penalty, not the disclosure.
