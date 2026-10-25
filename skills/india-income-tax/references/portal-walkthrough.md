# Portal walkthrough: incometax.gov.in, ITR-2 online (AY 2026-27 layout)

Work screen by screen. Ask for a screenshot of anything you are unsure of and reply with
exact values per field. The layout changes a little each year; adapt labels, keep the logic.

## Contents
1. Start the return
2. Part A: general and residency
3. Schedule-by-schedule fill guide
4. Check totals, pay, submit
5. Errors seen and fixes

## 1. Start the return

1. Log in -> e-File -> Income Tax Returns -> **File Income Tax Return**.
2. **Assessment Year:** FY + 1 (FY 2025-26 -> AY 2026-27). If the only filing types offered
   are 139(8A) updated return / 92CD / 139(9A), the AY is wrong or that year's normal window
   has closed.
3. **Mode:** Online. **Status:** Individual.
4. **Filing type:** "Original/Revised", then the section on the next screens: 139(1) if on
   time, **139(4) belated** if after the due date, 139(5) revised.
5. **ITR form:** choose "I know which ITR form I need" -> ITR-2 (or ITR-3). Don't accept a
   pre-selected ITR-1 for an NR.
6. **Reason for filing:** see `taxable-income-and-itr-forms.md` (taxable income above basic
   exemption > seventh proviso clause > Others).
7. If resuming, use **Resume Filing**, not Start New Filing; drafts persist.

## 2. Part A: general and residency

- **Opt out of new regime (115BAC(6))?** On time and old regime cheaper: Yes. Belated: it
  stays "No" (locked).
- **Personal info:** pre-filled from the PAN profile. For an NRI, a foreign address and
  foreign mobile are fine; keep the e-mail current - all notices go there.
- **Salary exemption questions** (allowances, HRA etc.): No unless there is Indian salary.
- **New-regime deductions screen:** only 80CCD(2) (employer contribution to Indian NPS) and
  80CCH (Agnipath). A foreign employer pension is not 80CCD(2). Usually No to both.
- **Residential status:** see `residential-status.md` for every field (status, condition,
  jurisdiction, foreign TIN, two day counts, FPI, unlisted shares, director).
- **Bank accounts:** list **every Indian account held at any time in the FY**, including
  ones closed since (dormant accounts may be skipped). Mark the one for refunds; it must be
  pre-validated on the portal (Profile -> My Bank Account) and PAN-linked. NRIs can choose a
  foreign bank account for refunds by giving SWIFT code and IBAN where the portal offers it,
  but an NRO account is the usual choice.

## 3. Schedule-by-schedule fill guide (NRI, no business income)

The portal marks schedules "Confirmed" even when empty. A person once reached the end with
every schedule confirmed and no numbers entered. Open each relevant one deliberately.

| Schedule | What to do |
|---|---|
| S (Salary) | Only Indian salary. Leave empty otherwise |
| HP | Indian property: rent received, municipal tax paid, 30% standard deduction automatic, interest on loan |
| **CG** | Fill per `capital-gains.md`: A2 (111A), A5 (non-equity STCG), B3 -> Schedule 112A, B8 (s.112 other assets). Then **Table F** |
| **112A** | One consolidated AE row + one row per pre-Feb-2018 holding |
| 112 / VDA | VDA only for crypto |
| **OS** | Savings interest (sum of NRO + domestic savings), deposit interest (FDs), dividends (with quarterly table), **interest on income-tax refund** (separate line). Section 57 deductions 0 |
| EI | Exempt income: NRE/FCNR interest (10(4)(ii) / 10(15)(iv)(fa)), agricultural income. Leave empty if none |
| CYLA / BFLA / CFL | Auto-computed set-off of current, brought-forward and carried-forward losses. Open each after CG/OS are done, check it matches, Confirm |
| AMTC | Not applicable to most individuals; confirm empty |
| Tax deferred on ESOP | Only for eligible Indian start-up employees; confirm empty |
| FSI / TR / FA | Residents only (foreign income, tax relief, foreign assets). Leave empty for an NR |
| SPI / SI | Clubbing / special-rate summary, auto |
| **Part B-TI** | Check: capital gains, other sources, gross and total income (rounded to Rs 10) against your computation |
| **Tax Paid** | TDS rows pre-fill from 26AS: open each, set **head of income** (interest TDS -> Other Sources; fund/share redemption TDS -> Capital Gains), confirm "TDS claimed this year" = full amount and carried forward 0. Self-assessment tax rows appear after payment |
| **Part B-TTI** | Tax on normal and special rates, 87A (0 for NR), surcharge, cess, relief (0 for an NR claiming credit abroad), interest and fee (open "Show details" for 234A/B/C/F), taxes paid, amount payable / refund |
| Foreign assets question (B-TTI) | "Applicable only in case of a resident": an NR answers **No** |

