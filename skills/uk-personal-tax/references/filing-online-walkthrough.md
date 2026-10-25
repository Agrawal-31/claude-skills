# Filing: choosing the route and getting through the screens

## Contents
1. Choose the route
2. Before you start
3. Working through a software flow
4. Review before submitting
5. Submit, then close out
6. Problems seen in practice

## 1. Choose the route

| Route | Use when | Limits |
|---|---|---|
| HMRC online (free) | Employment, UK income, most foreign income, most CGT | Can't file SA109 (residence, split year, FIG, OWR); some special cases excluded |
| Commercial software | Anything with SA109, or you want box-level control and attachments | Paid; check it supports your exact boxes |
| Paper | Fallback | Due 31 October; slower; HMRC calculates |
| Agent/accountant | Uncertain positions, enquiries, or you want someone else to sign off | Fees; you're still responsible for accuracy |

Picking software:
1. Start from HMRC's [list of commercial software suppliers](https://www.gov.uk/government/publications/self-assessment-commercial-software-suppliers/self-assessment-online-commercial-software-suppliers): check "schedules supported" includes every page you need and that attachments are supported.
2. Then confirm the specific boxes you need are in its flow, especially less common ones: SA106 box 56 (offshore funds), SA109 boxes 28/29/40-49, SA108 26.1. A listing of "all schedules" didn't guarantee box 56 in one consumer app; its support confirmed it was missing and offered a paid manual filing instead. Ask support before paying, or pick software with an "HMRC forms" view that shows every box.
3. Software that showed HMRC's own pages (an SA-forms mode alongside a question mode) handled a complex FIG/OWR return well at modest cost.

## 2. Before you start

- UTR, NI number, the box-by-box worksheet, notes text, and the computations PDF (keep it small; one product limited attachments to 5 MB).
- Government Gateway user ID and password. If the person signs in to HMRC with GOV.UK One Login, they need to create a separate Government Gateway user ID to connect commercial software ([GOV.UK guidance](https://www.gov.uk/guidance/check-how-to-submit-a-self-assessment-tax-return-using-commercial-software)).
- The expected result: taxable income, tax, tax deducted, balance. Every screen change is checked against it.

## 3. Working through a software flow

Have the person send screenshots; answer each field explicitly (value, or "leave blank", or "untick"). Patterns:

- **Question mode first, forms mode to check.** Use the question flow to switch on pages, then view the HMRC forms to confirm boxes. In one product, switching the CGT pages to "forms mode" stopped its per-disposal computation: use "view" instead.
- **Residence questions**: for a full-year resident, answer the automatic overseas tests "no", 183 days "yes", second residence "no". If the summary then says "eligible for split year", find the wrong answer.
- **Day counts may need integers**: enter whole days rounded down; the pound figures carry the exact relief.
- **Software may calculate relief itself** from inputs it can't see properly (e.g. OWR from a day count): override with the computed amount.
- **Defaults to untick**: FTCR ticked by default on foreign interest rows when FIG is claimed; "additional expenditure" rows on disposals; "work abroad" pages when OWR is on SA109.
- **Where foreign items live**: some apps put foreign income under "investments"; offshore fund gains sit under "other foreign income including disposals of holdings in offshore funds", not under "other UK income" and not under capital gains "other assets".
- **Validation warnings are often sequencing**: e.g. "qualifying employment income exceeds employment income" clears once the employment page is filled.
- **FIG on each disposal**: tick the FIG/foreign-asset option on every foreign disposal (losses included), then enter the FIG relief on the gain.
- **Watch the running total.** If the tax figure jumps by roughly (relieved amount × marginal rate), a FIG ".1" box or relief is missing.
- **Informational messages** (e.g. "reduced personal allowance", Child Benefit reminders) can be ignored when they match the facts.
- **Tax office fields** on the front page (issue date, office address) can usually be left at defaults for online filing.

## 4. Review before submitting

Print the full return PDF from the software and check every page against the worksheet: page TR 2 answers, each box, notes text (dates match boxes, no run-on sentences after character stripping), attachment present, SA302/SA110 matches the computation. Common catches: arrival date in a box differing from the note; postcode typos; a losses box filled when it should be nil; a ".1" FIG box blank.

## 5. Submit, then close out

1. Test submission if the software offers it; it validates with HMRC without filing. A success log looks the same for test and live: confirm which you did.
2. Live submission; save the HMRC receipt (submission reference, date/time) and the final PDF; lock the return in the software.
3. Check the HMRC account shows the return within a day or two and the balance matches.
4. Pay: reference is the UTR followed by K. Bank details and methods: [gov.uk/pay-self-assessment-tax-bill](https://www.gov.uk/pay-self-assessment-tax-bill) (check the page before paying; don't rely on copied account numbers).
5. If you bought software you no longer need, or a product couldn't handle the return, ask for a refund and confirm in writing that nothing will be submitted from that account.
6. Diary: 31 July second payment on account (if any), next 5 April, and the carry-forward items.

## 6. Problems seen in practice

| Problem | Fix |
|---|---|
| Free HMRC service won't take SA109 | Commercial software or paper by 31 October |
| App lacks a box you need | Ask support; if missing, switch product; don't force the item into another box |
| Accountant omitted something you expected | Check the current rule, ask for their workings; small gains under the exempt amount with proceeds under £50,000 need no SA108 |
| Two different arrival dates in records | Use the day you actually arrived to live/work; make box and note match |
| Return filed with an error | Amend online within 12 months of the 31 January deadline (wait 72 hours after filing) |
