# The tax-year folder

One folder per assessment year, shared with the agent as a single link, is the fastest way to
a filed return. It is a recommendation, not a precondition. Never hold up the work until the
person reorganises their files: collect from the portal, email and Drive first (step 3), and
offer the folder as the way to make this year faster and next year trivial.

The single most common error in practice is the wrong year: picking the wrong AY on the
portal, or downloading AIS/TIS for the wrong FY. A folder named for exactly one year, with the
FY and AY both in its name, is the cheapest guard against that.

## Layout

```
Tax/
└── India AY 2026-27 (FY 2025-26)/
    ├── Portal/              AIS, TIS, Form 26AS for this FY (check the year on each PDF)
    ├── Salary/              Form 16 / 16A (Form 130 from tax year 2026-27), salary slips
    ├── Bank interest/       interest certificates for every account, NRO / NRE / FCNR noted
    ├── Capital gains/       MF Central statement, broker Tax P&L, contract notes, holding statements
    ├── Residency/           travel history, passport stamps or immigration records, day counts
    ├── Foreign/             foreign tax paid, TRC, Form 10F, Form 67 (residents with foreign income)
    └── Return/              computation sheet, fill guide, challan receipts, ITR preview,
                             filed ITR PDF, acknowledgement, e-verification, 143(1) intimation
Wealth/
└── <broker or fund house>/  raw transaction exports that span years
```

- **Put both labels in the folder name**: `AY 2026-27 (FY 2025-26)`. From tax year 2026-27 the
  Income-tax Act, 2025 uses a single "tax year"; name those folders `India TY 2026-27`
  (see `income-tax-act-2025.md`).
- **If the person also files in the UK or elsewhere**, give that country its own year folder
  under `Tax/` in its own convention (e.g. `UK 2025-26`), not a shared one.
- **Keep multi-year exports under `Wealth/`**: purchase dates and costs for shares and fund
  units bought years ago are needed every time something is sold, including the 31 Jan 2018
  grandfathering values.
- **Record PDF password patterns** (often PAN in lower case, or PAN plus date of birth) in a
  private note, never in the folder name.

## What the agent does with it

1. **At the start**, ask once whether the person has (or wants) a year folder, and if so for
   its link. If documents are scattered, offer the layout above.
2. **If you can write to their Drive or file system**, offer to create the folders and file
   what you collected into them. Ask before moving or copying anything; never delete originals.
3. **Read the whole folder before asking for anything**, including subfolders, and check the
   FY printed on every AIS, TIS and 26AS against the folder's year.
4. **At close-out, save the outputs into `Return/`**: computation sheet, fill guide, challan
   receipt, filed ITR PDF, acknowledgement and e-verification confirmation. Add the
   post-filing record (see `post-filing.md`) as `Return/next-year.md`, including the figures
   handed to the residence-country return.

## Why it pays off

- **Year scoping** prevents the wrong-AY and wrong-AIS mistakes.
- **It is the record** for a 143(1) mismatch, a defective-return notice or a later ITR-U.
- **Next year starts from `Return/`**: carried-forward losses, refund history and the residency
  day counts that feed the next year's RNOR test.
