# Rates and thresholds, 2024-25 to 2026-27

Checked against GOV.UK on 24 October 2026. Before relying on a figure for the current year, open the cited page and confirm it; add a new column when a new year starts. `scripts/uk_tax_calc.py` must match this file.

## Contents
1. Income tax: allowances and rUK bands
2. Scotland (non-savings income only)
3. Savings and dividends
4. Capital gains tax
5. Child Benefit charge, pensions, other thresholds
6. Self Assessment dates, penalties, interest
7. Announced changes after 2026-27
8. Stale figures a model tends to produce

## 1. Income tax: allowances and rUK bands (England, Wales, NI)

Source: [Income Tax rates and allowances: current and past](https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past)

| | 2024-25 | 2025-26 | 2026-27 |
|---|---|---|---|
| Personal allowance | £12,570 | £12,570 | £12,570 |
| Income limit (taper £1 per £2 above) | £100,000 | £100,000 | £100,000 |
| Allowance nil at adjusted net income of | £125,140 | £125,140 | £125,140 |
| Basic rate 20%, taxable income up to | £37,700 | £37,700 | £37,700 |
| Higher rate 40% | £37,701 to £125,140 | same | same |
| Additional rate 45% | over £125,140 | same | same |
| Blind person's allowance | £3,070 | £3,130 | £3,250 |
| Married couple's allowance (max / min) | £11,080 / £4,280 | £11,270 / £4,360 | £11,700 / £4,530 |

With a full allowance, the higher rate starts at £50,270 of income. Bands apply to taxable income (after the allowance). Gift Aid and relief-at-source pension contributions, grossed up, extend the basic and higher rate limits and reduce adjusted net income. Salary sacrifice reduces pay itself.

