# Deadlines, penalties, payments, amendments and records

Sources: [deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines), [penalties](https://www.gov.uk/self-assessment-tax-returns/penalties), [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account), [interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates), [corrections](https://www.gov.uk/self-assessment-tax-returns/corrections), [records](https://www.gov.uk/keeping-your-pay-tax-records/how-long-to-keep-your-records). Checked October 2026.

## Calendar (for tax year ending 5 April Y)

| Date | What |
|---|---|
| 6 April Y | Return can be filed (file early for a refund) |
| 31 July Y | Second payment on account for year Y-1 (if any) |
| 5 October Y | Register for SA if a return is needed and you didn't file last year |
| 31 October Y | Paper return deadline |
| 30 December Y | Online return deadline if you want a balance (under £3,000, PAYE employee) collected through your tax code |
| 31 January Y+1 | Online return; pay balancing payment and first payment on account for year Y+1 |
| 31 January Y+2 | Last day to amend the return; last day for FIG claims |
| 5 April Y+4 | Overpayment relief claims for year Y |

Example: 2025-26 return: register by 5 October 2026, paper by 31 October 2026, online and pay by 31 January 2027, amend by 31 January 2028.

## Penalties

Late filing: £100 immediately (even if no tax is due); after 3 months £10 a day up to £900; after 6 months the greater of 5% of tax due or £300; after 12 months another 5% or £300. Late payment: 5% of unpaid tax at 30 days, 6 months and 12 months. Interest on late payments at base rate + 4% (7.75% from 9 January 2026; fetch the current rate). Reasonable excuse appeals are possible; mistakes in the return are penalised separately under inaccuracy rules (careless errors up to 30%, reduced to nil for unprompted disclosure).

## Payments on account

Due unless last year's SA balance (liability less tax deducted at source) was under £1,000, or more than 80% of the liability was deducted at source. Each is half of last year's SA balance, due 31 January and 31 July. Reduce online or with SA303 if this year's income will be lower (interest if reduced too far). Leaving UK employment or the UK often justifies reducing them. Compute:

```bash
python3 scripts/uk_tax_calc.py poa --liability 20000 --at-source 12000
```

## Paying

Reference: UTR + K. Methods: online/app, bank transfer, Direct Debit, card (personal debit), budget payment plan. Bank details on [gov.uk/pay-self-assessment-tax-bill](https://www.gov.uk/pay-self-assessment-tax-bill). Coding out: only for balances under £3,000 (HMRC's long-standing limit; the deadlines page doesn't state it, so confirm) with PAYE income next year and the online return filed by 30 December; opt out on page TR 6 if you'd rather pay or won't have a UK employer.

## Amending and correcting

Amend online within 12 months of the 31 January deadline (wait 72 hours after filing; Self Assessment account > tax return options). Paper amendments: mark "amendment" with name and UTR. After that: overpayment relief by letter up to 4 years after the tax year, with the prescribed statement and declaration. Underpaid earlier years: tell HMRC promptly (unprompted disclosure reduces penalties).

## Enquiries and records

HMRC can normally open an enquiry within 12 months of the date an on-time return was filed (longer for late or amended returns, and discovery assessments can reach back further for careless or deliberate errors; confirm with HMRC guidance for a specific case). Keep records at least 22 months after the end of the tax year (15 months after filing if late); self-employed and landlords longer (5 years after the 31 January deadline). Keep OWR and RSU workings for as long as later returns rely on them.
