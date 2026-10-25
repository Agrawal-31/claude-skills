# Do I need to file? Decision tree and routes

Source for the core criteria: [Who must send a tax return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return) (checked October 2026). HMRC's own checker: [gov.uk/check-if-you-need-tax-return](https://www.gov.uk/check-if-you-need-tax-return). When in doubt, run the checker with the person and screenshot the result.

## Decision tree

Work top to bottom. The first "yes" settles it.

1. **Has HMRC sent a notice to file for the year?** (Letter, email "you need to complete a tax return", or the return showing as due in the HMRC account.) → File by the deadline on the notice, even if nothing is owed. If you think it was sent in error, ask HMRC to withdraw it before 31 January rather than ignoring it; otherwise penalties start.
2. **Self-employed with gross income over £1,000, or a partner in a partnership?** → File.
3. **Capital gains tax to pay, or a disposal that needs SA108?** (Proceeds over £50,000, gains over the £3,000 exempt amount, or a claim such as losses or FIG.) → File, or use the real-time CGT service if eligible and nothing else needs a return. UK residential property: 60-day return regardless.
4. **High Income Child Benefit Charge** (adjusted net income over £60,000, either partner) and not paying it through PAYE? → File, or opt into PAYE collection if this is the only reason.
5. **Any claim that lives only on a return?** FIG regime, Overseas Workday Relief, split-year treatment, non-residence, foreign tax credit relief that can't be given through the tax code. → File (and see `filing-online-walkthrough.md`: these need commercial software).
6. **Untaxed income HMRC doesn't know about?** Property income (over the £1,000 property allowance), foreign income, tips/commission, casual income, large interest or dividends. HMRC's practice: property/other untaxed income over £2,500, or savings/investment income over £10,000, normally means a return; smaller amounts can often be coded out or reported by phone/online. (Thresholds from HMRC's checker practice, not the "who must send" page: confirm with the checker.) → File or tell HMRC.
7. **Off-payroll worker repaying a student loan?** → File.
8. **Want to claim something not possible otherwise?** Higher-rate relief on relief-at-source pension contributions or Gift Aid can also be claimed by phone/letter or via tax code; employment expenses over the online limit; losses. → Return optional but often easiest.
9. **None of the above, PAYE only.** → No return. Fix errors through the tax code or a refund claim (below).

Stale rules to ignore: "income over £100,000/£150,000 means a return" (removed from 2024-25); "being a company director always needs a return" (it isn't on HMRC's current list; what matters is whether a notice to file was issued, so check the notice).

## Already registered?

Registration by **5 October** after the tax year applies only if you've never filed or didn't file last year. Signs you're already registered: a UTR on HMRC letters, an SA payment reference ending in K (UTR + K), HMRC emails about "your 2025 to 2026 tax return", an annual tax summary showing Self Assessment. Searching the person's email for "Self Assessment", "UTR", "Unique Taxpayer Reference" from hmrc.gov.uk settles it quickly.

If registering late, HMRC sets a deadline three months from the notice date and a late-filing penalty doesn't apply while that window is open.

## Non-return routes

| Problem | Route | Notes |
|---|---|---|
| Underpaid PAYE after year end | P800 from HMRC (usually June to November), collected through next year's code if under £3,000 and you stay in PAYE, else direct payment | Don't wait if leaving the UK: pay or file instead |
| Simple Assessment (PA302) | HMRC issues a bill for e.g. State Pension over the allowance, untaxed interest | Pay by 31 January; query within 60 days if wrong |
| Wrong code this year (wrong estimated income, benefits, second job split) | Update income estimate in the HMRC app or Personal Tax Account | Changes the code in days; cumulative codes refund the year-to-date overpayment in the next payslip |
| Emergency code at a new job | Give the employer your P45 or complete the starter checklist; HMRC usually fixes within 35 days | See `paye-codes-and-refunds.md` |
| Overpaid PAYE after leaving a job mid-year with no new job | Claim online (form P50) or wait for year-end | |
| Leaving the UK, not in Self Assessment | P85 | If you'll file a return for the leaving year anyway (split year, FIG, RSU income), don't use P85: the refund comes via the return |
| Employment expenses | Online claim or P87; if you file a return, claim on the return instead | Commuting to a permanent workplace is never deductible |
| Higher-rate pension or Gift Aid relief | Phone/letter or via tax code | |
| Old years | Overpayment relief up to 4 years after the tax year end | |

## Output

State the answer as: "For [year] you [do / don't] need a return because [criterion]. Next action: [one action] by [date]." If a return is not needed, still list what would make one needed (a disposal, a move, Child Benefit) so the person can recheck.
