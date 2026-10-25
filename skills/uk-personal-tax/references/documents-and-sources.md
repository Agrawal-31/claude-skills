# Documents: what's needed, where to find it, how to check it

## Contents
1. Checklist by income type
2. Finding documents (email, drive, portals)
3. Reconciling payslips to the P60
4. Exchange rates and sterling conversion
5. Classifying accounts (ISA or not)
6. Source register

## 1. Checklist by income type

| Item | Document | Where it usually is |
|---|---|---|
| Employment pay and tax | P60 (year end) or P45 (left in year); every payslip | Payroll portal (Workday, ADP, etc.); emailed PDFs; employer HR |
| Benefits | P11D, or "payrolled benefits" lines on payslips | If payrolled, already in P60 pay; no P11D entry |
| Share awards | Vest/release confirmations, year-end summary, grant agreement (grant date) | Broker portal (Schwab, Morgan Stanley at Work, Fidelity, E*Trade); "release confirmation" emails |
| Share sales | Trade confirmations or annual realised gains report; broker monthly statements | Broker portal; check the month after year end for late trades |
| UK interest | Annual interest certificate or app statement | Bank app; "tax certificate", "interest statement" emails |
| Dividends (non-ISA) | Dividend vouchers / consolidated tax certificate | Broker |
| ISA | Nothing to report; just confirm it's an ISA | Provider statement |
| Foreign interest, dividends, fund sales | Bank interest certificates, broker capital gains statements, foreign tax deducted certificates | Overseas bank/broker portals; for India see the india-income-tax skill (AIS, Form 26AS, MF Central consolidated statement) |
| Foreign tax paid | Withholding certificates, the foreign return and assessment | |
| Pensions | Relief-at-source contribution statements; salary-sacrifice lines on payslips; pension input amounts for the annual allowance | Pension provider; payslips |
| Gift Aid | Donation records | Charity receipts, platform history |
| Residence and workdays | **The person's own estimate** of days abroad and workdays abroad per trip; the employer's HR status/attendance export and leave records | Ask the person; HR system. Not the mailbox (see below) |
| Prior years | Last return PDF, SA302, annual tax summary, HMRC letters | HMRC account; email |
| Admin | UTR, NI number, Government Gateway user ID (needed for commercial software) | HMRC letters; app |

Ask for everything missing in one message, with one line each on why it's needed.

## 2. Finding documents

If you can search the person's email or files, do it before asking. Queries that worked:

- P60 / payslips: `P60 OR payslip OR "pay slip" has:attachment after:YYYY/04/01`
- Broker: `(release confirmation OR "vest" OR "year-end summary" OR "realized gain") from:(schwab OR morganstanley OR fidelity OR etrade)`
- Bank interest: `("interest certificate" OR "tax certificate" OR "annual statement" OR "interest paid") after:<year end>`
- HMRC: `from:hmrc.gov.uk ("Self Assessment" OR "tax code" OR P800 OR "Simple Assessment")`; also `"Unique Taxpayer Reference"`
- Travel days: **don't search the mailbox.** In three real sessions, rebuilding trips from e-tickets, itineraries and calendar events took a long time and still left gaps, while the person could give a usable estimate in one message. The employer's status/attendance export was the definitive source for workdays abroad. Ask for both first. Reconstruct exact dates only if the result sits near a threshold that changes the outcome (SRT day-count bands, split-year conditions), and then only for the trips near the edge.
- Sales on overseas brokers: contract notes or daily statements from the broker's mailer

Practical snags: some connectors can't read WebP or scanned images (ask for PDF/PNG); spreadsheet and PDF downloads may arrive base64-encoded and need decoding; filters on HR exports can hide rows, so read the raw file. Payroll portals often stop working after leaving an employer, but people frequently emailed payslips to themselves.

## 3. Reconciling payslips to the P60

Sum all payslips for the tax year (tax months 1 to 12, the last one dated in March or early April) and check:

- taxable pay = P60 pay, to the penny;
- tax deducted = P60 tax;
- employee NI = P60 NI.

Then split taxable pay into components, because they're treated differently for workday relief and planning: base salary, salary-sacrifice pension (deducted before tax), bonus, RSU vest values (often shown as a gross-up with an offset line), dividend equivalents, allowances (transport, wellness), payrolled benefits (medical, dental). The P60 figure goes in SA102 box 1 unchanged; nothing on the payslip is added on top.

Typical RSU payslip lines: "RSU" taxable value, "RSU tax offset" (shares withheld to cover tax), "RSU excess refund" (cash back from over-withholding). Only the taxable value is pay.

If payslips don't reconcile, ask for the missing month before going further. A tax code change mid-year (e.g. 1257L to 0T) shows up here.

## 4. Exchange rates and sterling conversion

Every foreign amount goes on the return in sterling. HMRC accepts any reasonable, consistent method. What worked in practice:

- **Disposals (shares, funds, crypto)**: convert cost at the rate on the acquisition date and proceeds at the rate on the disposal date. Use Bank of England daily spot rates (database series such as XUDLUSS for USD, XUDLBK97 for INR into sterling), or the broker's own sterling figures if it reports them.
- **Recurring income (interest, dividends)**: HMRC's average rate for the year, published on the Trade Tariff service: [yearly averages](https://www.trade-tariff.service.gov.uk/exchange_rates/average) (e.g. "year to 31 March"), [monthly rates](https://www.trade-tariff.service.gov.uk/exchange_rates). Or the spot rate on each payment date.
- State the source and series in the computations attachment. Don't mix methods within one item.

## 5. Classifying accounts

Before treating broker activity as taxable, establish the wrapper:

- Stocks and Shares or Cash ISA: no tax, nothing on the return. Signs: provider labels it ISA; net subscriptions per tax year never exceed £20,000; deposits topping up to exactly the limit near 5 April.
- General investment account: dividends, interest and disposals are reportable.
- SIPP / workplace pension: nothing on the return except relief claims.
- Overseas accounts: taxable on the arising basis (unless FIG claimed); see `foreign-income-and-dtr.md`.

Ask the person to confirm the wrapper even when signals are strong; a wrong assumption can swing dozens of disposals onto SA108.

## 6. Source register

Keep a table in the pack: figure, value, source document (file name/link), date checked. Every box in the worksheet points to a row. Assumptions get their own rows marked "assumption" with the effect on the bill if wrong (for example, "25 days leave assumed; each extra leave day lowers the bill by about £20").
