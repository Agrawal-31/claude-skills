# Channels, fees and rules (UK)

**As of 24 October 2026.** Every figure here changes. Before quoting one to the person, re-check the linked official page and update this file if it moved.

## Where to sell what

| Item type | First choice | Also | Why |
|---|---|---|---|
| Electronics, cameras, drones, audio, consoles, keyboards | eBay | Colleagues/friends | Buyers search by model; biggest pool |
| Bags, shoes, clothing, sports kit, small games | Vinted | Colleagues | Fashion/sport audience, prepaid labels, no seller fee |
| Monitors, TVs, chairs, desks, furniture, anything bulky | Colleagues, Facebook Marketplace, Gumtree (collection) | eBay collection-only | Posting is costly and risky |
| Old phones/tablets/mainstream laptops under ~£200 | Buyback (CeX, musicMagpie) | eBay | Not worth listing time |
| Study texts | Course student groups, eBay by ISBN | | Niche buyers |
| Small low-value bits | One bundle to colleagues | Charity | Postage and trips eat the value |
| Mattresses, used bedding, hygiene items | Donate / recycle | | Returns and hygiene complaints |
| "Refurbished" resale on Amazon | Not realistic | eBay | Amazon Renewed is a gated programme for refurbishment businesses; one-off sellers can list "Used" only |

Rule of thumb: get a buyback quote first to set the floor, then list where the buyers are.

## eBay UK (private sellers)

Source: https://www.ebay.co.uk/help/selling/fees-credits-invoices/fees-private-sellers-activated-managed-payments?id=4822 (checked 24 Oct 2026)
- No final value fee and no regulatory operating fee for UK private sellers, excluding Motors.
- 300 free listings a month, then 35p each. Optional upgrades cost extra (subtitle £2, Gallery Plus £2.50 in some categories, reserve 4%).
- 3% international fee if the buyer's address is outside the UK.
- Seller currency conversion 2.5% (2.75% from 1 Dec 2026). Dispute fee £16.80.
- **Buyers** pay a Buyer Protection fee on private sellers' items: reported as £0.75 + 4% of the price up to £300 + 2% from £300 to £4,000 (rollout reporting, Feb 2025; verify on eBay help). The seller's net is unchanged, but buyers see the higher total, so it matters for colleague-vs-eBay comparisons.

## Vinted UK

Sources: https://www.vinted.co.uk/help/1227 (parcel limits), https://www.vinted.co.uk/pricelist (fees), Vinted help pages on sending and payment (checked 24 Oct 2026)
- No seller fee on standard sales. Optional paid bumps.
- Buyers pay a mandatory fee at checkout, published as a range of 3 to 8% + £0.30 to £0.80 depending on the order. Third-party reports say Vinted's October 2026 terms rename it from "Buyer Protection fee"; not confirmed on Vinted's own page.
- Parcel limits (standard items): InPost locker/shop and home 64 x 38 x 41 cm, 2 kg; Evri L+2W+2H up to 245 cm, 2 kg; Royal Mail 2nd Class medium 61 x 46 x 46 cm, 2 kg. Heavy items: Evri up to 15 kg; Royal Mail up to 20 kg. The listing form's Small/Medium/Large choices map onto these; the label states the weight band, and the size can often be changed at drop-off.
- You must send within 5 business days or the order is cancelled automatically (the buyer can grant a short extension).
- The buyer has 2 days after delivery to confirm or raise an issue; payout follows completion. If the person is leaving soon, stop listing on Vinted about a week before.
- Labels are QR codes; the drop-off shop or locker prints them. No printer needed.

## Tax and reporting (UK)

Sources: https://www.gov.uk/guidance/check-if-you-need-to-tell-hmrc-about-your-income-from-online-platforms, https://www.gov.uk/government/news/no-tax-changes-for-online-sellers, https://taxhelpforhustles.campaign.gov.uk/buying-or-making-things-to-sell-and-online-selling-tax-rules/ (checked 24 Oct 2026)
- Selling your own unwanted possessions is generally not taxable income, however many you sell.
- Capital Gains Tax can apply to a single item or set sold for more than £6,000.
- Buying or making things to sell for profit is trading; the £1,000 trading allowance applies per tax year.
- Platforms report sellers with 30+ sales or about £1,700 (EUR 2,000) in a calendar year to HMRC. Being reported does not mean tax is due.
Say this briefly if the person asks or if a sale looks large; don't give tailored tax advice.

## Drones (UK)

Sources: https://www.caa.co.uk/newsroom/news/regulator-calls-on-new-and-existing-drone-users-to-learn-new-rules-before-taking-off/ and secondary guides (checked 24 Oct 2026)
- From 1 January 2026 a Flyer ID is required for drones of 100 g or more (previously 250 g). Secondary sources say an Operator ID is also required for 100 g to under 250 g drones with a camera.
- So do **not** write "249 g, no registration needed" in a listing. Write "sub-250 g; check current CAA rules for Flyer ID and Operator ID".

## Workplace and friends groups

- Usually the best prices for bulky items and the least hassle: no fees, no postage, handover at the office.
- Check the group's rules (some forbid links, some want prices in the post).
- An ex-colleague or friend can post in a group you can't reach; write their post in their voice ("posting for a friend") with a contact route through them.

## Paid tools and APIs

- No connector currently creates Vinted listings; Vinted has no public listing API.
- eBay has an official Sell Inventory API (developer account, OAuth with `sell.inventory`, business policies, inventory location, then create item, create offer, publish). Photos must be public HTTPS URLs and category item specifics hard-fail. Sold-price data (Marketplace Insights) is gated. Worth it only at repeat volume.
- eBay Seller Hub bulk CSV upload is a middle path for many listings.
- Cross-listing subscriptions exist; rarely worth it for a one-off clear-out.
