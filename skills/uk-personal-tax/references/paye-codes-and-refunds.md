# PAYE, tax codes, underpayments and refunds

## Contents
1. Reading a tax code
2. Common problems and fixes
3. The £100k taper and high earners on 1257L
4. New job and emergency tax
5. Fixing a code in-year
6. Refund routes and timing
7. Messages to payroll and HMRC

## 1. Reading a tax code

| Code | Meaning | Annual tax-free pay (approx.) |
|---|---|---|
| 1257L | standard personal allowance | £12,579 (code × 10 + 9) |
| 1257L W1 / M1 / X | emergency, non-cumulative: each pay period taxed on its own | 1/52 or 1/12 of the allowance each period, no catch-up |
| 0T | no allowance; all pay taxed through the bands | £0 |
| BR / D0 / D1 | all pay at 20% / 40% / 45% (usually a second job) | £0 |
| K codes | negative allowance (benefits or debts exceed allowance) | adds to taxable pay |
| S or C prefix | Scottish or Welsh taxpayer | Scottish bands for S |
| NT | no tax deducted | |

Cumulative codes (no W1/M1) look at pay and tax for the whole year to date, so a corrected code refunds earlier over-deduction in the next payslip. Source for emergency codes: [gov.uk/tax-codes/emergency-tax-codes](https://www.gov.uk/tax-codes/emergency-tax-codes). Size any over- or under-deduction with:

```bash
python3 scripts/uk_tax_calc.py paye --year 2026-27 --code 1257L --pay-to-date 45000 --period 6 --tax-paid 9800
```

## 2. Common problems and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Income over £125,140 on 1257L all year | allowance tapered to nil but payroll gave it | Expect an underpayment of about 45% × £12,570 (≈ £5,657). File if in SA; otherwise P800 will follow. Update the estimate in the HMRC app so the current year is right |
| 0T on a modest single job | HMRC has no allowance record for this job, or estimated income too high | Update the income estimate; the code moves to 1257L and the next payslip refunds the year-to-date excess |
| BR on main job | second job treatment applied to the wrong job | Tell HMRC which job is main |
| Two jobs, allowance on the smaller one | allocation wrong | Ask HMRC to move the allowance |
| Benefit in kind added twice | benefit payrolled and also coded | Ask HMRC to remove it from the code |
| P800 says underpaid but you're in SA | P800 and the return overlap | The return figure wins; tell HMRC |
| Bonus month pushes you over £100k | taper hits in the bonus month | Normal; marginal rate 60% (rUK) or 67.5% (Scotland). Consider pension contribution before year end |

## 3. The £100k taper and high earners on 1257L

Adjusted net income between £100,000 and £125,140 loses £1 of allowance per £2. Payroll doesn't know your total income (bonus, RSUs, other jobs, interest), so it keeps the full code and under-collects. Check:

```bash
python3 scripts/uk_tax_calc.py taper --year 2025-26 --adjusted-net-income 112000
python3 scripts/uk_tax_calc.py income-tax --year 2025-26 --employment 112000 --tax-paid 32000
```

Levers before 5 April: relief-at-source or personal pension contributions (grossed up, they reduce adjusted net income), salary sacrifice into pension (reduces pay), Gift Aid. Show the person the saving in pounds for a given contribution; restoring £1 of allowance in this band saves 60p (rUK).

RSU vests are taxed through payroll at the marginal rate, often appearing as 45% plus NI. Large "effective" rates on a bonus or vest month are usually the taper plus NI, not an error.

## 4. New job and emergency tax

- Starting a job without a P45: the employer uses the starter checklist and often 1257L M1/W1. HMRC usually issues the right code within 35 days.
- With a P45: give it to the new employer straight away; it carries cumulative pay and tax.
- Two jobs in a year: the second employer may put you on BR or 0T until HMRC splits the allowance.
- Emergency code refunds normally arrive automatically through payroll once the correct cumulative code is applied; otherwise at year end via P800, or claim online if you've stopped working.
- Moving employer within a group or relocating into the UK mid-year: first UK payslip may use a non-cumulative code; check the code on each payslip and on the HMRC app.

## 5. Fixing a code in-year

The taxpayer, not the employer, controls the code. In the HMRC app or Personal Tax Account, open the employment and update the estimated income for the year. HMRC recalculates and sends the code to the employer electronically, usually within days; payroll applies it from the next run that the notice reaches before cut-off. A plain code (no W1/M1) catches up the whole year in one payslip.

Worked pattern (leaving the UK mid-year): someone on 0T because HMRC estimated a full year of high pay is leaving at month 7 with UK-part pay under £100,000. Updating the estimate to the actual UK-part total moved the code to 1257L; the final payslip refunded about seven months of allowance at the marginal rate. The remainder of the overpayment (PAYE spreads bands monthly, so a short year over-taxes) comes back only on the return. Accuracy matters: underestimating to get cash early only moves money between payslip and return.

After updating, check the next payslip shows the new code and the expected change in tax. If it still shows the old code, the notice missed the cut-off; nothing is lost.

## 6. Refund routes and timing

| Situation | Route |
|---|---|
| In SA | Refund on the return: claim to a UK bank account; online returns typically repay within weeks of filing; file from 6 April for a refund |
| Not in SA, still employed | Corrected code refunds through payroll; else P800 after year end |
| Stopped work, not starting again | Online claim (P50) |
| Leaving the UK, not in SA | P85 (include P45 parts 2 and 3) |
| Expenses | Online/P87 if not in SA; on the return if in SA |
| Earlier years | Overpayment relief up to 4 years after the end of the tax year |

Use HMRC's free routes ([gov.uk/claim-tax-refund](https://www.gov.uk/claim-tax-refund)). Repayment agents take a cut and assignment forms divert the refund to them.

## 7. Messages to payroll and HMRC

Templates in `templates.md`: "updated tax code, please apply to this payroll", "query about my tax code", "please explain this deduction". Payroll case tips: attach the HMRC code notice or app screenshot, pick a "tax code / PAYE" category, ask them to confirm receipt of the HMRC notice and which pay run it will hit.
