---
name: india-income-tax
description: Gets an individual's Indian income tax return (ITR) actually filed and e-verified on incometax.gov.in, with depth for NRIs living abroad (UK, US, Gulf, Singapore) who have Indian income. Covers residential status (NRI / RNOR / resident; 182-day, 60+365, 120-day and Rs 15 lakh rules, deemed residency), what India taxes, ITR-1/2/3, old vs new regime, AIS/TIS, Form 26AS, Form 16, interest certificates, MF Central / broker capital gains statements, Schedules CG, 112A, OS, FA, FSI, TR, DTAA relief and Form 67, NRO/NRE interest, TDS refunds, Challan 280, e-verification, 143(1), and missed deadlines (belated 139(4), 234F fee, 234A/B/C interest, revised return, ITR-U, condonation), plus the Income-tax Act, 2025 'tax year' switch. Use whenever someone mentions an Indian tax return, ITR, AY/FY, PAN, AIS, 26AS, NRI tax, Indian mutual fund or share sales, the e-filing portal or a missed 31 July deadline, even if they only send a portal screenshot asking what to pick.
---

# India income tax: get the return filed

The goal is a filed, e-verified return with the right tax paid, not an explanation of tax law.
Work like a careful CA sitting next to the person: decide status and form, collect the
documents, compute the tax yourself, walk the portal screen by screen, check the portal's
numbers against yours, pay, submit, e-verify, and leave them a record for next year.

Read `DISCLAIMER.md` once. Say you are not a tax adviser when the stakes justify it
(large amounts, foreign assets, treaty claims, notices), and name the specific point a CA
should confirm rather than a blanket "consult a professional".

## Before anything: pin the year

Most first-screen mistakes are a wrong year. Indian years run 1 April to 31 March.

- Income earned 1 Apr 2025 to 31 Mar 2026 is **FY 2025-26**, filed as **AY 2026-27**
  under the Income-tax Act, 1961 (the return filed in 2026).
- Income from 1 Apr 2026 is **tax year 2026-27** under the **Income-tax Act, 2025**, which
  replaced the 1961 Act on 1 April 2026. The return for it is filed in 2027. Section numbers
  change (139 -> 263, 234F -> 428, 115BAC -> 202 and so on), and forms are renumbered
  (Form 16 -> Form 130, Form 26AS -> Form 168 reported). Read
  `references/income-tax-act-2025.md` whenever the return is for tax year 2026-27 or later,
  or a user quotes a section number you don't recognise.
- The portal and statements may already print "Tax Year" on documents. A person who
  downloads AIS/TIS for "Tax Year 2026-27" when they meant FY 2025-26 gets the wrong year;
  check the period printed on every statement.

If the person is on a portal screen offering only odd options (ITR-U, 92CD, 139(9A)), they
have almost always picked the wrong AY. Ask what period the income was earned in.

## Mistakes from real sessions: don't repeat them

Each of these cost the person time. They matter more than any rule below.

1. **Hunting the mailbox for travel evidence.** To get the day counts (this year, and India days in the preceding four years), the agent ran 10+ email searches for flight bookings, e-tickets and even ride-hailing receipts in rupees, going back years. The person then said "we can put an estimate, it's fine for travel days". **Ask first:** "Roughly when were you in India each year, and for how long?" Run `scripts/residency_days.py` on that. Only reconstruct exact dates when the result sits near a threshold that changes the status: 182 days; 60 days with 365 in the preceding four years; 120 days with Indian income over ₹15 lakh; or the RNOR tests. The two day-count fields must be truthful and reasonable, not stamped to the day.
2. **Searching email for capital-gains data.** The agent searched every mailbox, including trash, for one platform's statements and found nothing. Sale data comes from AIS, MF Central and the broker's Tax P&L, not from emails. Go there first.
3. **Sending the person to two registrars.** CAMS and KFintech separately, then KFintech sign-up failed. Start with **MF Central**: one login (PAN plus OTP), one statement covering both registrars.
4. **Jumping ahead in the form.** The agent went straight to checking Part B-TTI while the person hadn't entered a single number ("I didn't fill any number anywhere yet, guide me"). The portal marks schedules "Confirmed" even when they are empty. Ask which screen they are on and guide from the first unfilled schedule, in portal order.
5. **Patching an upload file in pieces.** The person needed a ready-to-upload Schedule 112A file and had to ask for "the full new template" after receiving a partial one. Deliver the complete file in the format the portal accepts, and say which existing rows to delete first.
6. **Over-producing the reference record.** Asked for notes "for next year and the UK return", the agent started building a polished document. The person wanted "just for my reference and AI context, not an article". Keep the post-filing record as terse tables and bullets.
7. **The wrong year, twice.** See "Before anything: pin the year". Check the AY on every screen and the FY printed on every AIS/TIS before using it.

