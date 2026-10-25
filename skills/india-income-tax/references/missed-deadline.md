# Missed the deadline: options, costs, decision tree

Dates below are for AY 2026-27 (FY 2025-26) under the 1961 Act as amended by the Finance
Act 2026; confirm the current year's dates. Under the Income-tax Act, 2025 the same routes
exist in section 263 (return of income) with renumbered sub-sections.

## Decision tree

```
What period was the income earned in?  -> FY. AY = FY + 1. Select that AY on the portal.
|
+-- Was the 139(1) due date really missed?
|     no business income: 31 July | non-audit business/profession: 31 Aug (from AY 2026-27)
|     audit: 31 Oct | transfer pricing: 30 Nov | check for CBDT extensions that year
|     -> not missed: file a normal 139(1) return. Old regime still available. No fee.
|
+-- Missed, and today <= 31 Dec of the AY (and no assessment completed)?
|     -> BELATED RETURN u/s 139(4)
|        + refunds allowed, can file even if never filed before
|        - 234F fee, 234A interest, 234B/234C if advance tax short
|        - new regime only (no business income)
|        - business/capital losses of this year cannot be carried forward
|          (house-property loss can)
|        - later revision possible within the revised-return window
|
+-- After 31 Dec of the AY (belated window closed)
      |
      +-- Tax is payable / income was missed or under-reported
      |     -> UPDATED RETURN ITR-U u/s 139(8A), up to 48 months from end of the AY
      |        + additional tax 25% / 50% / 60% / 70% of (tax + interest) for filing within
      |          12 / 24 / 36 / 48 months after the AY ends
      |        + 234F fee and 234A/B/C interest still apply
      |        - cannot reduce tax, increase a refund, or create/increase a loss
      |        - not allowed if search/survey/assessment/reassessment is pending for that year
      |          (Budget 2026 reportedly allows it after a reassessment notice with +10%: verify)
      |        - one ITR-U per AY
      |
      +-- A refund is due (e.g. excess NRO TDS) or a loss needs carrying forward
            -> CONDONATION OF DELAY u/s 119(2)(b) (CBDT Circular 11/2024, 1 Oct 2024)
               application on the portal (e-File -> Income Tax Returns -> Condonation /
               "Request for condonation of delay") to the Principal CIT/CIT for claims up to
               Rs 1 crore per AY (higher authorities above), within 5 years from end of the AY;
               show reasonable cause and genuine hardship; no interest on the refund.
               If allowed, file the return within the time given.
```

If the person sees only "139(8A) Updated Return", "92CD" and "139(9A)" on the filing-type
screen, the selected AY's normal windows are closed. In a real case the person had simply
selected the previous AY; switching to the correct AY brought back "139(4) Belated".

## Cost of a belated return (what to tell the person)

| Item | Amount | Notes |
|---|---|---|
| 234F fee | Rs 5,000; Rs 1,000 if total income <= Rs 5 lakh | Nil if total income is within the basic exemption (filing not mandatory) |
| 234A | 1% per month (or part) on tax unpaid after TDS/advance tax, from the day after the due date to filing | Paying before the due date stops it even if the return is late |
| 234B | 1% per month from 1 April of the AY to payment, if advance tax < 90% of assessed tax | Applies whether or not the return is late |
| 234C | Instalment shortfalls (3 months each for June/Sept/Dec, 1 for March) | Capital-gains relief only if the tax on gains was actually paid in later instalments |
| Lost old regime | Difference between regimes | Only matters if old-regime deductions were large |
| Lost loss carry-forward | Future tax on gains that the loss would have sheltered | Capital and business losses |

Run `scripts/india_tax_calc.py` with `filing_date` set to today and the next month-end to
show how much one more month costs. Every month started adds 1% on the unpaid tax under both
234A and 234B, so pay and file within the current month.

## Choosing between options that overlap

- **Belated vs ITR-U before 31 Dec:** always the belated return; no additional tax.
- **Original return filed, mistake found:** revised return u/s 139(5) (window to 31 March
  after the AY from AY 2026-27, per Finance Act 2026 commentary; a fee is reported for
  revisions after 9 months). After that, ITR-U if it increases tax; rectification u/s 154 for
  a mistake apparent in the 143(1) intimation.
- **Return never filed, only TDS refund at stake, belated window closed:** ITR-U cannot give
  a refund. Use condonation, or accept the loss if small.
- **Mistake that doesn't change tax** (e.g. a loss row labelled pre-2018 when bought later):
  a revision is optional; note it for next year.

## Filing ITR-U

- Portal: File Income Tax Return -> AY -> filing type 139(8A) -> ITR-U plus the base ITR
  form; give the reason (return not filed, income not reported, wrong head, wrong rate...).
- Compute: tax + interest on the updated income, less taxes already paid; then additional
  tax on (tax + interest); pay via Challan 280 (minor head 300 for tax, interest and the
  additional tax) **before** filing; the challan details go in ITR-U Part B.
- Keep evidence of why income was missed; ITR-U is not a defence if a notice already exists.
