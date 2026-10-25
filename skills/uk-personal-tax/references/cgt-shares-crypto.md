# Capital gains: shares, RSU sales, funds, crypto, property

Rates and exempt amount: `rates-and-thresholds.md` section 4. Compute with `scripts/uk_tax_calc.py cgt`; for many trades use a matching tool such as `cgt-calc` (KapJI/capital-gains-calculator, MIT), which applies the rules below to broker exports.

## Contents
1. Is it a disposal? Is it a capital gain at all?
2. Matching rules
3. RSUs and employee shares
4. Sterling conversion
5. When SA108 is needed
6. Crypto
7. Losses
8. Property
9. Worked example (generic)

## 1. Is it a disposal? Is it a capital gain at all?

Disposals: sale, exchange (including crypto-to-crypto), gift (at market value, except to a spouse/civil partner or charity), using an asset to pay for something. Not CGT:

- ISA and pension holdings: ignore.
- **Non-reporting offshore funds** (most Indian and many other overseas mutual funds, some ETFs domiciled abroad): the gain is an *offshore income gain*, taxed as income at your marginal rate and reported on SA106 (page F6, box 56). Check HMRC's [list of reporting funds](https://www.gov.uk/government/publications/offshore-funds-list-of-reporting-funds) by ISIN; a fund on the list is taxed under CGT instead. Don't put offshore fund gains on SA108 and don't enter them as "other UK income" (both mis-tax them).
- Employment income on RSU vest or option exercise: taxed through payroll as pay; only later price movement is CGT.

## 2. Matching rules (shares and crypto tokens)

For each class of share or token, match a disposal in this order:

1. acquisitions on the **same day**;
2. acquisitions in the **next 30 days** (bed and breakfasting);
3. the **section 104 pool** (average cost of everything else).

Source: HMRC HS284 and the [crypto guidance](https://www.gov.uk/guidance/check-if-you-need-to-pay-tax-when-you-sell-cryptoassets). Confirm with the person that nothing was bought back within 30 days of a sale; the computation should say so explicitly.

## 3. RSUs and employee shares

- Base cost of vested shares = market value at vest that was charged to income tax (the employer uses it; the broker's "cost basis" usually matches). Shares withheld to cover tax are not a disposal by you.
- Sell-to-cover or immediate sales a few days after vest typically produce small gains or losses from price movement. Identify each sale with the vest it came from (same-day / 30-day rules usually do this automatically).
- Foreign shares (a US employer's stock) are foreign assets: relevant if a FIG claim is made (gains relievable; losses not allowable in that year).
- Dividend equivalents paid through payroll are pay, not dividends.

## 4. Sterling conversion

Cost at the rate on the acquisition date, proceeds at the rate on the disposal date (Bank of England daily spot rates). State the series in the attachment. A falling foreign currency can turn a foreign-currency gain into a sterling loss, and vice versa. Indian funds bought over several years need a rate per purchase lot; the consolidated statement lists each lot.

Fund statements may show redemption amounts net of transaction taxes (India's STT) while gains are computed on gross values; derive cost from the purchase amounts, not "amount minus gain". Check the rupee totals tie to the foreign return.

## 5. When SA108 is needed

Complete SA108 if any of: disposal proceeds of chargeable assets over £50,000; gains before losses over the annual exempt amount; claiming losses; any claim or election (including a FIG claim on gains). Otherwise gains under the exempt amount don't need reporting. Use the real-time CGT service for a one-off gain if you're not otherwise in SA (by 31 December after the tax year).

Lesson from practice: an accountant left small crypto gains (under the exempt amount, proceeds well under £50,000) off the SA108 and kept the computation on file. That was correct. A model quoting an outdated "4 × exempt amount" proceeds test nearly pushed a complaint. Before challenging a preparer, check the current trigger, ask for their workings, and get the proceeds figure.

What to enter (listed shares section): number of disposals, total proceeds, total allowable costs, gains before losses, FIG amount (box 26.1 if claimed), losses. Whole pounds: proceeds and gains rounded down, costs rounded up. Attach a computation listing each disposal.

## 6. Crypto

- Each token type has its own pool; matching rules as above.
- Taxable events: selling for fiat, swapping for another token, spending, gifting. Staking/mining rewards are usually income when received (then their value is base cost).
- Records HMRC expects: per transaction type, date, number of tokens, sterling value, cumulative pool cost before and after, exchange statements. Exchange "tax reports" help but don't track pooled cost on their own.
- From 2024-25 the return has a dedicated cryptoasset section; report there rather than in "other property".
- Many transactions: use crypto tax software or `cgt-calc`-style matching, then enter totals. Keep the transaction-level file.
- Unpaid tax for earlier years: HMRC's Cryptoasset Disclosure Service.

## 7. Losses

- Same-year losses reduce gains before the exempt amount; brought-forward losses only reduce gains down to the exempt amount.
- Losses must be claimed (reported) within 4 years of the end of the tax year to be carried forward.
- In a FIG claim year, foreign losses are not allowable and can't be carried forward; enter losses as nil and explain in the notes.
- Losses on assets to connected persons are ring-fenced.

## 8. Property

UK residential property: report and pay within 60 days of completion through the UK property CGT service, then include on the return. Main-residence relief, letting relief and periods abroad are adviser territory if the numbers matter.

## 9. Worked example (generic)

Higher-rate taxpayer, 2025-26, taxable income £60,000. Sold shares for £30,000 (cost £18,000), and a separate holding at a £2,000 loss. Net gains £10,000; minus £3,000 exempt = £7,000 at 24% = £1,680.

```bash
python3 scripts/uk_tax_calc.py cgt --year 2025-26 --gains 12000 --losses 2000 --taxable-income 60000
```

SA108: proceeds and costs for both disposals, gains before losses £12,000, losses £2,000. No SA108 would be needed if gains were under £3,000 and proceeds under £50,000.