## The workflow

Follow these stages in order. Each stage names the reference file that holds the detail;
load it when you reach that stage, not before.

### 1. Status (residency) - `references/residential-status.md`

Residency decides everything else: what income is taxable, which form, whether 87A and the
basic exemption help, whether Schedule FA applies. Determine it for the specific FY.

1. Ask the person for their India trips with approximate dates and lengths, for the FY and
   the 4 (better 10) preceding FYs. **Don't search the mailbox for travel evidence** (mistake
   1 above). An honest estimate is fine for the two day-count fields. Pin exact dates only
   for trips whose length could move the result across a threshold, and ask the person to
   check those against their passport or airline app.
2. Run `scripts/residency_days.py` (both arrival and departure days count by default). It
   prints the day counts the ITR asks for and the status with the rule chain.
3. Confirm the judgment facts yourself: did they come "on a visit", did they leave India
   this year for employment, is Indian income (excluding foreign-source income) above
   Rs 15 lakh, are they tax resident elsewhere.
4. Fill the residency worksheet in `references/worksheets.md` and show it to the person.

Shortcut for an Indian citizen settled and tax resident abroad who only visits: under 182
days is Non-Resident when Indian income is up to Rs 15 lakh; above Rs 15 lakh, under 120
days is still Non-Resident. Returnees and foreign nationals need the full tree (60+365).
Day counts still go on the return, so never leave them at 0.

### 2. Scope and form - `references/taxable-income-and-itr-forms.md`

- **NR / RNOR:** only Indian income (received or accruing in India). Foreign salary, UK
  accounts and foreign investments stay out. RNOR also excludes most foreign income.
- **ROR:** worldwide income, plus Schedule FA (foreign assets, calendar-year basis) and
  Schedule FSI/TR if claiming foreign tax credit (needs Form 67).
- **Form:** ITR-1 only for ROR with simple income up to Rs 50 lakh. NR and RNOR always use
  **ITR-2** (no business income) or **ITR-3** (business/professional income in India).
  When unsure, go one form up: ITR-2 covers everything ITR-1 does, and a wrong form makes the
  return defective under 139(9).
- **Regime:** the new regime is the default. The old regime can be chosen only in a return
  filed by the 139(1) due date (no business income). A belated return is locked into the new
  regime; tell the person this before they look for 80C. Run `scripts/india_tax_calc.py`,
  which prints both regimes and marks the old one unavailable when belated.

### 3. Documents - `references/documents.md`

Ask once whether the person keeps a year folder and, if so, for its link; if not, offer the
layout in `references/tax-folder.md` (and to build it, if you can write to their Drive). Don't
wait on it. Collect, then reconcile before entering a single number. Minimum set:

- **AIS** (and TIS) and **Form 26AS** from the portal, for the right FY.
- Form 16 / 16A (Form 130 from tax year 2026-27), salary slips if any Indian salary.
- Interest certificates for every Indian bank account held during the year, including
  closed ones; note which are NRO, NRE, FCNR or resident.
- Capital gains statements: **MF Central** (covers CAMS + KFintech funds in one file, Excel,
  lot by lot), broker **Tax P&L** (Zerodha Console etc.), plus the broker contract notes or
  holding statement for purchase dates of shares.
- Prior-year ITR acknowledgement (for carried-forward losses and refund history).
- For residents with foreign items: foreign bank/broker statements, foreign tax paid
  evidence, employer share plan statements.

Reconcile: every AIS line must map to a statement line or be explained. AIS is what the
department will match against; a one-rupee difference (77 vs 78) is worth fixing.

### 4. Compute - `references/capital-gains.md`, `references/rates-and-limits.md`

Classify every item and compute the tax before opening the return form. Mutual funds are
where errors hide: equity-oriented funds (65%+ Indian equity) go to 111A/112A; international
FoFs, foreign-index funds and other non-equity funds go to section 112 / slab rate and get
no Rs 1.25 lakh exemption; debt funds bought after 1 Apr 2023 are always short-term. AIS
usually labels the type; check the AMC's own classification when a statement calls every
fund "equity".

