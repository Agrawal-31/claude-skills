# The tax-year folder

One folder per tax year, shared with the agent as a single link, is the fastest way to a
finished return. In the session this skill came from, the person shared a Drive folder at the
start ("use this folder for all documents"). The agent read the P60, 13 payslips and the RSU
statements from it in one pass, reconciled payslips to the P60 to the penny, and later picked
up new subfolders (broker exports, equity awards) as they were added.

It is a recommendation, not a precondition. Never hold up the work until the person
reorganises their files: search email and Drive first (Step 3), and offer the folder as the
way to make this year faster and next year trivial.

## Layout

```
Tax/
└── UK 2025-26/
    ├── Employment/              P60, P45, P11D, payslips/ (one PDF per month)
    ├── Equity/                  RSU vest confirmations, sale confirmations, broker year-end summary
    ├── Savings & investments/   bank interest statements, dividend vouchers, broker tax reports
    ├── Foreign/                 overseas income statements, foreign tax paid, offshore fund reports
    ├── Evidence/                travel/workday records, residence evidence, claim support
    └── Return/                  worksheet, computation, filed return PDF, submission receipt,
                                 payment confirmation, HMRC letters (P800, SA302, tax code notices)
Wealth/
└── <broker or platform>/        raw transaction exports that span tax years
```

- **Name the year folder by the UK tax year** (6 April to 5 April), e.g. `UK 2025-26`. If the
  person also files in another country, give that country its own year folder under `Tax/`
  in its own year convention (for India: `India AY 2026-27`), not a shared one.
- **Keep multi-year exports under `Wealth/`**, not inside a year. Broker histories, crypto
  exchange exports and share plan records are needed for cost basis in later years too (s104
  pools, RSU acquisition costs).
- **Use the source document's own file name** where it is already dated; otherwise
  `YYYY-MM-DD <issuer> <what>.pdf`.
- **Prefer PDF, PNG or JPG.** Some connectors cannot read WebP or HEIC; convert or re-export.

## What the agent does with it

1. **At the start**, ask once whether the person has (or wants) a tax-year folder, and if so
   for its link. If documents turn up scattered across email and Drive, offer the layout above.
2. **If you can write to their Drive or file system**, offer to create the folders and to
   file the documents you found (email attachments, downloaded statements) into them. Ask
   before moving or copying anything; never delete originals.
3. **Read the whole folder before asking for anything**, including subfolders, and list what
   is there against the checklist in `documents-and-sources.md`. Ask only for the gaps.
4. **When new subfolders appear mid-task**, re-list and pick them up without being told twice.
5. **At close-out, save the outputs into `Return/`**: the box-by-box worksheet, the
   computation, the computations attachment, the filed return PDF, the submission receipt and
   the payment confirmation. Then write a short `Return/next-year.md` with the carry-forward
   items (payments on account due, losses, RSU vests with relief still to come, split-year or
   FIG years used).

## Why it pays off

- **Year scoping** stops wrong-year documents leaking into the figures.
- **It is the evidence file** HMRC expects you to keep (see `deadlines-penalties-payments.md`
  for how long), already assembled if an enquiry arrives.
- **Next year starts from `Return/`**: last year's figures, payments on account and
  carry-forwards are in one place.
