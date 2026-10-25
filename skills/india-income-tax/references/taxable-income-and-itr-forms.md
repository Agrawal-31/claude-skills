# What is taxable, which ITR form, which regime

## Income map by head (what goes where)

| Item | NR treatment | Resident treatment | Schedule (ITR-2) |
|---|---|---|---|
| Indian salary (incl. RSUs/ESOPs taxed through Indian payroll) | Taxable if services rendered in India | Taxable | S (Salary) |
| Foreign salary for work outside India | Not taxable | ROR: taxable, credit for foreign tax | S + FSI/TR |
| Rent from Indian property | Taxable (tenant must deduct TDS u/s 195) | Taxable | HP |
| Interest on NRO savings / FDs | Taxable at slab rate; TDS 30% + surcharge + 4% cess | n/a | OS |
| Interest on resident (domestic) savings / FDs | Taxable | Taxable; 80TTA/80TTB in old regime | OS |
| Interest on NRE / FCNR deposits | Exempt while FEMA non-resident (s.10(4)(ii) / 10(15)(iv)(fa); 2025 Act Schedule IV) | Taxable for ROR | EI (exempt) |
| Interest on income-tax refund | Taxable | Taxable | OS ("interest on income tax refund") |
| The refund itself | Not income | Not income | - |
| Dividends from Indian companies / funds | Taxable at slab; TDS 20% (+ surcharge, cess) for NR, treaty rate with TRC + Form 10F | Taxable at slab; TDS 10% above threshold | OS (with quarterly accrual table) |
| Sale of listed shares / equity funds | 111A / 112A | 111A / 112A | CG + 112A |
| Sale of other funds, unlisted shares, property, gold | 112 / slab | 112 / slab | CG |
| Crypto / VDA | 30% flat, no set-off | same | VDA |
| Foreign shares, foreign funds, foreign bank interest | Not taxable | ROR: taxable | CG / OS + FSI, FA |

## ITR form selection (AY 2026-27)

Source: incometax.gov.in "Which ITR should I file" help page (AY 2026-27).

```
Any income from business or profession (incl. freelancing, consulting, F&O trading
treated as business, partner in a firm)?
  Yes -> ITR-3 (ITR-4 Sugam only for RESIDENT individuals/HUFs/firms on presumptive
         44AD/44ADA/44AE income up to the limits, no capital-gains complexity)
  No  -> Resident and Ordinarily Resident, total income <= Rs 50 lakh, only salary/pension,
         one house property, other sources, agri income <= Rs 5,000, and 112A LTCG
         <= Rs 1.25 lakh; no STCG, no foreign asset/income/signing authority, no unlisted
         shares, not a director, no losses brought/carried forward, no 194N TDS, no deferred
         ESOP tax?
           Yes -> ITR-1 (Sahaj)
           No  -> ITR-2
```

- **NR and RNOR can never use ITR-1.** If the portal pre-selects ITR-1 for an NRI, don't
  accept it.
- Use the "I know which ITR form I need" path on the portal once decided; the guided path
  sometimes suggests the wrong form.
- Filing the wrong form invites a defective-return notice under 139(9). If unsure between
  two, the higher form is safe.
- Due dates differ by income, not form number (from AY 2026-27, Finance Act 2026, per
  commentary): no business income -> 31 July; business income without audit -> 31 August;
  audit -> 31 October; transfer pricing -> 30 November. Confirm each year.

## Is filing mandatory?

Filing is required if any applies (1961 Act s.139(1) and its seventh proviso; same reasons
appear as the "reason for filing" question on the portal):

1. Total income before exemptions/deductions exceeds the basic exemption limit
   (new regime Rs 4 lakh from FY 2025-26; old regime Rs 2.5 lakh, Rs 3 lakh / Rs 5 lakh for
   resident seniors/super-seniors).
2. Seventh proviso conditions, for example: deposits over Rs 1 crore in current accounts;
   foreign travel spend over Rs 2 lakh; electricity bills over Rs 1 lakh; TDS/TCS of
   Rs 25,000 or more (Rs 50,000 for resident seniors); savings bank deposits of Rs 50 lakh or
   more in the year. (Check the current list on the portal screen.)
3. A resident with any foreign asset or signing authority (even with no taxable income).
4. Wanting a refund of TDS, or to carry forward a loss (loss returns must be on time).

**Portal "reason for filing" screen.** Pick in this order:
- "Taxable income is more than basic exemption limit" if total income exceeds the limit.
  Capital gains count; a person who first picked "Others" for a small refund had to change it
  after realising the gains pushed income over the limit.
- Otherwise "Seventh proviso" and tick the clause that applies (most often TDS >= Rs 25,000).
- Otherwise "Others" (for example, filing only to claim a refund of NRO TDS).
The answer does not change the tax; it records why you are filing.

## Old vs new regime

| | New regime (default, s.115BAC; 2025 Act s.202) | Old regime |
|---|---|---|
| Slabs | See `rates-and-limits.md` | See `rates-and-limits.md` |
| Standard deduction (salary/pension) | Rs 75,000 | Rs 50,000 |
| 80C, 80D, 80E, 80G, 80TTA/TTB, HRA, LTA, home-loan interest on self-occupied | Not allowed | Allowed |
| 80CCD(2) employer NPS, 80CCH Agnipath | Allowed | Allowed |
| 87A rebate (residents) | Up to Rs 60,000; income up to Rs 12 lakh (FY 2025-26 on) | Up to Rs 12,500; income up to Rs 5 lakh |
| Choosing it | Automatic | Non-business: tick in a return filed **by the 139(1) due date**. Business: Form 10-IEA by the due date |

- **Belated return = new regime.** The opt-out question on a 139(4) return is greyed at
  "No" or rejected. Explain this up front so nobody hunts for 80C on a late return.
- For an NRI whose income is mainly capital gains, the regime rarely matters: special rates
  are the same in both and the NR cannot use the basic exemption against them. NRIs can use
  80C/80D/80TTA (not 80TTB) under the old regime if they have slab income worth sheltering.
- Run `scripts/india_tax_calc.py` to compare. Don't recommend old regime unless the saving
  is real after counting only deductions the person can document.

## Scope checks for the person abroad

Before filing, ask once, plainly:
1. Any Indian salary or Indian-payroll share vesting this FY?
2. Rent from Indian property?
3. Sales of Indian shares, mutual funds, property, gold bonds?
4. Interest: which banks, and is each account NRO, NRE, FCNR or still a resident account?
5. Any freelance/consulting income paid by Indian clients (pushes to ITR-3 and the
   31 August date)?
6. Unlisted shares (exercised ESOPs of a private company)?
7. Any TDS they expect back?
For a resident, add: every foreign account, broker, share plan, pension, property and
insurance policy held at any time in the calendar year (Schedule FA).
