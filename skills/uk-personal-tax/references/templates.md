# Output templates

Fill these with the person's figures; keep personal identifiers (UTR, NI number, addresses, account numbers) out of anything that will be shared beyond the person and HMRC.

## Contents
1. Filing pack outline
2. Computation
3. Box-by-box worksheet
4. Computations attachment (PDF)
5. Filing checklist
6. Letters and messages

## 1. Filing pack outline

```
# Self Assessment [year]: filing pack
Prepared [date]. Status: [draft / ready to file / filed on DATE, receipt REF]

## Summary
You [owe £X / are owed £X] for [year], due [date]. Main reason: [one line].
Payments on account: [none / £X on 31 Jan and 31 Jul], because [test].

## Computation            (section 2)
## Main return answers    (TR 2 page questions)
## Employment (SA102)     (worksheet rows)
## Foreign (SA106)
## Capital gains (SA108)
## Residence and FIG (SA109)
## Notes text             (exact text for each notes box, character-checked)
## How to file            (route, software, steps, test then live)
## Still needed           (each item with its effect on the bill)
## Evidence to keep       (list, keep until DATE)
## Reconciliation and sources (payslips vs P60, source register)
## Later years            (carry-forward items)
```

## 2. Computation

```
Income tax [year], [England, Wales and NI / Scotland]
                                                 £
Employment income (SA102 box 1)            xxx,xxx
Less overseas workday relief (SA109 box 49) (x,xxx)
Foreign income (relieved under FIG)          [listed, nil taxable]
Other income                                   x,xxx
Total income                               xxx,xxx
Less personal allowance (reason)             (x,xxx)
Taxable income                             xxx,xxx

  £37,700 at 20%                              7,540
  £x at 40%                                   x,xxx
  £x at 45%                                   x,xxx
  Savings / dividend slices                    x,xxx
Income tax                                    xx,xxx
Less foreign tax credit relief                (x,xxx)
Capital gains tax                              x,xxx
Total liability                               xx,xxx
Less tax deducted (PAYE, other)              (xx,xxx)
Balance to pay / (repay)                       x,xxx
Payments on account test: [balance < £1,000 or >80% at source] → [none / 2 × £x]
```

Add a decision table when an option changes the answer:

| Option | Tax | Notes |
|---|---|---|
| No claim, credit relief | £x | keeps allowance and CGT exempt amount |
| FIG claim on foreign items | £x | loses allowance (already nil?), foreign losses unusable |

## 3. Box-by-box worksheet

| Page | Box | Label | Enter | Exact figure | Source |
|---|---|---|---|---|---|
| SA102 | 1 | Pay from this employment | 85,000 | 85,000.40 | P60 |
| SA102 | 2 | UK tax taken off | 21,001 | 21,000.60 | P60 |
| SA106 | 4 / 4.1 | Overseas interest / FIG amount | 120 / 120 | 120.55 | bank certificate, HMRC average rate |
| SA109 | 28 | FIG claim on foreign income | X | | eligibility: arrival date, 10+ years non-resident |

Rounding: income and gains down; tax deducted and costs up.

## 4. Computations attachment (PDF)

Title, tax year, "attachment to SA108/SA106", no more personal data than HMRC needs (name and UTR are normal on an attachment HMRC receives). Sections:

- A. Listed shares: table of each disposal (date acquired, date sold, quantity, proceeds in currency, rate and source, proceeds £, cost £, gain/loss £); share identification statement (same-day/30-day/pool; "no acquisitions within 30 days after any sale"); RSU base cost explanation; SA108 entries; FIG statement if claimed.
- B. Offshore funds: per fund, ISIN, lots, dates, rates, sterling proceeds/cost/gain; statement that none is a UK reporting fund (checked against HMRC's list on DATE); SA106 box 56/56.1.
- C. Foreign interest and dividends: per source, currency amount, rate used, sterling, foreign tax.
- D. FIG claims by item: each item and amount with its box.
- E. FTCR workings (if credit claimed): per item, foreign tax, treaty limit, UK tax, credit.

Keep it under the software's size limit. State only what the documents show; remove claims you can't evidence.

## 5. Filing checklist

- [ ] Year and route confirmed (HMRC online / software / paper / agent)
- [ ] Registered for SA (UTR) or registration done by 5 October
- [ ] Payslips reconcile to P60; P11D/payrolled benefits handled
- [ ] Every account classified (ISA / taxable / overseas)
- [ ] All disposals listed and converted to sterling; 30-day check done
- [ ] Foreign income listed by source; FIG vs credit decided with numbers
- [ ] Residence position and dates confirmed; box and note dates match
- [ ] Workdays, leave and travel days counted (if OWR)
- [ ] Computation run through the script; independent re-check done
- [ ] Worksheet complete in whole pounds; notes text fits the software
- [ ] Attachment built and under size limit
- [ ] Software supports every box needed (checked before buying)
- [ ] Final return PDF reviewed box by box; SA302 matches
- [ ] Test submission passed; live submission receipt saved
- [ ] Payment made (UTR + K) or scheduled; coding-out choice made
- [ ] Records filed; carry-forward items diarised

## 6. Letters and messages

**To payroll: apply an updated tax code**

> Subject: Updated HMRC tax code to apply from [month] payroll
>
> Hello, on [date] I updated my estimated income with HMRC for [year]. HMRC is issuing a revised tax code notice to [employer], expected to change my code from [old] to [new] on a cumulative basis. [My [month] pay will be my final UK payroll as I am relocating abroad.] Please confirm when the notice is received, apply it to the [month] payroll before my final payslip [and P45], and tell me if it arrives after the cut-off. Thank you. [Name, employee number]

**To HMRC: query a tax code or P800**

> I'm writing about my [year] tax code [code] / calculation dated [date]. My employment income for the year is [£x] from [employer] and I have [no other income / other income of £x]. The code [gives / doesn't give] a personal allowance of [£x], which appears wrong because [reason]. Please review and issue a corrected code. [NI number on the letter only.]

**To HMRC: overpayment relief (after the amendment window)**

> I am claiming overpayment relief under Schedule 1AB TMA 1970 for the tax year [year]. I believe I overpaid £[x] because [reason]. [I have / have not] previously appealed against this. I declare that the particulars given are correct and complete to the best of my information and belief. [Signature, name, UTR, date]

**To an accountant: query an omission**

> Thanks for the return. Could you confirm where [item] was reported, or why it wasn't needed? My understanding is that SA108 is required where proceeds exceed £50,000, gains exceed the annual exempt amount or a claim is made; my proceeds were £[x] and gains £[x]. Could you share the computation you hold? If no pages were required, a short note in the additional information box would be fine.

**To software support: missing box**

> My return needs [form] box [n] ([label]) of £[x], with £[x] claimed in box [n.1] under the FIG regime. I can't find this in the flow (the section only offers [options]). Where should it be entered, or can you add it? If it isn't supported, please confirm so I can file elsewhere and refund my fee; please don't submit anything from my account.

**To HMRC: leaving the UK (if not using a return)**

Use form P85 online; attach P45 parts 2 and 3. If filing a return for the leaving year, don't send P85: complete SA109 split-year boxes instead.
