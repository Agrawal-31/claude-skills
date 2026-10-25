---
name: sell-my-stuff
description: End-to-end UK resale of a person's own belongings - find what they own by mining their email (and photos) for receipts, decide what to sell, price it from real sold data, write listings, create eBay and Vinted drafts in their browser, run a colleague/friends sale page and status sheet, then handle offers, buyers, box sizes and postage, wrong-item or order problems, platform support, and tracking what sold. Use whenever someone wants to sell, declutter, clear out before a move, asks "what can I sell" or "what is this worth", wants eBay/Vinted/Facebook Marketplace/workplace-group listings or posts, wants a sale page or spreadsheet, asks what box or parcel size to buy for something they sold, needs to reply to a buyer or open a Vinted/eBay support case, or wants a sold-items tracker. Use it even for a single piece of the job (just pricing, just one listing, just "I sent the wrong item"), because the guardrails here prevent the expensive mistakes.
---

# Sell My Stuff

Turn "I have loads of stuff, help me sell it" into money in the bank, without listing things that were returned or belong to someone else, selling the same item twice, underpricing boxed items, or leaking personal data.

The job runs in stages. Each stage leaves an artifact the person checks before the next. Enter at whatever stage they need, but keep the guardrails at the bottom on throughout.

| Stage | Output | Read |
|---|---|---|
| 1. Inventory from email | Master inventory + selection sheet | `references/inbox-search.md` |
| 2. Identify from photos | Matched, labelled photos ready to publish | `references/photos.md` |
| 3. Price | Ask price, floor, and evidence per item | `references/pricing.md` |
| 4. Choose channel | Item to channel map | `references/channels-and-fees.md` |
| 5. Write listings | Copy-paste listing pack | `references/listing-templates.md` |
| 6. Draft in browser | Saved drafts on eBay/Vinted | `references/browser-automation.md` |
| 7. Local/colleague sale | Status sheet, sale page, posts | `references/sale-page-and-posts.md` |
| 8. After the sale | Shipping plan, buyer replies, support cases, tracker | `references/after-the-sale.md` |

## Mistakes from real sessions: don't repeat them

Each of these cost the person a correction, often several. They matter more than any technique below.

1. **A shallow first inventory.** The agent searched product keywords, covered electronics only, spot-checked one mailbox and one Amazon marketplace, and missed whole retailers (homeware, sports, Shopify brand stores). The person had to push six times, ending with "take as much time as you need, but list every single item from every single mailbox". Do the exhaustive sender-by-sender pass the first time, across every mailbox and every marketplace domain (.co.uk, .de, .in, .com and so on), every category except consumables. End with a coverage table (mailbox × sender × date range × pages read) so gaps are visible before the person finds them.
2. **"No result recorded" reported as "nothing there".** A search that ran with no logged outcome is not a confirmed empty. Re-run it or say it is unchecked.
3. **Guessing the pricing stance.** The agent first priced low, then got "don't underprice anywhere". Later it raised colleague prices to match public ones, and the person wanted them left alone because colleagues are a closed group. Ask the stance per channel (public vs friends/colleagues) before pricing, and never re-price one channel to match another without asking.
4. **Inferring state changes.** The agent assumed a reservation had fallen through and relisted an item on two pages. It also assumed which post was "round two". When a status or intent is ambiguous, ask one short question rather than editing several artifacts on a guess.
5. **Counts without contents.** "Found 41 more items, should I add them?" made the person ask "what are these 41 items?". Always show the list (grouped: sell / donate / keep / bin) with the count.
6. **Too much on the sale page.** Moving plans, destination and personal context went onto a page colleagues see, and the person asked to cut it. Buyer-facing pages carry item facts only, unless the person asks for more.
7. **The wrong browser.** The agent opened the built-in browser pane, which wasn't signed in, when the person had Vinted and eBay logged in in Chrome. Use the browser where the person is already signed in. Ask which one before starting.
8. **Trusting the person's hint over the records.** The person's recollection of which retailer an item came from turned out to be wrong. Use the hint as a lead, but confirm it in the mail.

## Tool roles (use whatever the host provides)

