# Documents: what, where from, how to open, how to reconcile

## Core statements from the e-filing portal (incometax.gov.in)

| Document | Where | What it shows | PDF password |
|---|---|---|---|
| **AIS** (Annual Information Statement) | Services -> Annual Information Statement (opens the AIS portal) -> choose the **Financial Year** -> download PDF or JSON | Every reported transaction against the PAN: interest by account, dividends, each security/fund sale with dates and cost where reported, TDS, refunds, foreign remittances | PAN in lower case + date of birth DDMMYYYY |
| **TIS** (Taxpayer Information Summary) | Same page | AIS aggregated by category; the "processed value" the department will use | same as AIS |
| **Form 26AS** | e-File -> Income Tax Returns -> View Form 26AS -> TRACES -> View Tax Credit -> pick AY -> HTML/PDF | TDS (Part I), 15G/15H (Part II), TDS on property/rent (Part IV), TCS, advance/self-assessment tax paid, refunds | date of birth DDMMYYYY |
| Prior ITR acknowledgement / filed return | e-File -> Income Tax Returns -> View Filed Returns | last year's figures, losses carried forward, bank account used for refunds | PAN lower case + DOB |
| Challan receipts | e-Pay Tax -> Payment history | BSR code, challan serial, date, CIN, minor head | none |

**Year trap.** AIS/TIS let you choose the year and now label it "Tax Year" in places. In a
real filing, the first AIS/TIS downloaded was for the following year and showed nothing
useful. Always check the period printed at the top before reading figures.

**Form 26AS head-of-income trap.** 26AS shows TDS under the deduction section (194A, 195,
194K...). The ITR pre-fills these rows but may leave "head of income" as "Not applicable",
which must be corrected (see portal walkthrough).

From tax year 2026-27, Form 26AS is reported to become **Form 168** and Form 16 **Form 130**
under the Income-tax Rules, 2026; the content is the same.

## Income documents

| Need | Get it from | Notes |
|---|---|---|
| Salary in India | Form 16 (Form 130 from TY 2026-27) from employer; payslips | Only Indian-payroll salary; foreign salary of an NR stays out |
| Bank interest | Each bank's interest certificate (net banking -> Tax / Interest certificate) | One per account incl. closed ones; mark each as NRO / NRE / FCNR / resident savings / FD |
| Mutual fund capital gains | **MF Central** (mfcentral.com): login with PAN + OTP, Reports -> Capital Gains Statement -> FY -> Excel | Covers CAMS and KFintech registrars in one file, lot by lot, with quarter split. Worked when KFintech's own sign-up failed |
| Mutual fund (alternative) | CAMS (camsonline.com -> Statements -> Capital Gain/Loss) and KFintech (mfs.kfintech.com) separately; or the AMC's own year-end email | AMC emails usually attach a password-protected PDF (often PAN in capitals); CAMS emails may only link to a request page |
| Shares | Broker tax P&L (e.g. Zerodha Console -> Reports -> Tax P&L, FY, Excel) | Plus a holding statement or contract note for purchase dates when the P&L is ambiguous |
| Purchase date of an old share | Broker DP / transaction statement or the original contract note | AIS may show a 31 Jan 2018 FMV for any listed share, which does **not** mean it was bought before 2018. A real filing marked a 2023 purchase as pre-2018 because of this |
| Rent | Rent agreement, receipts, tenant's TDS certificate (Form 16A) | Municipal taxes paid are deductible |
| Property sale | Sale deed, purchase deed, improvement bills, buyer's TDS certificate | NR seller: buyer deducts TDS u/s 195; consider a lower deduction certificate before the sale |
| Foreign income/assets (residents) | Foreign bank and broker statements for the **calendar year** (Schedule FA) and the FY (FSI), share plan statements, foreign tax return / tax paid proof | Needed for Form 67 too |
| Foreign tax ID (NRs) | e.g. UK UTR, US SSN | For the residency screen |
| TRC + Form 10F (NRs claiming treaty rates) | TRC from the residence-country tax authority; Form 10F filed online on the portal | Give both to the Indian bank/fund house for lower TDS |

## Opening the PDFs

- Ask for the password pattern, not the raw data: "AIS opens with PAN in lower case followed
  by date of birth". If tools are available (qpdf, pdftotext, openpyxl), decrypt and extract
  locally; never paste the full PDF text back to the person.
- Prefer Excel/CSV versions (MF Central, broker P&L) over PDFs; they keep lot detail.
- Connectors may read emails but not download attachments; ask the person to upload the
  file or put it in a shared folder.

## Reconciliation checklist

Build a single table: source line -> amount -> AIS line -> schedule. Then:

1. **TDS:** total of 26AS Part I = sum of the TDS schedule. Note each deductor's TAN and
   section.
2. **Interest:** every bank in AIS appears in your list; NRE interest identified as exempt.
3. **Sales:** every AIS sale (SFT-17/18 style entries for securities and fund units) matches
   a statement lot by value; AIS fund categories (equity vs other units) agree with your
   classification. Anything in AIS without a statement is a missing account.
4. **Dividends:** AIS dividend lines (often tiny) go in OS with their quarter.
5. **Refund interest:** interest on last year's refund (shown in 26AS/AIS) is income; the
   refund itself is not.
6. **Mismatch you believe is wrong:** submit AIS feedback ("information is incorrect /
   duplicate / belongs to another PAN") rather than ignoring it.

## Clues worth acting on

- NRI's fund redemptions show **no TDS** in 26AS -> the folios are still tagged resident.
  The return is unaffected (tax is paid via self-assessment), but the person should update
  folios, demat and bank KYC to NRI status with an NRO mandate (FEMA compliance).
- Domestic (resident) savings accounts still open after becoming NRI -> should be
  redesignated NRO; interest is taxable either way.
- A broker statement saying "Individual-Resident" for an NRI -> convert to an NRI demat/
  trading account (PIS where required) or close it.
