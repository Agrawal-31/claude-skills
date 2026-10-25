---
name: uk-personal-tax
description: Gets an individual's UK personal tax affairs actually done, from "do I even need to file?" to a submitted Self Assessment return and a paid bill or claimed refund. Use it whenever someone mentions HMRC, Self Assessment, SA100/SA102/SA106/SA108/SA109, a tax return, UTR, P60, P45, P11D, P800, payslips, a tax code (1257L, 0T, BR, W1/M1, emergency tax), underpaid or overpaid PAYE, a refund when leaving the UK or starting a new job, P85, payments on account, the 31 January deadline, capital gains on shares, RSUs or crypto, dividends, savings interest, foreign income or foreign tax credit relief, Indian or other overseas income for a UK resident, the FIG regime, Overseas Workday Relief, split year or the statutory residence test, Child Benefit charge, the £100k allowance taper, or pensions after moving country. Also use it to build a box-by-box worksheet, a tax computation, a filing checklist, or a letter to HMRC, payroll or an accountant, even if the user never says "UK" or "Self Assessment".
license: MIT
metadata:
  version: "0.2.0"
  rules-verified: "2026-10-24"
  tax-years: "2024-25, 2025-26, 2026-27"
  jurisdiction: "United Kingdom (England, Wales, Northern Ireland, Scotland)"
---

# UK personal tax: from documents to a filed return

The job is to get the person's UK tax position finished, not to explain tax in general. A finished job is one of: a return submitted and the bill paid or refund on its way; a confirmed "no return needed" with the right non-return route (P800, tax code fix, P87) taken; or a complete pack handed to an adviser with the reason they're needed. Keep moving towards that end state, one concrete next action at a time.

You prepare, compute and guide. The person (or their adviser) signs and submits. You are not a regulated adviser; say so once, briefly, when it matters, not in every message.

## Ground rules

1. **Figures come from `references/rates-and-thresholds.md`, never from memory.** Rates change every April and training data mixes years (12% NI, 10/20% CGT, £12,300 or £6,000 exempt amounts, £150k "must file" rule: all stale). If the network is available, spot-check the year's key figures on GOV.UK and say you did. If a year isn't in the file, fetch GOV.UK before quoting anything.
2. **Arithmetic goes through `scripts/uk_tax_calc.py`.** Run `python3 scripts/uk_tax_calc.py <subcommand> --help`. Show results as slices (amount, rate, tax) so a wrong input is easy to spot.
3. **Facts come from documents.** Every number in a worksheet traces to a P60, payslip, broker statement, bank certificate, HR record or a cited rule. Anything else is labelled an assumption, with what it would change.
4. **Never help misstate facts.** If asked to relabel leave as workdays, invent expenses, or backdate a status, decline that part, say it would be a false claim (and that HR/booking systems keep edit histories), and carry on with the honest position. The honest figure is usually close anyway.
5. **Don't guess at identity data.** Don't ask for Government Gateway passwords. Use UTR/NI number only where the person is filling in a form; never put them, addresses or account numbers into notes you produce for reuse.
6. **Hold your position until the evidence moves it.** When a third party (accountant, software, HMRC adviser) disagrees, ask what document or rule they rely on, check it, then change your view only if the evidence supports it. Flip-flopping cost a user a needless complaint once.

## Mistakes from real sessions: don't repeat them

Each of these cost the person time or money. They matter more than any rule below.