- **Mail reader**: Gmail connector, Outlook/Microsoft Graph connector, or a multi-account integration. People usually have 2 to 4 mailboxes, so expect to switch accounts or use more than one tool.
- **Sheet editor**: a Google Sheets connector that edits cells in place. A Drive-only connector can create files but not edit them, which forces a new file and a new link every time. Ask for the Sheets connector early.
- **Browser**: Claude in Chrome (uses the person's real logins) is the one that works for eBay and Vinted. A built-in browser pane is usually not signed in, and you must not type their password.
- **Local files**: a device or file connector to reach photos on their computer, and a shell with Python for the scripts in `scripts/`.
- **Web**: search and fetch for new prices, specs, dimensions, and platform rules.

Check what is connected before promising anything. If a tool is missing, say what it would unlock, then carry on with what you have (copy-paste packs always work).

## Stage 1. Build the inventory from email

Email order history is the most complete record of what someone owns, and it is full of traps. The approach that worked, after several shallow passes failed:

1. **Agree scope first**: time window (5 years is a good default, but check where the oldest mail is), exclusions (another country, clothing, consumables), and whose items count. Write the exclusions at the top of the inventory and keep to them, but flag high-value items an exclusion would drop (portable devices bought abroad often travelled with the person).
2. **Map every mailbox.** Confirm which account each connector is actually on (read the recipient address on results). Each mailbox has a footprint: one holds the marketplace account, another the direct-brand stores, an older one a previous country.
3. **Enumerate by sender and paginate to the end.** Do not rely on product-name searches; they return newsletters. Open every message whose subject doesn't name the item.
4. **Verify ownership** for every candidate: cancellations, returns, refunds, "return approved but never sent", gifts, items shipped to someone else, company property.
5. For a big sweep, **fan out parallel workers** (one per mailbox or retailer slice) with a shared brief and a "known items" list so they don't duplicate. Ask each to report per-sender page counts as proof of coverage.

Output: a master inventory (markdown, private) and a selection sheet with a blank `SELL?` column and a `Previously` column holding their last answers, so a regenerated sheet never makes them redo work. Expect blind spots (in-store, paper receipts, gifts, image-only receipts) and say so; invite them to walk the house and send photos.

## Stage 2. Photos

Photos reveal what email can't: extras worth money, flaws that must be disclosed, model numbers on labels. Convert HEIC, build contact sheets to review many at once, zoom on labels, and match to inventory rows. Before any photo leaves the machine, strip metadata and blur serials, personal photos, addresses on boxes, and drawer contents (`scripts/prepare_photos.py`).

## Stage 3. Price

- The strongest signal is **what it actually sold for recently**. eBay shows a "Recommended price" from recent sold items inside the listing form once category and condition are set, and Vinted shows a suggested range. Record both next to your price. They are often well below desk-research estimates; say so plainly.
- Know the ceiling: today's new price, discounts, and whether a re-release or successor caps the old model.
- Price for condition: unused/boxed is not "used". Extras in the photos raise the price.
- Ask the person's stance (speed vs "don't underprice anywhere") and record it. If they change their mind, keep a before/after table so they can see exactly what moved.
- Reserved and sold items keep the price agreed. Plan drops by date (hold, drop 10% on a date, take best offers in the final week).

## Stage 4 to 6. Channel, listing, drafts

- Electronics, cameras, drones, audio: eBay (and colleagues). Bags, shoes, sports kit, small games: Vinted. Bulky furniture, monitors, TVs: collection-only to colleagues or local. Low-value bits: bundle, donate, or skip.
- Write every listing as copy-paste blocks first. That file is useful even if the browser fails.
- In the browser, **save drafts only** (Vinted "Save draft", eBay "Save for later"). Verify fields by reading input values with JavaScript, not by trusting a screenshot. Publishing, sending messages to buyers, accepting offers and cancelling orders are commits: do them only on an explicit yes for that specific action, and expect the host's safety layer may still block the click. When blocked, hand over the exact one-click path instead of retrying.

## Stage 7. Colleague or friends sale

A sanitised status sheet (Item, Details, Condition, Price, Status, Collection, Notes) is the source of truth; a sale page with photos links to it; posts point to both. Strip order numbers, IMEIs, prices paid, personal notes, addresses and move details from anything buyer-facing.

## Stage 8. After the sale

Check the inbox for sold, offer, label and ship-by emails across all mailboxes. For each sale, update the sheet and page, end the listing everywhere else, then plan packaging (box size from product dimensions plus padding, weight vs label band), drop-off and deadline. Handle offers, wrong-item shipments, cancellations and support cases with the playbooks and message templates in `references/after-the-sale.md`. Keep `templates/tracker.csv` current.

## Guardrails (always on)

- **Ownership before listing.** Returned, refunded, cancelled, company-issued, gifted, partner's, landlord's or rented-flat fixtures: flag and hold until the person confirms. A partner's items need the partner's decision.
- **Disclose flaws** in the first lines: dead batteries, region plugs, wired-only, scuffs, missing parts, sizing quirks. Undisclosed flaws become "not as described" returns at the seller's cost.
- **No publishing, sending, buying, cancelling or accepting without an explicit yes** for that action. Drafts are fine.
- **One item, one live sale.** The moment something is reserved anywhere, end it everywhere else.
- **No personal data on public material**, including photo metadata, box labels and the eBay item location (default shows the full postcode; suggest the area only).
- **Platform facts change.** Fees, parcel limits, deadlines and legal rules in the references are dated. Re-check the official page before quoting a number to the person.
- **Report what changed** after every edit to their sheet, page or listings, in a short list, and say which file is the source of truth.

## Bundled resources

| File | Use |
|---|---|
| `references/inbox-search.md` | Mailbox mapping, query playbook, retailer quirks, ownership checks, fan-out brief |
| `references/photos.md` | HEIC, contact sheets, labels, privacy redaction |
| `references/pricing.md` | Evidence sources, heuristics, category gotchas |
| `references/channels-and-fees.md` | Where to sell, fees, buyer fees, tax and drone rules (dated) |
| `references/listing-templates.md` | Title rules, field-order templates, disclosures |
| `references/browser-automation.md` | Driving Vinted and eBay forms, uploads, failures and fixes |
| `references/sale-page-and-posts.md` | Status sheet, sale page, workplace and friend posts |
| `references/after-the-sale.md` | Inbox monitoring, offers, packaging and postage, order problems, support, message templates |
| `scripts/prepare_photos.py` | HEIC to JPEG, resize, strip metadata, blur boxes |
| `scripts/contact_sheet.py` | Labelled grids for reviewing many photos |
| `scripts/decode_raw_email.py` | Read a raw/HTML order email whose plain text omits the items |
| `scripts/net_proceeds.py` | What the seller nets and what the buyer pays, per platform |
| `scripts/parcel_fit.py` | Does an item fit a box, padding left, girth vs carrier limits |
| `templates/tracker.csv` | Inventory, listing and sale tracker columns |