Use `scripts/schedule_112a_helper.py` for lot-level equity gains (it builds the consolidated
112A row, grandfathered BE rows and the Table F quarter split) and `scripts/india_tax_calc.py`
for the total tax, both regimes, and 234A/B/C/F. Produce a computation sheet in the format in
`references/worksheets.md`. Rules that surprise non-residents:

- No 87A rebate for non-residents. RNORs are residents, so they get it.
- A non-resident's unused basic exemption cannot absorb 111A/112/112A gains. A resident with
  identical income can pay nil where an NRI pays 12.5%. This is the law, not a filing error.
- TDS deducted at 30%+ on NRO interest counts against the whole liability, including tax on
  gains.

### 5. Pay before submitting

If tax is still due after TDS and advance tax, pay it as **self-assessment tax**: portal
e-Pay Tax -> Income Tax -> AY (= FY + 1 under the 1961 Act) -> Minor head **300**
(Challan 280 / ITNS 280). The return's "Pay Now" button pre-fills this. Round up to the next
Rs 10. Keep the BSR code, challan serial number, date and CIN; they must match exactly in
Schedule Tax Paid. Pay in the same month you file: interest rises by 1% per started month.

### 6. File on the portal - `references/portal-walkthrough.md`

Walk the person through the online form screen by screen. Ask for a screenshot at every
screen you are not sure about and answer with exact field values. The walkthrough file has
the filing-section choice, the "reason for filing" (seventh proviso) choice, the residency
screen, every schedule an NRI typically fills, and a table of portal errors with fixes,
including:

- Schedule 112A: post-31 Jan 2018 holdings go in **one consolidated row** (ISIN
  `INNOTREQUIRD`, name `CONSOLIDATED`, whole rupees). Per-fund CSV upload failed with
  `common.errors.csv_row_skip`.
- Schedule CG "other assets" sale value goes in **"assets other than unquoted shares"**, not
  the unquoted-shares line.
- Table F (quarter of accrual) must equal each gain type exactly, or validation fails with a
  BFLA mismatch.
- TDS rows default to head of income "Not applicable": set Other Sources / Capital Gains.
- "Date of Deposit cannot be more than System Date": a time-zone clash for people abroad who
  paid after midnight IST. Never change the challan date; wait or switch the computer to IST.

After filling, check Part B-TI (total income) and Part B-TTI (tax) against your computation.
If they differ, find the schedule that is wrong before paying anything.

### 7. Submit and e-verify - `references/post-filing.md`

E-verify immediately (Aadhaar OTP, net banking, pre-validated bank or demat account EVC, or
signed ITR-V posted to CPC Bengaluru). It must be done within 30 days of upload or the
return is treated as not filed; the verification date can become the filing date. Download
the acknowledgement, the full return PDF and the challan receipt.

Then: watch for the 143(1) intimation, handle refunds or defective-return notices, fix
mismatches in folio/demat/bank residency tags, and write the next-year notes.

## Missed the deadline? - `references/missed-deadline.md`

Decision order (AY 2026-27 dates; confirm current-year dates):

1. Is it really late? ITR-1/ITR-2: 31 July. Non-audit ITR-3/ITR-4: 31 August from AY 2026-27
   (Finance Act 2026). Audit cases later. A person with business income may still be on time.
2. Before 31 December of the AY: **belated return u/s 139(4)**. Refunds allowed. Costs: 234F
   fee (Rs 5,000; Rs 1,000 if total income is up to Rs 5 lakh; nil if income is within the
   basic exemption), 234A interest 1% per month on unpaid tax, 234B/234C if advance tax was
   short. New regime only. Most losses cannot be carried forward.
3. After that: **updated return ITR-U u/s 139(8A)**, up to 48 months from the end of the AY,
   with additional tax of 25/50/60/70% of tax plus interest by year band. It can only
   increase tax: no refund, no new loss.
4. Refund stuck because the window closed: condonation of delay u/s 119(2)(b) (CBDT
   Circular 11/2024, within 5 years of the AY end).

Quantify the cost with `scripts/india_tax_calc.py` (set `filing_date`) so the person sees
the rupee figure, and tell them the portal's figure is what they pay.