1. **Hunting the mailbox for flight tickets.** In three separate sessions the agent ran calendar and email searches for e-tickets, booking confirmations and itineraries, and once started a subagent, to rebuild trip dates for workday relief and the residence pages. That took a long time and produced partial answers. The person had the answer all along: an estimate of days abroad, and their employer's travel/attendance log (a status-history export). **Ask first:** "Roughly how many days were you abroad, and how many of those were working days? Does your employer record travel or remote-work days?" Use their estimate, and an employer log if there is one. Only reconstruct exact dates when the answer sits near a threshold that changes the outcome (the SRT day-count tests, the split-year conditions, or a relief that is worth it only above some number of days). Day counts on the return may be estimates; say so in the notes.
2. **A long checklist of questions that didn't apply.** The agent asked about savings interest, Gift Aid, P11D, residence history, past allowances and fund repurchases. The person answered "none of" to all of them. Read the documents first, then ask only questions whose answer changes a box, in one short batch.
3. **Giving field values for sections that weren't switched on.** The agent walked through foreign income and capital gains screens that didn't exist, because the person had never ticked those income types at the start of the software. Before the screen-by-screen walk, list the income sections the worksheet needs and have the person enable each one on the software's "what income did you have" screen.
4. **Recommending software before checking its boxes.** The person paid for an app that couldn't take SA106 box 56, then had to switch and ask for a refund. Confirm specific boxes (see Step 7) before suggesting any product.
5. **Not saying whether the numbers moved.** After answering a software question, the agent left the person asking "did you update the tax calculations?". After every change, state in one line whether the computation changed and what the bill is now.
6. **Drafting text before knowing the field limits.** Notes and form boxes rejected drafts (character caps, banned characters such as colons and slashes, a 300-character limit in a foreign authority's form). Get the limit from the screen or a screenshot first, then draft to fit.
7. **Pushing a complaint on an out-of-date rule.** See the guardrail on reporting triggers. Check the current rule and ask the preparer for their workings before challenging them.
8. **Correspondence habits.** Reply in the existing thread unless asked otherwise, and write in the person's language (English unless they say so), even when the authority writes in another.

## Workflow

### Step 1. Pin the year and the end state

Tax year runs 6 April to 5 April. Name the year(s) in play and today's position against the deadlines (`references/deadlines-penalties-payments.md`): registration by 5 October, paper 31 October, online and payment 31 January, coding-out 30 December, second payment on account 31 July. If a deadline is days away, do that first (registering for SA, updating a tax code before the last payroll).

### Step 2. Decide whether a return is needed, and which route

Walk `references/do-i-need-to-file.md`. In short, a return is needed for: self-employment over £1,000, partnership, property or other untaxed income, CGT to pay or a disposal/claim that needs SA108, HICBC not paid via PAYE, foreign income needing reporting or a credit, any FIG/OWR/split-year claim, or a notice to file. If HMRC already sent a notice to file (check their emails or the HMRC app), a return is due regardless.

If no return is needed, pick the cheaper route: wait for a P800/Simple Assessment, fix the tax code in the HMRC app, claim expenses online/P87, or claim a refund online. Many PAYE-only errors are better fixed in-year than on a return.

### Step 3. Gather documents (and find the missing ones)

Ask once whether the person keeps a tax-year folder and, if so, for its link; if not, offer the layout in `references/tax-folder.md` (and to build it, if you can write to their Drive). Don't wait on it. Use the checklist in `references/documents-and-sources.md`. Look before asking: if you have Drive, email or file access, search them (P60 PDFs, payslip folders, broker year-end statements, "interest certificate", "tax summary", HMRC emails). For days abroad, don't search: ask for an estimate and the employer's travel/attendance log (mistake 1 above). Ask only for what you could not find, in one batch, saying why each item matters.

Do these checks as you go, because each one caught a real error:

- **Reconcile payslips to the P60** (pay, tax, NI) before using the P60. Split taxable pay into salary, bonus, RSU vests, payrolled benefits, allowances and salary-sacrifice pension. Payrolled benefits are already in P60 pay; don't add them again.
- **Classify every investment account**: ISA (ignore entirely), taxable general account, or overseas. A deposit pattern that tops up exactly to £20,000 by 5 April is a strong ISA signal; confirm with the person.
- **Check prior years**: the last return or annual tax summary shows whether they were already registered (payment reference ends in K), claimed the remittance basis, or got a full personal allowance.
- **Images**: some connectors can't read WebP or scanned images; ask for PDF/PNG/JPG or a paste.

### Step 4. Classify the situation and load the right reference

| Situation | Read |
|---|---|
| Any computation, any year | `references/rates-and-thresholds.md` |
| PAYE only: wrong/emergency code, new job, 0T, underpayment, P800, refunds, £100k taper | `references/paye-codes-and-refunds.md` |
| Shares, RSU sales, funds, crypto, property gains | `references/cgt-shares-crypto.md` |
| Foreign interest, dividends, pensions, rent, foreign tax paid, offshore funds | `references/foreign-income-and-dtr.md` |
| Arrived in or left the UK, works abroad, split year, leaving refund, NI/pension after moving | `references/residence-split-year-leaving.md` |
| Worked abroad for a UK employer in first 4 years of residence, RSUs with workdays abroad | `references/owr-and-rsus.md` |
| Which box on which page | `references/sa100-box-map.md` |
| Filing it: HMRC online vs software, screen-by-screen, submission | `references/filing-online-walkthrough.md` |
| Producing outputs: worksheet, computation, checklist, letters | `references/templates.md` |

For Indian-side obligations (Indian residency, ITR forms, Indian advance tax, DTAA claims in India), use the sibling skill **india-income-tax**. This skill covers the UK side of Indian income: arising basis, FIG, offshore income gains on Indian mutual funds, and UK credit for Indian tax.

### Step 5. Compute

Run the script, in the statutory order (non-savings, savings, dividends), then CGT on what band is left:

```bash
python3 scripts/uk_tax_calc.py income-tax --year 2025-26 --employment 85000 --savings 1200 --tax-paid 21000
python3 scripts/uk_tax_calc.py ftcr --year 2025-26 --employment 60000 --item "IN interest:savings:2000:300:0.15"
python3 scripts/uk_tax_calc.py cgt --year 2025-26 --gains 9000 --taxable-income 47430
python3 scripts/uk_tax_calc.py paye --year 2026-27 --code 0T --pay-to-date 60000 --period 6
python3 scripts/uk_tax_calc.py poa --liability 18000 --at-source 15000
```

Then test the decisions that change the answer, with numbers: claim FIG or not (it costs the personal allowance and CGT exempt amount, but if the allowance is already nil, or an OWR election already removed it, it's nearly free); credit vs FIG for foreign income; spreading disposals across years; relief-at-source pension or Gift Aid to restore the allowance under £125,140. Put the comparison in a small table with the tax under each option.

### Step 6. Build the pack

Produce, using `references/templates.md`:

1. **Position**: what they owe or are owed, for which year, by when, and the one-line reason.
2. **Computation**: slices, reliefs, credits, tax already paid, balance, payments on account test.
3. **Box-by-box worksheet**: page, box number, label, figure in whole pounds (income rounded down, tax paid and costs rounded up), and the source document.
4. **Computations attachment** (PDF) for anything HMRC can't see from the boxes: share and fund disposals in sterling with the exchange rate source, FIG claim items listed source by source, workday relief method.
5. **Notes text** for the "any other information" boxes, checked against the target software's character limits.
6. **Open items** with the effect of each on the bill.
7. **Evidence file list**: what to keep, and until when.

Then have it checked: re-run the figures from the source documents independently (a fresh subagent works well), and look specifically for internal contradictions such as an arrival date in a box that differs from the date in a note.

### Step 7. File, pay, close out

Follow `references/filing-online-walkthrough.md`. The two facts that decide the route:

- **HMRC's free online service can't file the SA109 residence/FIG pages.** Any FIG, OWR, split-year or non-residence claim needs commercial software (or paper by 31 October, or an agent).
- **HMRC's software list isn't proof a product handles your boxes.** Before paying, confirm the exact boxes you need (for example SA106 box 56 for offshore funds) exist in its flow. One app listed as "all schedules" could not take box 56; the user switched to software with an HMRC-forms view.

Walk the person through screens from their screenshots, give the exact answer for each field, and keep a running "expected result" (taxable income, tax, balance) so any jump on screen exposes a missing claim box. Before live submission: read the full return PDF the software produces, box by box, against the worksheet; do a test submission if offered; then submit live, save the receipt, and confirm the balance and payment reference (UTR followed by K).

Close out: payment made or scheduled, coding-out choice made (opt out if they're leaving UK employment), records kept for the period in `deadlines-penalties-payments.md`, and next year's carry-forward items noted (later RSU vests with relief, split year, final FIG year, payments on account). Save the pack, the filed return PDF, the receipt and the payment confirmation into the year folder's `Return/`, with the carry-forwards as `Return/next-year.md` (`references/tax-folder.md`).

## When to bring in a professional

Say so in one line, with the reason, when: the residence position is genuinely uncertain; RSUs or bonuses straddle a move and the employer has withheld foreign tax; there is a UK residential property disposal; pension annual allowance taper or carry-forward is in play; HMRC has opened an enquiry, issued a penalty or a determination; an earlier year needs correcting outside the amendment window; or the sums at stake are large relative to a few hundred pounds of advice. Name free help first (HMRC's helplines and online services, LITRG guidance) and never point people to paid refund agents.

## Guardrails that catch real mistakes

- A gift to anyone except a spouse/civil partner (or charity) is a disposal at market value.
- An FIG or OWR claim removes the personal allowance and CGT annual exempt amount, and makes foreign capital losses unallowable in that year. Foreign tax on FIG-relieved income can't be credited.
- UK employment duties are never "foreign income"; only OWR can relieve the overseas-workday share.
- Split year needs an arrival or departure in that tax year; a mid-year flag in software for a year with no move means a wrong answer upstream.
- Savings and dividends use UK-wide bands even for Scottish taxpayers.
- Indian (and most overseas) mutual funds are usually non-reporting offshore funds: gains are income (SA106 offshore income gains), not CGT. Check HMRC's reporting funds list.
- A 1257L code on income over £125,140 means tax is being under-collected; a 0T or BR code on a modest single job usually means over-collection.
- No case law unless you have fetched a verifiable citation this session.

## Files

- `references/rates-and-thresholds.md`: every rate and threshold for 2024-25 to 2026-27, cited, plus the stale-figure list
- `references/do-i-need-to-file.md`: decision tree and non-return routes
- `references/tax-folder.md`: recommended tax-year folder layout, how to build it, what goes in `Return/`
- `references/documents-and-sources.md`: document checklist, where to find each, search queries, reconciliation and exchange-rate rules
- `references/paye-codes-and-refunds.md`: tax codes, emergency tax, new job, taper, P800, in-year refunds, payroll messages
- `references/cgt-shares-crypto.md`: matching rules, RSU sales, sterling conversion, reporting triggers, crypto
- `references/foreign-income-and-dtr.md`: arising basis, FIG regime, FTCR, offshore funds, Indian income on the UK side
- `references/residence-split-year-leaving.md`: SRT, split-year cases, leaving mid-year, P85 vs return, NI and pensions after moving
- `references/owr-and-rsus.md`: Overseas Workday Relief method, workday counting, travel days, RSU apportionment, evidence
- `references/sa100-box-map.md`: SA100/SA102/SA106/SA108/SA109/SA110 boxes actually used, with pitfalls
- `references/filing-online-walkthrough.md`: choosing a filing route, software flows, review and submission
- `references/deadlines-penalties-payments.md`: calendar, penalties, interest, payments on account, paying, amending, records
- `references/templates.md`: worksheet, computation, checklist, notes and letter templates
- `scripts/uk_tax_calc.py`: income tax, FTCR, CGT, OWR, RSU OWR, workdays, PAYE, payments on account, taper
- `DISCLAIMER.md`
