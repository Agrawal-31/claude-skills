# DTAA relief, Form 67, Schedules FSI / TR / FA, treaty TDS rates

Two different situations. Decide which applies first.

| Situation | Who gives relief | Where |
|---|---|---|
| **Non-resident** with Indian income (e.g. UK resident with Indian gains/interest) | India taxes as source country (treaty may cap the rate). The **residence country** gives credit for Indian tax | Residence-country return (UK: sibling skill uk-personal-tax). In the ITR, B-TTI "tax relief" stays 0 and Schedules FSI/TR/FA stay empty |
| **Resident (ROR)** with foreign income (foreign salary, foreign dividends, foreign share sales, foreign rent) | **India** gives credit for foreign tax under s.90 (treaty country) or s.91 (no treaty) | ITR Schedule FSI + Schedule TR, backed by **Form 67** |

RNORs are generally not taxed on foreign income, so they rarely need FTC; check case by case.

## A. Non-resident: reducing Indian tax and TDS

1. **Treaty rate on TDS.** Indian payers deduct at domestic NR rates (NRO interest 30% +
   cess). To get the treaty rate (India-UK DTAA: interest 15%, 10% where the beneficial owner
   is a bank; dividends 10% generally / 15% for some property-income vehicles), give the
   bank/fund house:
   - Tax Residency Certificate from the residence-country tax authority (UK: HMRC
     certificate of residence),
   - **Form 10F** filed electronically on the portal (mandatory e-filing since 2022; reported
     renumbered Form 41 under the Income-tax Rules, 2026),
   - PAN, and often a no-PE / beneficial-ownership declaration.
   Without them the higher domestic rate is deducted; the excess comes back only through the
   ITR as a refund.
2. **Claiming the treaty rate in the ITR.** If income is taxable at a DTAA rate lower than
   the domestic rate, report it in the OS / CG lines for "income taxable at DTAA rates" with
   country, article and rate, and have the TRC and Form 10F on file. Most NRIs with only bank
   interest don't need this because slab-rate income under the basic exemption is taxed at nil
   anyway; the TDS simply becomes a refund or offsets other tax.
3. **Capital gains:** India-UK Article 14 lets each state tax under its own law, so Indian
   gains stay taxable in India for UK residents. Some other treaties differ (see the
   India-Singapore ruling in `capital-gains.md`); India-Mauritius/Singapore/Cyprus share rules
   were amended in 2016-17. Check the specific treaty and any Limitation of Benefits clause.
4. **Hand-off to the residence country:** give the creditable Indian tax per income item.
   Only the tax and cess are creditable; 234A/B/C interest and the 234F fee are not.
   Apportion tax to items (e.g. 112A tax across funds in proportion to their gains). Keep
   the challan receipt, Form 26AS and the filed ITR as evidence of tax paid.

## B. Resident: foreign tax credit (Rule 128; 2025 Rules equivalent - check number)

**Rule:** credit = lower of (foreign tax paid on that income) and (Indian tax attributable to
that income), computed **source by source and country by country**. No credit for foreign
interest, penalty or tax under dispute (credit for disputed tax can be claimed after the
dispute settles, within 6 months). Convert at the SBI TT buying rate on the last day of the
month **before** the month the tax was paid/deducted.

**Form 67 (statement of foreign income and tax credit):**
- File online on the portal (e-File -> Income Tax Forms -> Form 67) **before** the return, or
  at least within the time allowed: from 1 April 2022 the rule allows filing on or before the
  end of the AY where the return is furnished under 139(1) or 139(4). Tribunals have mostly
  allowed credit despite late Form 67, but the department contests it; file on time.
- Attach proof of foreign tax: foreign tax return / assessment, employer certificate, or
  bank/broker statement of tax withheld, and the payment evidence.
- If foreign tax is later refunded or changed, file a fresh Form 67 / revised return.
- The new form number under the Income-tax Rules, 2026 was not confirmed when this was
  written; search "Form 67 Income-tax Rules 2026 new number".

**Schedule FSI:** country, foreign TIN, each head of foreign income (salary, house property,
capital gains, other sources), income included in total income, tax paid outside India,
Indian tax on that income, relief available (lower of the two), relevant DTAA article.

**Schedule TR:** totals of relief by country; section 90 / 90A / 91; whether any tax relief
was refunded.

**Schedule FA (foreign assets), residents (ROR) only, calendar year Jan-Dec ending in the FY:**

| Table | What |
|---|---|
| A1 / A2 | Foreign depository accounts (bank) / custodial accounts: peak balance, closing balance, gross interest |
| A3 | Foreign equity and debt interests: shares held directly, RSUs vested and held, ESPP shares |
| A4 | Foreign cash-value insurance / annuity contracts |
| B | Financial interest in any entity |
| C | Immovable property |
| D | Any other capital asset |
| E | Accounts with signing authority |
| F / G | Trusts, other income from outside India |

- Convert at the SBI TT buying rate on the relevant date (peak and closing values).
- Report even if no income arose and even if the asset was sold during the year.
- Penalty: Rs 10 lakh under the Black Money Act for non-disclosure (discretionary per a 2025
  Special Bench ruling); no penalty if aggregate non-immovable foreign assets are Rs 20 lakh
  or less (from 1 Oct 2024). Disclosure is still required.
- Returning NRIs: as RNOR, Schedule FA is not required; it starts in the first ROR year.

## C. NRE / NRO quick answers (frequent question)

| | NRE | NRO |
|---|---|---|
| Interest taxable in India | No, while FEMA non-resident (1961 Act s.10(4)(ii); 2025 Act Schedule IV) | Yes, slab rate |
| TDS | None | 30% + surcharge + cess; treaty rate with TRC + Form 10F |
| Funds | Money brought from abroad; repatriable | Indian-source income (rent, dividends, redemptions, pension) |
| Gains on investments made from it | Taxable in India | Taxable in India |
| Residence country | Usually taxes it as foreign interest (UK: yes, unless a special regime applies) | Same, with credit for Indian tax |
| On return to India | Redesignate as resident / RFC; interest becomes taxable | Redesignate as resident |

Tax can be paid from either account (Challan 280 via net banking).