## 4. Check totals, pay, submit

1. Compare Part B-TI and B-TTI with your computation sheet line by line. A rupee or two from
   rounding is fine; anything more is a wrong entry somewhere (look at the schedule feeding
   that line). Note: B-TTI won't reveal a double-counted slab-rate item if it falls inside the
   NR's slab-rate band; only B-TI shows it.
2. **Pay:** use "Pay Now" on B-TTI (pre-fills Challan 280, AY, minor head 300). Payment by
   Indian net banking, debit card, UPI, or over the counter. The tax/interest/fee breakup on
   the challan can all go under "Tax"; the return uses the total.
3. Back in the return, the challan should appear under Tax Paid (self-assessment). If it
   doesn't after a few minutes, add it manually: BSR code, date of deposit, challan serial,
   amount. Amount payable must show 0. A few rupees of overpayment rounds to a nil refund.
4. **Preview Return** -> download the PDF -> read it (or let the agent parse it) -> fix ->
   **Proceed to Validation** -> errors list -> fix -> **Proceed to Verification**.
5. **E-verify now** (see `post-filing.md`).

### Deep review of the preview PDF

Before submitting, extract the preview PDF text and check:
- AY, section (139(1)/139(4)), regime flag, residential status and both day counts.
- Every bank account; refund account flagged.
- Each CG line: sale value on the right line (unquoted vs other), cost not altered, Table F.
- OS lines match AIS to the rupee.
- TDS rows: heads of income, full claim.
- Self-assessment challan details.
- B-TTI amount payable 0.
Comparing two preview PDFs with `diff` after an edit shows exactly what changed.

## 5. Errors seen and fixes

| Symptom | Cause | Fix |
|---|---|---|
| AY screen offers only 139(8A) / 92CD / 139(9A) | Wrong AY, or that year's belated window closed | Pick AY = FY + 1; if truly closed, see `missed-deadline.md` |
| AIS figures don't match anything | AIS downloaded for the wrong year | Re-download for the right FY; check the printed period |
| `common.errors.csv_row_skip` on Schedule 112A upload | Template rules (AE rows need blank FMV columns; whole rupees; current template) and the portal consolidating AE rows | Enter manually: one consolidated AE row (INNOTREQUIRD / CONSOLIDATED) + BE rows |
| 112A total double counts after upload | Old manual row left in place | Delete existing rows before uploading |
| Non-equity fund sale shows under "unquoted shares" | Wrong sub-line in A5 / B8 | Put sale value in "assets other than unquoted shares"; unquoted lines 0; answer No to "includes unquoted shares?" |
| "Table F Sl. No. X breakup is not equal to item 3x of BFLA" | Quarter split doesn't match the gain, often because an edit changed the cost | Restore the correct cost; re-enter Table F to equal each gain type exactly |
| OS total off by Rs 1 | A line typed 1 rupee off AIS | Match AIS exactly |
| TDS rows show head of income "Not applicable" | Default when pre-filling | Set Other Sources / Capital Gains per row |
| "Date of Deposit cannot be more than System Date" | Challan paid after midnight IST while the session/computer still on the previous date (common abroad) | Never change the challan date. Save draft, log out, resume in a new session; if it persists, wait until the local date catches up or set the computer's time zone to IST temporarily |
| Days in India show 0 | Default | Enter real counts |
| Old regime toggle greyed | Belated return | Expected: new regime only |
| B-TTI interest higher than expected | 234C on the standard schedule because no advance tax was paid; 234A/B by started month | Expected; the portal's figure is payable. Pay in the same month to avoid another 1% |
| Tax higher than "slab maths" suggests for an NRI | No 87A, no basic-exemption absorption of special-rate gains | Expected under the law |
| Pre-2018 share treatment questioned later | Purchase date taken from AIS FMV column | Check the broker statement; if the tax is unchanged, a revision is optional |
| Portal session timeouts | Long sessions | Save Draft often; drafts survive logout |
