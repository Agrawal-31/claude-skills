# Foreign income, the FIG regime and double taxation relief

For the Indian side (Indian residential status, ITR forms, Indian tax rates, DTAA claims in India, Form 10F/TRC), use the sibling skill **india-income-tax**. This file is the UK side.

## Contents
1. The default: arising basis
2. The FIG regime (from 2025-26)
3. Credit or FIG? Decide with numbers
4. Foreign tax credit relief mechanics
5. Offshore funds
6. Indian income on the UK return
7. Foreign pensions and social security
8. Where it goes on the return

## 1. The default: arising basis

A UK resident is taxed on worldwide income and gains as they arise, whether or not the money comes to the UK. The remittance basis and domicile were abolished from 6 April 2025. Foreign income is converted to sterling (`documents-and-sources.md` section 4) and reported on SA106, with credit for foreign tax under the treaty.

Small foreign interest can sometimes go in the UK interest box as a shortcut on some software; don't do this if you're claiming FIG or a tax credit, because the FIG and credit boxes exist only on SA106.

## 2. The FIG regime (from 2025-26)

Sources: [HS266](https://www.gov.uk/government/publications/foreign-income-and-gains-fig-regime-self-assessment-helpsheet-hs266/hs266-foreign-income-and-gains-fig-regime-2026), [RFIG43000](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig43000), [RFIG45100](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig45100).

- **Who**: a "qualifying new resident": UK resident for the year after at least 10 consecutive tax years of non-UK residence. Available for up to 4 consecutive tax years starting with the year of becoming UK resident. Split years and treaty-non-resident years count as years of UK residence in the four; someone who arrived in, say, February 2024 has 2023-24 (year 1, split year) to 2026-27 (year 4), so FIG is available for 2025-26 and 2026-27 only.
- **What it relieves**: foreign income (interest, dividends, rent, pensions, offshore income gains: RFIG45100 includes them) and foreign gains (e.g. sale of foreign shares). Not UK employment income; the overseas-workday share of employment income is relieved through OWR instead (`owr-and-rsus.md`).
- **Claim**: annual, on the return. SA109 box 28 (income), box 29 (gains); then report each item on SA106 or SA108 and enter the relieved amount in the ".1" boxes (SA106 4.1 interest, 6.1 dividends, 9.1 pensions, 56.1 offshore funds; SA108 26.1). Each source must be identified and quantified. Deadline: 12 months after the 31 January filing date.
- **Cost of claiming** (RFIG43000): lose the personal allowance, blind person's allowance, married couple's allowance, marriage allowance and the CGT annual exempt amount for the year; foreign capital losses in the year cease to be allowable; foreign trading/property losses lost. FIG-relieved income still counts in adjusted net income (HICBC, taper). No foreign tax credit on relieved income.
- **Practical rule**: worth it when the allowance is already gone (adjusted net income over £125,140) or already lost through an OWR election, or foreign income/gains are large. Once you've made any FIG or OWR claim for the year, claiming on every foreign item is free, so claim on all of them (including a small foreign share gain that would otherwise be taxed with no exempt amount).
- HMRC's free online return can't take SA109: use commercial software (`filing-online-walkthrough.md`).

## 3. Credit or FIG? Decide with numbers

Run both and show a table:

```bash
# A: no claim, credit relief
python3 scripts/uk_tax_calc.py ftcr --year 2025-26 --employment 90000 \
  --item "foreign dividends:dividends:4000:600:0.15" --item "foreign interest:savings:3000:450:0.15"
# B: FIG claim (no allowance), foreign items left out
python3 scripts/uk_tax_calc.py income-tax --year 2025-26 --employment 90000 --fig-claim
```

Compare UK tax A (after credit) with B. Also count the lost CGT exempt amount and any foreign losses. For incomes under £100,000 with modest foreign income, B usually loses.

## 4. Foreign tax credit relief mechanics

Source: [HS263 (2026)](https://www.gov.uk/government/publications/calculating-foreign-tax-credit-relief-on-income-hs263-self-assessment-helpsheet/relief-for-foreign-tax-paid-2026-hs263).

- Credit = lower of (foreign tax, limited to the treaty rate) and (UK tax on that item). Calculated item by item, not pooled.
- Tax above the treaty rate isn't creditable; reclaim it from the foreign tax authority (e.g. by giving the foreign bank a tax residence certificate and treaty form).
- Ordering: set allowances first against income with no foreign tax; treat the item with the highest foreign rate as the top slice. The `ftcr` subcommand takes items in the order given; list the highest-rate item first and test the alternative order.
- Only tax (and surcharges/cess that are part of the tax) is creditable; foreign interest and late-filing fees are not.
- Alternative: deduction relief (foreign tax reduces the taxable amount). Better only if there's no UK liability.
- Credit is entered on SA106 (column for foreign tax and the FTCR claim); HMRC calculates it if you don't.
- Split the foreign tax by income type and then by source in proportion to the foreign tax computation when a single foreign return taxed several items.

## 5. Offshore funds

Non-reporting fund disposals: offshore income gain = gain computed on CGT principles in sterling (no exempt amount, no indexation), taxed as income. SA106 page F6 box 56 ("gains on disposal of holdings in offshore funds"), with 56.1 if FIG is claimed. Distributions from such funds are foreign dividends/interest. Reporting funds: excess reportable income each year (from the fund's report) is income; disposals are CGT. Source: [HS265](https://www.gov.uk/government/publications/offshore-funds-self-assessment-helpsheet-hs265/hs265-offshore-funds).

## 6. Indian income on the UK return

Typical items for a UK resident with Indian holdings:

| Indian item | UK treatment | UK page |
|---|---|---|
| Indian mutual fund redemptions (equity, debt, international FoFs) | Usually non-reporting offshore funds: offshore income gains, taxed as income | SA106 box 56 (56.1 if FIG) |
| Directly held Indian shares sold | CGT in sterling | SA108 listed shares |
| NRO / savings / FD interest | Foreign savings income | SA106 interest, boxes 3/4 (4.1 if FIG) |
| NRE interest (tax-free in India) | Still taxable in the UK for a UK resident | SA106 interest |
| Dividends | Foreign dividends | SA106 dividends |
| Indian rental income | Foreign property income | SA106 land and property |
| EPF / NPS withdrawals | Specialist: may be pension or lump sum; get advice | |

Indian tax and cess on these items is creditable up to the UK tax on each item; Indian interest and late fees (234A/B/C, 234F) are not. Indian TDS on NRO interest above the treaty rate is reclaimed in India, not credited in the UK. The Indian financial year (1 April to 31 March) and the UK tax year (6 April to 5 April) differ: place each item in the UK year by its date. HMRC's average rate "year to 31 March" is a reasonable rate for interest; use daily rates for disposals.

## 7. Foreign pensions and social security

Foreign state and occupational pensions are taxable in the UK (usually with a 10% deduction for foreign pensions) unless the treaty gives exclusive taxing rights to the other state (common for government-service pensions). Contributions refunds and lump sums need case-by-case checking. Future pensions earned abroad (e.g. EU state pension rights) are reported only when paid.

## 8. Where it goes on the return

See `sa100-box-map.md` for SA106 boxes. Put the item-by-item list of FIG claims and FTCR workings in the computations attachment.
