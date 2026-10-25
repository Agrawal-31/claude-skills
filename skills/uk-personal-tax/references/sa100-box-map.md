# SA100 and supplementary pages: boxes actually used

Box numbers are from the 2025-26 forms and notes (published by HMRC as SA100/SA102/SA106/SA108/SA109 2026 and their notes on assets.publishing.service.gov.uk). HMRC renumbers boxes between years: open the current year's notes before relying on a number. Software shows the same numbers in its "HMRC forms" view.

General rules: whole pounds; round income and gains down, tax paid and costs up. Every figure in the worksheet carries its source.

## Contents
1. SA100 main return
2. SA102 employment
3. SA106 foreign
4. SA108 capital gains
5. SA109 residence and FIG
6. SA110 / SA302 tax calculation
7. Notes boxes

## 1. SA100 main return

TR 6 boxes 2/3 and TR 7 box 19 were confirmed on a filed 2025-26 return; the other page references are approximate, so check the current form.

| Page | Box / question | Use |
|---|---|---|
| TR 2 | Supplementary page questions (employment, self-employment, partnership, UK property, foreign, trusts, capital gains, residence/FIG) | Answer yes only for pages you're filing; "Capital gains: yes" also triggers the computations prompt |
| TR 3 | UK interest, dividends | Non-ISA UK interest and UK dividends |
| TR 4 | Tax reliefs: relief-at-source pension contributions (gross), Gift Aid | Not salary sacrifice |
| TR 5 | Student loan, HICBC | |
| TR 6 | Box 2: don't collect underpaid tax through PAYE code; box 3: don't use next year's code for non-PAYE income | Tick both if leaving UK employment or preferring to pay directly |
| TR 7 | Box 19: any other information | General notes; use for a capital gains note if the software has no SA108 notes box |

## 2. SA102 employment (one page per employment)

| Box | Entry |
|---|---|
| 1 | Pay from this employment (P60/P45, including payrolled benefits, RSU vests, bonus) |
| 1.1 | Payrolled benefits affecting student loan (only if repaying one) |
| 2 | UK tax taken off pay in box 1 |
| 3 | Tips and other payments not on P60 |
| 4 | Employer PAYE reference (e.g. 123/AB45678) |
| 5 | Employer name |
| 6, 7 | Director / close company questions |
| 8 | Off-payroll working |
| 9 to 16 | Benefits from P11D (blank if payrolled) |
| 17 to 20 | Allowable expenses |

OWR comes off on SA109, not here. Don't tick "income arose from working abroad" in software when OWR is on SA109.

## 3. SA106 foreign

| Page / box | Entry |
|---|---|
| F1 box 1 | Unremittable income (rare) |
| F1 box 2 | Total FTCR if calculating yourself (HMRC calculates if blank) |
| F2 interest table, boxes 3 / 4 | Interest from overseas savings: row per country (country code, amount before tax, foreign tax, FTCR yes/no, taxable amount); box 3 total of column D, box 4 total of column F |
| 4.1 | Interest claimed under FIG |
| F2 dividends, boxes 5 / 6 / 6.1 | Foreign dividends; 6.1 FIG |
| 9.1 | Overseas pensions/benefits claimed under FIG |
| F6 box 56 | Gains on disposal of holdings in offshore funds (non-reporting funds) |
| 56.1 | Offshore fund gains claimed under FIG |
| F6 boxes 38 to 39 | FTCR on foreign gains (CGT) |

With FIG claimed on an item: foreign tax column blank, FTCR "no" (software may tick FTCR by default: untick it).

## 4. SA108 capital gains

| Box | Entry (listed shares and securities section) |
|---|---|
| 23 | Number of disposals |
| 24 | Disposal proceeds |
| 25 | Allowable costs (including purchase price) |
| 26 | Gains in the year before losses (include FIG-claimed gains here) |
| 26.1 | Amount claimed under the FIG regime |
| 27 | Losses in the year (nil for foreign losses in a FIG year) |
| 28 | Claim/election code (PRR, BAD, etc.); there is no FIG code |
| 29, 30 | Gains and tax already reported via real-time returns |

Other sections: UK residential property, other property/assets, unlisted shares, and from 2024-25 a cryptoasset section. Attach computations. Software that computes per disposal rounds each sale, so totals may differ by a pound or two from your sheet: acceptable.

## 5. SA109 residence and FIG (2025-26)

| Box | Entry |
|---|---|
| 1 | Not UK resident for the year |
| 3 / 3.1 / 6 | Split year: X, case number(s), date the UK part ends or begins |
| 4 | UK resident in the previous year |
| 7 to 13 | Residence test facts (overseas test, gaps, overseas home, UK days, exceptional days, ties, UK workdays): mostly for non-residents and split years |
| 16 | Non-resident claiming personal allowance |
| 23 | Date of arrival in the UK (qualifying new resident) |
| 24 | Last UK-resident tax year before the most recent arrival (blank if never) |
| 28 | X: FIG claim on foreign income |
| 29 | X: FIG claim on foreign gains |
| 30 | QAHC deemed foreign income |
| 40 / 41 | X: OWR election / X: OWR claim |
| 43 | OWR transitional provisions (prior remittance basis only) |
| 44 to 49 | OWR figures (see `owr-and-rsus.md`) |
| 50 to 53 | Temporary Repatriation Facility (former remittance-basis users only) |
| 54 | Any other information: arrival date, residence history, workdays and method, list of FIG items |

HMRC's free online service doesn't support SA109; SA109 notes say to use commercial software or an agent, and not to send it as an attachment.

## 6. SA110 / SA302 tax calculation

After filing, the SA302 (tax calculation) shows income, reliefs ("Foreign employment relief" for OWR, "Foreign income relief" for FIG), taxable income, tax, tax deducted and balance. Check it equals your computation within rounding. SA110 box 1 is total tax due; boxes 10/11 payments on account.

## 7. Notes boxes

Software may restrict characters. One app allowed only `A-Za-z0-9&'()*,-.@£` and 2,000 characters: no colons, slashes or semicolons. Write notes that survive stripping (use "2025-26", commas, parentheses), then read the final PDF to check sentences didn't run together. Every date and figure in a note must match the boxes.

Template for SA109 box 54 (generic):

> Arrived in the UK to live and work on [date], UK resident from [year] (split year) after more than 10 years of non-UK residence. Overseas workday relief covers [n] workdays abroad in [year], made up of [n] weekdays in [countries] and [n] days of business travel. FIG claims cover foreign interest of £[x] (SA106 box 4.1), offshore income gains of £[x] (SA106 box 56.1) and foreign share gains of £[x] (SA108 box 26.1). Workings are in the attached PDF.
