# Residence, split year, arriving and leaving the UK

Sources: [RDR3 statutory residence test guidance](https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3) (updated June 2026), [RFIG21000 split year cases](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig21000), [leaving the UK](https://www.gov.uk/tax-right-retire-abroad-return-to-uk), [voluntary NI abroad from 6 April 2026](https://www.gov.uk/government/publications/voluntary-national-insurance-contributions-for-periods-abroad-from-6-april-2026/voluntary-national-insurance-contributions-abroad-from-6-april-2026). Residence guidance moved from RDRM to the RFIG manual in 2025: don't cite RDRM12xxx pages.

## Contents
1. Statutory residence test
2. Split year
3. Arriving: first years
4. Leaving mid-year: the refund and how to get it sooner
5. P85 or a return?
6. What follows you abroad (RSUs, bonuses, UK income)
7. National Insurance and pensions when moving
8. Fact checklist

## 1. Statutory residence test (per tax year)

Apply in order. Days count if you're in the UK at midnight (with deeming rules for some frequent visitors, RFIG20720).

**Automatic overseas tests** (any one → non-resident):
1. UK resident in one or more of the previous 3 years and fewer than 16 UK days.
2. Not UK resident in any of the previous 3 years and fewer than 46 UK days.
3. Full-time work overseas, fewer than 91 UK days and fewer than 31 UK workdays (more than 3 hours), no significant break.

**Automatic UK tests** (any one → resident):
1. 183 or more UK days.
2. A UK home for at least 91 consecutive days (30+ in the year), present there on 30+ days, and no overseas home or fewer than 30 days in it.
3. Full-time UK work over a 365-day period with more than 75% of workdays in the UK.

**Sufficient ties test** otherwise. Ties: family, accommodation, work (40+ UK workdays), 90-day, and country tie (only for those resident in a prior year). Resident in any of the previous 3 years: 16-45 days needs 4 ties, 46-90 needs 3, 91-120 needs 2, over 120 needs 1. Not resident in any of the previous 3: 46-90 needs all 4, 91-120 needs 3, over 120 needs 2.

Software asks these as yes/no questions; for a normal full-year resident, answer the automatic overseas tests "no" and the 183-day test "yes", and the rest won't matter. Day counts can be estimates: ask the person for nights abroad per trip and take 365 minus the total. Say in the notes that it is an estimate. Only pin exact dates when a count sits near an SRT band edge.

## 2. Split year

Only for a tax year in which you arrive or leave. Leaving cases: 1 (start full-time work overseas), 2 (partner of someone in case 1), 3 (cease to have any UK home). Arriving: 4 (start to have only home in UK), 5 (start full-time UK work), 6 (cease full-time work overseas), 7 (partner of 6), 8 (start to have a home in UK). Where more than one applies there are priority rules (RFIG21030): for leavers, case 1 beats 2 and 3.

Effect: the overseas part is treated as non-resident for most foreign income and for employment income earned there; the UK part is taxed normally with the **full** personal allowance and full-year bands. Claimed on SA109 (box 3, case number, date the UK part ends or begins). A split year counts as a year of UK residence for the FIG 4-year window.

If software shows "eligible for split year" in a year with no arrival or departure, an earlier answer (often "did you have a second residence" or a future move) is wrong: go back and fix it rather than accepting the flag.

## 3. Arriving: first years

- First tax year: often split year (case 5 or 8).
- If 10+ years of non-residence before arrival: qualifying new resident for 4 tax years (FIG regime and OWR available, `foreign-income-and-dtr.md`, `owr-and-rsus.md`).
- Register for SA by 5 October after the year if a return is needed (foreign income, a claim, a split year).
- Leftover foreign tax affairs (old country's final return, deregistration from the population register, social security record) are not UK tax but affect evidence of the move date: keep the departure certificates.

## 4. Leaving mid-year: the refund and how to get it sooner

Why there's usually a refund: PAYE spreads the bands and allowance by month. If you leave in month 6, payroll has only given 7/12 of the bands, while the UK part of a split year is taxed on full-year bands and allowance. A 0T code (HMRC assumed a full year) makes it larger.

Size it:

```bash
python3 scripts/uk_tax_calc.py paye --year 2026-27 --code 0T --pay-to-date 70000 --period 6
python3 scripts/uk_tax_calc.py income-tax --year 2026-27 --employment 70000 --tax-paid 24601.50
```

Getting part of it early: update the income estimate for the employment in the HMRC app to the UK-part total (salary, bonus and any vests taxed before departure). If that total is under £100,000 (or under £125,140 for a partial allowance), the code moves from 0T to 1257L and the final cumulative payslip returns the year-to-date allowance at the marginal rate. Check the final payslip shows 1257L without W1/M1. Don't claim FIG/OWR for the leaving year unless it's worth more than the allowance it costs.

The rest comes via the return for the leaving year, which can be filed from 6 April after the year ends. Keep a UK bank account open for the repayment. RSUs vesting after departure may still carry UK-taxable slices (section 6), which reduce the refund.

## 5. P85 or a return?

- Not in SA and leaving: P85 (with P45 parts 2 and 3) to get the refund and tell HMRC.
- Filing a return for the leaving year anyway (split year, FIG, foreign income, RSU income after leaving): don't use P85; the return does the job. HMRC's online services can't be used to tell them you're leaving: the SA109 goes via commercial software or paper.
- Exception: continuing full-time work for a UK employer abroad for a full tax year: P85 plus return.
- Opt out of collecting any balance through a future tax code (SA100 page TR 6) if you won't have UK PAYE income next year; pay directly instead.

## 6. What follows you abroad

- **RSUs and other securities income**: apportioned over the vesting period by where duties were performed (UK workdays share stays UK-taxable even if the vest is after departure); the employer's mobility payroll may withhold. A treaty-non-resident but UK-resident person doesn't get the non-residence exemption for securities income.
- **Bonuses** earned for UK duties: UK-taxable when paid.
- **UK rental and UK interest**: remain UK-taxable as a non-resident (non-resident landlord scheme for rent).
- **Treaty**: the new country's treaty decides tie-breaks and which country taxes what; check the specific treaty on GOV.UK.

## 7. National Insurance and pensions when moving

- Check the NI record and State Pension forecast before leaving ([gov.uk/check-state-pension](https://www.gov.uk/check-state-pension)). Fill gaps with Class 3 **while still UK resident** if worthwhile.
- From 2026-27, voluntary Class 2 for periods abroad is closed (except limited groups); Class 3 abroad needs 10 continuous years of UK residence or 10 qualifying years. Existing Class 2 payers have a transitional route if they apply before 6 April 2027.
- At least 10 qualifying years are needed for any UK State Pension. Periods in the EEA/Switzerland (and some treaty countries) can count towards the 10 under coordination rules; the UK then pays its proportional share.
- UK workplace pensions stay invested; update address and contact details with each provider.
- Pension rights in the country you left (EU state pensions, provident funds) are paid later under that country's rules and taxed by your country of residence at the time.

## 8. Fact checklist

Arrival and departure dates (the actual day you flew to live/work, confirmed by flights and payroll); UK residence history for the previous 10 years; days in UK; UK home dates (tenancy); where duties were performed; job start/end dates; family location; prior remittance-basis claims; employer mobility arrangements. Make sure the date in SA109 box 23 matches the note text exactly.
