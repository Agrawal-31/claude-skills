# Inbox search playbook

Goal: a complete, honest list of what the person owns and could sell. Completeness comes from method, not clever keywords. In the session this skill came from, the first five passes each missed things; what finally worked was sender enumeration with full pagination, opening every unnamed message, and a separate verification pass.

## Contents
1. Scope
2. Map every mailbox
3. Sweep method
4. Query cookbook (Gmail and Outlook)
5. Retailer and sender quirks
6. Ownership verification
7. Blind spots and how to close them
8. Fan-out brief for parallel workers
9. Output format

## 1. Scope

Agree before searching:
- **Window.** Default 5 years. Find the oldest mail first (`before:YYYY/01/01`, stepping back) so you know what the mailbox can and can't show.
- **Exclusions.** Common: items in another country, clothing, consumables, food, digital goods, services. Write them at the top of the inventory.
- **Whose items.** Partner's and household items need that person's decision; keep them on a separate private sheet.
- **Deadline.** A move-out date drives the order of work (bulky items first, they need collection).

Exclusions are blunt. When one would drop a valuable portable item (a laptop or watch bought abroad that may have travelled with them), list it once in a "check" section rather than silently dropping it. Ask once, accept the answer, don't re-raise it.

## 2. Map every mailbox

- Ask which addresses exist, including old ones and a partner's if relevant. Sweep **every** one.
- **Confirm the connected account** on each run by reading the recipient address in results. Connectors get switched between accounts by the person; a "no results" can mean "wrong mailbox".
- Note each mailbox's footprint, e.g. "marketplace account lives here", "direct-brand stores here", "previous country here". Marketplace orders only appear in the mailbox registered to that marketplace account.
- Note delivery addresses per era. They tell you which home an item went to (and so whether it's still there), and whether it went to someone else.

## 3. Sweep method

1. **Enumerate transactional senders**: run broad order-subject queries per year, collect distinct sender domains, then query each sender and paginate to the last page.
2. **Open every message whose subject doesn't name the item** ("Your order", "Ordered: 1 item", "Thanks for your purchase").
3. **Read the right part.** If the plain-text body lacks line items, fetch the full/raw message and decode the HTML (`scripts/decode_raw_email.py`). PDF receipts: fetch the attachment (raw MIME) and run `pdftotext`.
4. **Exclude noise senders** explicitly (newsletters, crypto, ride-hailing, food delivery) so they stop drowning results.
5. **Record coverage** (sender, pages, messages) so "complete" is provable, and so a follow-up pass knows what was done.
6. **Search by order number** to find the matching cancellation, return or refund email, because those often name only the order number.
7. **Search by the person's hints, but treat hints as leads.** "I bought it from store X" was wrong once; the receipt was from store Y, found via a phrase from the actual email ("Your items were picked up").

## 4. Query cookbook

Gmail (connector `search_threads` / `get_message` / `get_thread`):
```
in:anywhere subject:(order OR receipt OR invoice OR dispatched OR shipped OR delivered) after:2021/01/01 before:2023/01/01 -from:(newsletter-domain.com OR other-noise.com)
from:(auto-confirm@amazon.co.uk OR auto-confirm@amazon.de OR order-update@amazon.in OR auto-confirm@amazon.com)
from:shopifyemail.com OR from:t.shopifyemail.com          # direct-brand stores
(cancelled OR refund OR "return") "<order number>"
category:purchases                                          # partial only; misses older mail
"<phrase from the email body>" in:anywhere                  # e.g. "items were picked up"
(brand OR model) (order OR receipt OR invoice) -from:<brand marketing domain>
```
- Brand-name searches alone return marketing. Always pair with order words and exclude the brand's marketing domain.
- `category:purchases` was only partly reliable and didn't reach older years.
- Use `includeTrash` / `in:anywhere`; receipts get archived or deleted.

Outlook / Microsoft Graph (`list-mail-messages`):
- `$search` uses KQL and must be double-quoted: `"from:auto-confirm@amazon.co.uk"`. Don't combine `$filter` with `$search`.
- Date windows: `$filter=receivedDateTime ge 2023-10-01T00:00:00Z and receivedDateTime lt 2023-11-20T00:00:00Z`, `$orderby=receivedDateTime desc`.
- Paginate with the skip token until it stops.

Multi-account integrations (for example a Gmail tool that takes an account parameter) let one query run against several mailboxes; good for the after-sale inbox check.

## 5. Retailer and sender quirks

| Pattern | What happens | Fix |
|---|---|---|
| Marketplace subjects like "Ordered: 1 item", "Your order." | Item hidden | Open every one |
| Dispatch email with no confirmation | ~20+ orders only had dispatch mail | Treat dispatch, delivery and review-request emails as order evidence |
| Cancellation names only the order number | Cancelled duplicate looks owned | Search the order number |
| Several country stores (.co.uk, .de, .com, .in) | Item bought abroad missed | Query each sender domain |
| "Customers also bought" / recommendation footers | Look like purchases | Ignore unless an order number is attached |
| Direct-brand Shopify stores | Anonymous `store+NNN@t.shopifyemail.com` sender, brand only in body | Enumerate the Shopify sender |
| ERP-sent receipts (e.g. NetSuite) | Sender isn't the brand | Search the order format, not the sender |
| In-store purchases | Paper receipt only | Loyalty-points and "how was your purchase" survey emails prove a purchase; the store account's purchase history names the items |
| PDF-only receipts (Apple retail, furniture stores, jewellers, fashion chains) | Body empty | Fetch the attachment, `pdftotext` |
| Image-only line items (some discount marketplaces) | Names only in product images | Ask the person to check the app's order history |
| Package forwarding services | Contents not itemised | Find the original retailer order in the date window; forwarding dates can be months off |
| Order confirmation vs pickup receipt | Confirmation price was pre-discount | Use the final receipt for price paid |
| Beauty or consumable retailers | Durable devices hidden among liquids (a shower filter head was missed this way) | Judge each line, not each retailer |
| Books, study texts, games | Wrongly filed as consumables | Keep in scope; they sell in niche groups |
| Mixed household purchasing | Partner's order on your account, yours on theirs | Note "bought on X's account, may be Y's" |

## 6. Ownership verification

For every candidate, look for and record:
- **Cancelled** (including payment declined, out of stock, cancelled minutes after ordering).
- **Returned and refunded.** A return *request* or *approval* is not a return: look for the refund or credit note. "Return approved, never sent back" means they still own it.
- **Duplicates**: two orders the same day may be one cancelled and one kept.
- **Gift / shipped elsewhere**: delivery name or address differs.
- **Company property**: work-issued laptops and phones are not theirs to sell even if they're in the flat. Check for offboarding threads.
- **Open claims**: an item with an open warranty or complaint (wrong finish delivered, replacement pending) should be held; settling first is usually worth more.
- **Rented-flat fixtures** (taps, shower hoses, filters fitted to the property) and anything on a landlord's inventory.
- **Personalised or engraved** items: lower resale; some (engagement jewellery) shouldn't go on a sale list at all. Leave sensitive items off and mention them privately.

Raise a mismatch once, plainly: "Email shows this was refunded on [date]. If this is a different unit, ignore this."

## 7. Blind spots

Say these out loud so the person knows the list isn't the house:
- In-store and cash purchases, gifts, hand-me-downs.
- Purchases on another person's account or an unconnected mailbox.
- Image-only or app-only receipts.

Ways to close them: the person walks the house and sends a photo batch (price from photos, see `photos.md`); store account order histories; card statements for unexplained amounts. When something has no email trail at all, say so and stop searching.

## 8. Fan-out brief for parallel workers

When a sweep is big, split by mailbox or slice (marketplace all-time; non-marketplace retailers; beauty/consumable shops; pre-window years; unresolved unknowns; sender census). Write one brief file every worker reads first:

```
# Sweep brief
Mailbox: <address> (verify on every result)
Window: <dates>   Exclusions: <list>
Known items (do not report again): see known_items.txt
Known failure modes: consumable-shop durables, approved-but-unsent returns, books, image-only receipts, cancellations naming only order numbers
For each item report: name | spec/size/colour | price paid | date | retailer | order ref | delivered to (area only) | status Owned/Returned/Cancelled/Unclear | evidence (message ids)
Coverage table: query | pages | messages
Privacy: skip underwear, health and intimate items (count only). Don't copy addresses or card numbers into reports.
Write results to <slice>.md
```

Then merge, dedupe against the existing sheet, and present new finds grouped as Sell / Keep / Donate / Bin for the person to pick, rather than adding everything.

## 9. Output format

**Master inventory (private markdown)**: scope and exclusions at top, mailbox coverage table, then tiers by value:

| Item | Spec | Paid | Bought | Source / order ref | Delivered to | Status | Flags |
|---|---|---|---|---|---|---|---|

Sections: Tier 1 (high value), Tier 2, small items, Do not sell (returned, cancelled, not theirs), To check (unidentified purchases with "where to look").

**Selection sheet** (spreadsheet): `SELL? | Previously | Group | Item | Spec | Paid | Bought | Source | Est low | Est high | Suggested ask | Notes`. Leave `SELL?` blank. Read their marks back via a CSV export or the Sheets connector. People also mark by cell colour (for example "yellow means boxed, red means unused, pink means sell"): read `userEnteredFormat.backgroundColor` through the Sheets API, or export as xlsx and read fills with openpyxl. If the sheet seems unchanged after "I updated it", check whether they edited an older copy before assuming anything.