Marriage allowance (£1,260 transfer, 10% of the allowance) is unchanged in principle; confirm on [gov.uk/marriage-allowance](https://www.gov.uk/marriage-allowance) before quoting.

## 2. Scotland: non-savings income

Same source. Bands are on taxable income. Scottish rates apply to earnings, pensions, rent and other non-savings income only.

| Band | Rate | 2024-25 | 2025-26 | 2026-27 |
|---|---|---|---|---|
| Starter | 19% | up to £2,306 | up to £2,827 | up to £3,967 |
| Basic | 20% | £2,307 to £13,991 | £2,828 to £14,921 | £3,968 to £16,956 |
| Intermediate | 21% | £13,992 to £31,092 | £14,922 to £31,092 | £16,957 to £31,092 |
| Higher | 42% | £31,093 to £62,430 | same | same |
| Advanced | 45% | £62,431 to £125,140 | same | same |
| Top | 48% | over £125,140 | same | same |

[gov.uk/scottish-income-tax](https://www.gov.uk/scottish-income-tax) shows 2026-27 in gross terms: starter £12,571 to £16,537, basic to £29,526, intermediate to £43,662, higher to £75,000, advanced to £125,140.

Unverified detail: how the band extension for relief-at-source pensions and Gift Aid is applied across the Scottish bands, and which band test decides the personal savings allowance for a Scottish taxpayer. The script extends Scottish limits above the starter band and uses UK limits for the PSA. Check HMRC guidance if the answer is near a band edge.

## 3. Savings and dividends (UK-wide, including Scotland)

| | 2024-25 | 2025-26 | 2026-27 | Source |
|---|---|---|---|---|
| Starting rate for savings (0%) | up to £5,000 | up to £5,000 | up to £5,000 | rates page above |
| Personal savings allowance | £1,000 basic, £500 higher, £0 additional | same | same | standard rule, confirm on [gov.uk/apply-tax-free-interest-on-savings](https://www.gov.uk/apply-tax-free-interest-on-savings) |
| Savings rates | 20 / 40 / 45% | same | same | |
| Dividend allowance | £500 | £500 | £500 | rates page above |
| Dividend rates (basic / higher / additional) | 8.75 / 33.75 / 39.35% | 8.75 / 33.75 / 39.35% | **10.75 / 35.75** / 39.35% | rates page above |

The starting rate band shrinks £1 for each £1 of taxable non-savings income, so it is gone once non-savings income exceeds £17,570. The PSA and dividend allowance are nil-rate bands: they still use up basic-rate band. ISA income is ignored completely.

## 4. Capital gains tax

Source: [CGT rates and annual tax-free allowances](https://www.gov.uk/government/publications/rates-and-allowances-capital-gains-tax/capital-gains-tax-rates-and-annual-tax-free-allowances)

| | 2024-25 | 2025-26 | 2026-27 |
|---|---|---|---|
| Annual exempt amount (individuals) | £3,000 | £3,000 | £3,000 |
| Shares and other assets, basic / higher | 10 / 20% to 29 Oct 2024; 18 / 24% from 30 Oct 2024 | 18 / 24% | 18 / 24% |
| Residential property | 18 / 24% | 18 / 24% | 18 / 24% |
| Business Asset Disposal / Investors' Relief | 10% | 14% | 18% |

Gains are taxed at the basic rate to the extent of unused basic-rate band after income. Trustees' exempt amount is £1,500.

Reporting triggers (SA108 notes 2025-26, quoted in an HMRC PDF and [ICAEW guidance](https://www.icaew.com/insights/tax-news/2025/oct-2025/cgt-tips-for-202425-tax-returns)): complete SA108 if disposals of chargeable assets were worth more than **£50,000**, or chargeable gains before losses exceed the annual exempt amount, or you want to claim losses or make a claim/election (including any FIG claim). The old "4 x annual exempt amount" proceeds test is out of date; don't use it (it cost one user a pointless dispute with an accountant). UK residential property: report and pay within 60 days of completion ([gov.uk](https://www.gov.uk/capital-gains-tax/reporting-and-paying-capital-gains-tax)). From 2024-25 the return has a separate cryptoasset section ([HMRC crypto guidance](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets)).

## 5. Child Benefit charge, pensions, other thresholds

| Item | Figure | Source |
|---|---|---|
| High Income Child Benefit Charge | 1% of Child Benefit per £200 of adjusted net income over £60,000; all of it at £80,000 (2024-25 onward) | [gov.uk/child-benefit-tax-charge](https://www.gov.uk/child-benefit-tax-charge) |
| HICBC via PAYE | allowed only if you don't otherwise need a return | same |
| Pension annual allowance | £60,000; taper if threshold income > £200,000 and adjusted income > £260,000; 3-year carry forward | [gov.uk annual allowance](https://www.gov.uk/tax-on-your-private-pension/annual-allowance) |
| Tapered allowance minimum, MPAA | £10,000 each (standard figures, not shown on that page: confirm) | |
| OWR cap | lower of 30% of qualifying employment income and £300,000 | [EIM43600](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600) |
| FIG regime | first 4 tax years of UK residence after 10 consecutive years of non-residence | [HS266](https://www.gov.uk/government/publications/foreign-income-and-gains-fig-regime-self-assessment-helpsheet-hs266/hs266-foreign-income-and-gains-fig-regime-2026) |
| Self-employment trading allowance / must-file trigger | income over £1,000 | [who must send a return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return) |
| MTD for Income Tax (sole traders, landlords) | qualifying income over £50,000 from 6 April 2026; over £30,000 from April 2027; over £20,000 from April 2028 | [gov.uk MTD eligibility](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax) |

## 6. Self Assessment dates, penalties, interest

Details in `deadlines-penalties-payments.md`. Late payment interest: Bank of England base rate + 4% from 6 April 2025 (7.75% from 9 January 2026); repayment interest base − 1%, minimum 0.5% (2.75%). Source: [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates). The rate moves with base rate: fetch it before quoting.

## 7. Announced changes after 2026-27 (not yet in the script)

Announced at Budget 2025 and reported by professional bodies (not yet confirmed on a GOV.UK rates page in this check): from 6 April 2027, savings income rates rise two points to 22 / 42 / 47%, and property income gets its own rates of 22 / 42 / 47% in England, Wales and NI. Allowance thresholds remain frozen. Confirm on GOV.UK before using for 2027-28.

## 8. Stale figures a model tends to produce

| Stale | Correct for these years |
|---|---|
| Employee NI 12% | 8% main rate, 2% above the upper earnings limit |
| CGT 10% / 20% on shares | 18% / 24% from 30 October 2024 |
| CGT exempt amount £12,300 or £6,000 | £3,000 |
| Dividend allowance £2,000 or £1,000; rates 7.5 / 32.5% | £500; 8.75 / 33.75% (to 2025-26), 10.75 / 35.75% (2026-27) |
| "Everyone over £100k / £150k must file" | the high-income PAYE trigger (£100k, then £150k for 2023-24) was removed from 2024-25; file only on the criteria in `do-i-need-to-file.md` |
| HICBC from £50,000 | £60,000 to £80,000 from 2024-25 |
| SA108 needed if proceeds over 4 x exempt amount (£12,000) | over £50,000 proceeds, or gains over the exempt amount, or a claim |
| Remittance basis, domicile, non-dom | abolished from 6 April 2025; residence-based FIG regime instead |
| Old OWR (3 years, keep pay offshore) | 4 years, qualifying new resident, election + claim, capped, no remittance condition |
| Residence guidance at RDRM | moved to the Residence and FIG Regime Manual (RFIG) |
| Class 2 voluntary NI from abroad | removed from 2026-27; Class 3 abroad needs 10 years' UK residence or 10 qualifying years |
