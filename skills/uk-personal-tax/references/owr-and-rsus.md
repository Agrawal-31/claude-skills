# Overseas Workday Relief (OWR) and RSU apportionment

Sources: [EIM43550 onwards (OWR)](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43550), [EIM43565 general earnings](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43565), [EIM43575 securities income](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43575), [EIM43580 election and claim](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43580), [EIM43600 financial limit](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43600), [EIM43605 transitional](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim43605), [EIM77020 travel days](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim77020), [LITRG OWR](https://www.litrg.org.uk/international/uk-tax-uk-residents-foreign-income-and-gains/overseas-workday-relief).

## Contents
1. Who gets it (from 2025-26)
2. Cost and value
3. Counting workdays
4. The method, component by component
5. Box entries
6. Evidence and HMRC checks
7. Honest-claims line

## 1. Who gets it

- A qualifying new resident (FIG conditions, 4-year window) with employment duties performed outside the UK.
- An **OWR election** (s41M ITEPA) in the return for the year (SA109 box 40) plus a **claim** (s41P, box 41). The election matters even for later relief on trailing income from that year.
- No requirement to keep the pay offshore (unlike the pre-2025 rules).
- Cap: lower of 30% of qualifying employment income for the year and £300,000. Transitional rules (box 43) only for people who used the remittance basis in 2023-24 or 2024-25.

## 2. Cost and value

The election/claim removes the personal allowance and CGT exempt amount for the year. Worth it when foreign workdays are meaningful or the allowance is already tapered away. Each foreign workday is worth roughly (annual pay ÷ workdays) × marginal rate; show the person that number.

## 3. Counting workdays

- Total workdays = weekdays − bank holidays − leave (PTO, sick, bereavement, time off in lieu, company days off) + weekend/holiday days actually worked. Use the HR status export if one exists; read it unfiltered.
- A foreign workday: substantive duties performed wholly outside the UK that day. Leave abroad is not a workday, whatever the trip.
- Travel days (EIM77020), applied to weekends too when travel is for business:
  - journeys of 7 hours or less: morning departure or afternoon arrival = overseas workday; morning arrival or afternoon departure = UK workday;
  - journeys over 7 hours: morning departure and afternoon arrival = overseas workday; morning arrival and afternoon departure = half UK, half overseas.
- Time off in lieu earned by UK weekend work: add those weekend days as UK workdays when worked (or when taken, consistently).
- The reason for being abroad (personal trip with approved remote work) doesn't matter if the work was done there.

```bash
python3 scripts/uk_tax_calc.py workdays --year 2025-26 --leave-days 30 --extra-workdays 2
```

## 4. The method, component by component

Apportion on a just and reasonable basis; workday apportionment is the norm. Treat each pay element separately:

| Element | Method |
|---|---|
| Salary, general allowances, payrolled benefits, dividend equivalents | overseas workdays ÷ total workdays in the year |
| Pay tied to UK duties (e.g. UK commuting allowance) | not apportioned; exclude (conservative, per EIM77020's "specifically allocated" rule) |
| Bonus | over its earning period (e.g. calendar year); only days in the qualifying year can get relief; workdays in the pre-qualifying part are excluded from box 44 |
| RSU vests | accrue evenly per day over grant (or start) to vest; keep the slice in the qualifying year; × overseas ÷ total workdays inside that slice (`rsu-owr`) |

```bash
python3 scripts/uk_tax_calc.py owr --year 2025-26 --employment 90000 --foreign-workdays 15 --total-workdays 220
python3 scripts/uk_tax_calc.py rsu-owr --vest-value 8000 --grant 2025-01-20 --vest 2025-11-15 --year 2025-26 --overseas-workdays 9 --total-workdays 150
python3 scripts/uk_tax_calc.py income-tax --year 2025-26 --employment 120000 --owr-exempt 7500 --fig-claim --tax-paid 40000
```

Sensitivities worth showing: each extra leave day (raises the overseas share slightly), grant date (later grant = less pre-qualifying accrual), travel-day treatment. Later vests of the same award contain slices earned on this year's overseas days: note them for next year's return.

## 5. Box entries (SA109 2025-26 numbering; recheck each year)

| Box | Entry |
|---|---|
| 40 | X: OWR election |
| 41 | X: OWR claim |
| 43 | blank unless transitional (prior remittance basis) |
| 44 | qualifying employment income after deductions (P60 pay less income relating to non-qualifying years, e.g. pre-6 April 2025 RSU accrual and bonus share) |
| 46 | qualifying foreign employment income |
| 47 | financial limit (30% of box 44, max £300,000) |
| 48, 49 | relief claimed (lower of 46 and 47) |
| 54 | note: arrival date, number of overseas workdays and where, method, attachment reference |

SA102 box 1 stays at the full P60 pay; the relief comes off through SA109. Don't also tick a "work abroad" or "foreign earnings" option on the employment pages: that can double-claim. Some apps only accept whole days for the day count: round down and say so in the note; the pound figures carry the exact relief. If software calculates relief itself from the day count, override it with the computed figure.

## 6. Evidence and HMRC checks

HMRC often checks OWR claims, starting with claimed days against employer leave records. Keep what already exists (don't spend the session reconstructing it from the mailbox): flights and boarding passes, approvals for working abroad, the HR status export, something dated from each overseas workday (calendar, emails, commits), RSU grant and vest statements, and the workings. HMRC doesn't need the workings with the return; supply within the enquiry window if asked. Keep records at least until the enquiry window closes, and longer while later vests rely on them.

## 7. Honest-claims line

If someone asks to change leave days to working days abroad, decline: it's a false claim, the HR system keeps an edit history, and it endangers the genuine part. A genuine correction (actually worked on a day logged as leave) needs same-day evidence and an adjusted leave balance.
