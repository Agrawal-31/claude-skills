# Residential status (individuals)

Law: section 6 of the Income-tax Act, 1961 (FY 2025-26 and earlier). The Income-tax Act,
2025 keeps residence in section 6 with renumbered sub-sections (182-day test 6(1)(a) ->
6(2)(a); deemed residence 6(1A) -> 6(7); RNOR 6(6) -> 6(13), per commentary mapping) and the
same substance. Status is decided **fresh for each FY**.

## Decision tree

```
Days in India this FY (arrival and departure days both counted)
|
+-- >= 182 ............................................ RESIDENT -> go to RNOR test
|
+-- < 182
    |
    +-- Indian citizen who LEFT India this FY for employment abroad / as ship crew?
    |       -> only the 182-day test applies .......... NON-RESIDENT
    |
    +-- Indian citizen or PIO, living abroad, who CAME ON A VISIT this FY?
    |       Indian income (excl. foreign-source) <= Rs 15 lakh
    |           -> 60 becomes 182 ......................... NON-RESIDENT
    |       Indian income > Rs 15 lakh
    |           -> >= 120 days this FY AND >= 365 days in 4 preceding FYs
    |                  ...................................... RESIDENT, always RNOR
    |           -> otherwise ............................... NON-RESIDENT (check deemed residence)
    |
    +-- Everyone else (foreign nationals, people not "visiting")
            -> >= 60 days this FY AND >= 365 days in 4 preceding FYs
                   ............................................ RESIDENT -> go to RNOR test
            -> otherwise ...................................... NON-RESIDENT

Deemed residence (s.6(1A)): Indian citizen, Indian income (excl. foreign-source) > Rs 15
lakh, and NOT liable to tax in any other country by domicile/residence/similar
  -> RESIDENT, always RNOR (regardless of days). Being tax resident in the UK, US etc.
     takes a person out of this rule; people in no-income-tax jurisdictions are the target.

RNOR test (for anyone resident): RNOR if ANY of
  (a) non-resident in 9 out of the 10 preceding FYs, or
  (b) in India 729 days or less in the 7 preceding FYs, or
  (c) resident only through the 120-day rule above, or
  (d) deemed resident under s.6(1A).
Otherwise ROR (resident and ordinarily resident).
```

"Indian income" for the Rs 15 lakh test means total income other than income from foreign
sources (income accruing from a business controlled in, or profession set up in, India counts
as Indian). Compute it before deciding; capital gains on Indian funds count.

"Came on a visit" is a fact question. Someone who moves back to India for good during the
year is not visiting; for them the 60-day test applies (often making them resident but RNOR,
which is the usual landing status for returnees for 2-3 years).

## Counting days

- Count every calendar day physically present in India, including arrival and departure days
  (the conservative and common practice; some advisers exclude one of them - if a case sits
  within a day or two of a threshold, get advice).
- Transit through an Indian airport without immigration is arguable; a day spent in a city
  en route counts.
- The ITR-2 residential-status screen asks for two numbers: **days in India during the
  previous year (this FY)** and **total days in the 4 preceding FYs**. Fill both with real
  figures. A real return was nearly submitted with both at the default 0.
- Keep the evidence (trip list with sources) with the tax papers.

### Getting the dates: ask, don't search

In the real session the agent ran 10+ mailbox searches (flight bookings, check-in emails,
ride-hailing receipts in rupees) to rebuild trips going back four years. The person then said
"we can put an estimate, it's fine for travel days". The estimate was quicker and good
enough, because the status wasn't close to any threshold.

1. **Ask for the trips:** roughly when and how long, per FY, including the emigration date
   (all days from 1 April to that date count for that FY).
2. **Run the checker** on the estimates and look at the margins. If the status is the same
   with every trip a few days longer, stop: enter the estimates.
3. **Only if it is close** (within about 10 days of 182, 60 or 120, or of an RNOR test), pin
   the trips that matter. Ask the person to check their passport stamps, immigration e-gate
   records or airline app. Mailbox searches are the last resort, limited to those trips.

"We can put an estimate" is acceptable for honest estimates. Deliberately lowering figures is
not, and gains nothing when the status is clear either way.

## Running the checker

```
python3 scripts/residency_days.py --example > trips.json   # edit it
python3 scripts/residency_days.py trips.json
```

Fields: `fy`, `trips` (arrive/depart ISO dates), optional `lived_in_india_until` plus
`history_start` (so earlier years count as full residence), `indian_citizen`,
`person_of_indian_origin`, `came_on_visit`, `left_for_employment_this_fy`,
`indian_income_excl_foreign`, `liable_to_tax_elsewhere`, optional `prior_statuses`,
`count_mode`.

The script prints the two ITR day counts, days by FY, the 7-year total, status and the rule
chain, and warnings when history is incomplete. It models the visit/employment exceptions
only for the target year.

## What each status means for the return

| | Non-Resident (NR) | RNOR | ROR |
|---|---|---|---|
| Taxable in India | Indian-source income only (received/accrues/arises in India) | Indian income + foreign income from a business controlled / profession set up in India | Worldwide income |
| Foreign salary, foreign bank interest, foreign shares | Not taxable, not reported | Generally not taxable | Taxable; report in Schedule FSI; foreign tax credit via Form 67 |
| Schedule FA (foreign assets) | No (answer "No" to the B-TTI foreign assets question; it says "applicable only in case of a resident") | No | **Yes, mandatory**, calendar-year basis |
| ITR-1 | Not allowed | Not allowed | Allowed if otherwise eligible |
| 87A rebate | No | Yes | Yes |
| Basic exemption against 111A/112/112A gains | No | Yes | Yes |
| Higher senior-citizen exemption (old regime) | No | Yes | Yes |
| 80TTB (seniors' interest deduction) | No | Yes (resident senior) | Yes |
| NRE / FCNR interest | Exempt (FEMA non-resident) | NRE: taxable once FEMA-resident; FCNR exempt for RNOR | Taxable |
| ITR-2 residency screen | "Non-resident", jurisdiction of residence + foreign TIN | RNOR condition chosen from dropdown | "Resident" |

FEMA status (decides NRE/NRO accounts) is a separate test from tax residency: someone who
leaves India for employment is FEMA non-resident from departure. Keep them distinct.

## Residency screen in ITR-2 (non-resident)

- Residential status: **Non-Resident**; pick the condition that says the person did not meet
  any residency condition.
- Jurisdiction(s) of residence: the country, e.g. United Kingdom. Add more only if tax
  resident in more than one country during the year.
- Taxpayer Identification Number: the foreign tax ID (UK: the 10-digit Self Assessment UTR;
  National Insurance number if no UTR; US: SSN/ITIN).
- Days in India (this FY) and in the 4 preceding FYs: real numbers.
- FPI: No (it is for registered portfolio investor entities). 115H (continuing special NRI
  investment-income rules after becoming resident): normally No.
- Unlisted equity shares held at any time during the year: Yes if they ever **exercised**
  options in a private company and still held the shares (needs company name, PAN, shares,
  cost). Unexercised options and RSUs of a listed company (Indian or foreign) don't count.
- Director in a company at any time in the year: answer truthfully (Indian or foreign
  company; needs DIN for Indian companies).
