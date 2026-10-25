# After the sale: offers, shipping, problems, support, tracking

## Contents
1. Inbox check for sales and offers
2. Keeping channels in sync
3. Offers
4. Packaging, box sizes and postage
5. Before handing over: resets
6. Order problems (wrong item sent, cancellations, late labels)
7. Contacting platform support
8. Message templates
9. Tracker

## 1. Inbox check

Run across **every** mailbox the marketplace accounts use (a multi-account mail tool helps):
```
(from:vinted OR from:ebay) newer_than:7d
from:vinted ("Order update" OR "time to ship" OR "offer" OR "cancel")
from:evri OR from:inpost OR from:royalmail newer_than:7d      # drop-off and tracking confirmations
```
Read each sale email for: item, sale price, buyer handle (keep private), carrier, ship-by deadline, whether a label exists yet, the package size or weight band on the label, and any cancellation or offer. Marketing "your item was favourited" mails can be skipped.

Summarise as a table: item | sold for | carrier | ship by | label? | pack in. Then list the urgent items first ("label not generated yet", "eBay already marked dispatched but it's still at home", "label is a 1 kg band, weigh it").

Offer to repeat this daily if the host supports scheduled tasks.

## 2. Keeping channels in sync

Whenever anything is reserved or sold anywhere: update the status sheet, update the sale page, end or delete the listing on every other channel, and tell the person which listings they need to end if you can't. Double-selling is the main way a clear-out goes wrong.

## 3. Offers

- Vinted buyers offer low and repeatedly; each offer email shows the offer and the list price. Summarise all open offers per item with the best one, and the time since.
- eBay offers below the auto-decline floor never reach the person.
- Accepting or countering is the person's call. Give a recommendation tied to their deadline and floor.

## 4. Packaging, box sizes and postage

Method that worked:
1. Get product dimensions and weight from the retailer or manufacturer spec page (search "[model] dimensions weight"). If two sources disagree, assume the heavier.
2. Add padding: about 3 to 5 cm each side for fragile items. Check the item can lie in its longest orientation.
3. Choose a stock box size, give one fallback, and compute packed weight (item + box ~0.3 to 0.6 kg + padding).
4. Check against the label's limits: weight band on the label, and the carrier's size rule (Evri uses length + 2 x width + 2 x height, see `channels-and-fees.md`). Run `scripts/parcel_fit.py`.
5. If over the label's band, change the parcel size before drop-off (Vinted lets you change size at the drop-off point in many cases; check the current help article).
6. Produce one shopping list (boxes by size and count, mailing bags, padded envelopes, bubble wrap, tape) and where to buy locally: a pack-and-ship shop sells single boxes in exact sizes; stationery and discount stores have envelopes and bags; big retailers sell multipacks of moving boxes; post offices have padded envelopes.

Typical fits:
| Item | Pack in |
|---|---|
| Card game, book, small flat item | Padded envelope (about 22 x 26 cm) |
| Soft backpack or clothing | Large grey mailing bag (about 60 x 75 cm), no box |
| Pair of skates or boots, small heater | Box about 40 x 30 x 25 cm |
| Smart speaker, small electronics | Box about 25 x 20 x 20 cm plus wrap |

Category packing tips: wrap skate blades in cardboard or guards so they don't cut the box; stuff boots to keep shape; unclip stands and wrap cables; never post swollen lithium batteries; fill voids so nothing moves.

## 5. Before handing over: resets

Factory reset and remove from the owner's account: phones and tablets (sign out of iCloud/Find My or Google first), smart speakers (for example a speaker reset by holding the connect button while powering on until the light flashes, then remove the "not connected" device from the app), streaming sticks, cameras with app pairing, smart watches. Wipe computers. Say so in the listing only once it's done.

## 6. Order problems

**Wrong item sent in a parcel**
1. Find the drop-off confirmation email: shop, time and tracking.
2. The best interception point is the parcel shop before the courier's collection (often once a day). The person can ask the shop for it back with the drop-off email; it's at the shop's discretion. Once in the network, couriers generally won't stop it.
3. If interception fails: message the buyer before delivery, apologise, explain, and ask them **not to confirm the order as received** (confirming releases payment and closes the order), and say all postage will be covered.
4. Open a platform support request on that order (section 7).
5. Vinted's process (as its assistant described it): the buyer reports the wrong item from the order conversation, which suspends the order; the item comes back; the seller cancels so the buyer is refunded; the seller relists the correct item and the buyer buys it again, creating a fresh label. The old label can't be reused for a different parcel.
6. Handle the other affected order separately (if its buyer asked to cancel, accepting is cleanest; reason "Agreed with the buyer").

**Buyer asks to cancel**: accepting their request is usually fine. A seller-initiated cancellation can attract a negative review; pick the accurate reason.

**No label yet**: on Vinted the seller generates it from the buyer conversation; there's a deadline from the sale (see `channels-and-fees.md`). Do it the same day.

**eBay shows dispatched but it isn't**: post it immediately and check the label's weight band.

## 7. Contacting platform support

Vinted (logged in): order conversation > order details > Help, or Help Centre > "I need help with a specific order" > choose the order > pick the closest topic > search the issue > "No" on "Was this helpful?" or open a topic article > "Contact us" opens a ticket form with the order prefilled (up to 5 photos). Submitting starts a support conversation in the inbox; an automated assistant often replies first with the process.

eBay: Help & Contact from the order in Purchase/Sold history, choose the issue, then the contact option offered.

Support messages work best with: order reference, item, what happened with date and time, tracking, drop-off location, what you're asking for (numbered), and a note that the buyer has been told. Keep personal details out of anything public; a support ticket is private, but include only what's needed.

## 8. Message templates

Wrong item, to buyer:
> Hi, I'm really sorry, I made a packing mistake. The parcel on its way to you contains [wrong item] instead of [item]. The [item] is still with me. I'm sorting it out with [platform] support now. Please don't confirm the order as received when the parcel arrives, so you stay fully covered. I'll pay all postage to get the [item] to you and the other item back to me. Apologies again for the hassle.

Wrong item, to support:
> Hello, I made a packing error on order [ref] ([item]). On [date] at [time] I dropped off a parcel at [drop-off point] using this order's label (tracking [tracking]). It contains the wrong item: [wrong item] from a separate listing ([other ref]). The [item] is still with me and I've told the buyer.
> Could you please: 1) stop or redirect the parcel back to me if possible; 2) otherwise provide a return label for [wrong item] and a new label so I can send the [item]; 3) keep this order open and protected for the buyer until they receive the correct item.
> Thank you.

Offer reply (counter):
> Thanks for the offer. The lowest I can do is £[x], which includes [extras]. Happy to accept at that.

Collection arrangement:
> It's yours at £[x]. I can bring it to [office/area] on [day], or you can collect from [area] [times]. Payment by [method] on handover.

Reserved item fell through:
> No problem, thanks for letting me know. I'll put it back on the list.

## 9. Tracker

Keep `templates/tracker.csv` (or a sheet with the same columns) as the record of what sold where and for how much:
`item, owner, channel, listing_status, list_price, floor, platform_suggested, status, sold_price, buyer_ref, sold_date, ship_by, carrier, label_ready, box, shipped_date, paid_out, notes`

Report totals by owner and channel when asked "what has sold".