## Cross-border: treaty relief and the other country

- **NR with Indian income:** India taxes first as source country. Treaty rates can cut TDS
  (India-UK: interest 15%, dividends 10/15%) if the bank or payer gets a Tax Residency
  Certificate plus Form 10F filed on the portal (Form 41 under the 2025 Rules, reported).
  Capital gains on Indian shares and funds are usually taxable in India under its own law
  (India-UK). The foreign tax credit for Indian tax is claimed in the country of residence,
  not in the ITR: B-TTI "tax relief" stays 0. Hand the Indian figures (tax and cess only;
  interest and fees are not creditable) to the residence-country return.
- **ROR with foreign income:** India taxes worldwide income and gives relief u/s 90/91 via
  Schedule FSI and TR, only if **Form 67** is filed (by the end of the AY for returns under
  139(1)/139(4), per the 2022 rule change; tribunals have been lenient on late filing but do
  not rely on it). Schedule FA is mandatory for residents with any foreign asset, even
  income-free ones; the Black Money Act penalty is Rs 10 lakh, with a Rs 20 lakh aggregate
  threshold for non-immovable assets from 1 Oct 2024.
- Detail: `references/dtaa-and-form-67.md`.

For the UK side (Self Assessment, foreign tax credit relief on Indian tax, treatment of Indian
mutual funds as non-reporting offshore funds, the FIG regime), use the sibling skill
**uk-personal-tax**. Pass it the Indian figures from the computation sheet: each gain with
dates, the Indian tax and cess by gain type, interest by account, and TDS.

## Outputs to produce

Produce these as files or clearly formatted messages, using the templates in
`references/worksheets.md`:

1. **Residency determination worksheet**: trips, day counts, tests, status, evidence.
2. **Income map and computation sheet**: every income line, its schedule, rate, tax; both
   regimes if available; TDS; interest and fee; balance payable.
3. **Schedule-by-schedule fill guide**: exact values per field, in portal order.
4. **Pre-filing checklist** and **post-filing record** (acknowledgement, challan, figures for
   the foreign return, next-year actions).

Save all of these, plus the challan receipt, filed ITR PDF and acknowledgement, into the year
folder's `Return/`, with the post-filing record as `Return/next-year.md`
(`references/tax-folder.md`). The next year's return is far faster with it.

## Scripts (python3, standard library only)

| Script | Use |
|---|---|
| `scripts/residency_days.py trips.json` | Day counts per FY and NR / RNOR / ROR with the rule chain (`--example` for input) |
| `scripts/india_tax_calc.py input.json` | Tax under both regimes, 87A, surcharge, cess, residency effects, 234A/B/C/F (`--example`) |
| `scripts/schedule_112a_helper.py lots.csv` | Equity lots -> 111A/112A split, consolidated AE row, grandfathered BE rows, Table F |
| `scripts/selftest.py` | Re-run after editing any rate table; all cases should pass |

On a real belated NRI return the calculator matched the portal's 234A/234B/234C/234F to the
rupee and the tax within Rs 1 of rounding. Still treat it as a check, not the answer.

## Ground rules

- **Verify current figures.** Every rate and limit in this skill is labelled by FY/AY and
  was checked in late 2026. Before relying on one for a different year, search
  incometax.gov.in / incometaxindia.gov.in or the latest Finance Act, and say which year a
  figure is for.
- **The portal's computed figure wins** for interest and tax; use yours to catch errors, not
  to argue with it. A large gap means a wrong schedule entry.
- **Never alter official data to make validation pass** (challan dates, TDS amounts, AIS
  figures). Fix the entry that is actually wrong.
- **Truthful day counts.** Best estimates from evidence are fine; zero is not.
- **Sensitive data.** PAN, Aadhaar, date of birth and bank details are needed to open PDFs and
  fill the form. Use them only for that, don't repeat them back unnecessarily, and don't
  store them in notes meant for other people. Common PDF passwords: AIS/TIS and the ITR
  acknowledgement = PAN in lower case + date of birth DDMMYYYY; Form 26AS = DOB DDMMYYYY;
  CAMS/KFintech statements = whatever password the person set when requesting them.
- **Residency tags.** If an NRI's mutual fund folios, demat or savings accounts are still
  tagged resident (no TDS on redemptions, domestic savings account), flag it as a FEMA and
  TDS issue to fix with the fund house/bank; it does not change the return itself.
