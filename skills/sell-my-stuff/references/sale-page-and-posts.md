# Status sheet, sale page and posts

For a colleague, friends or local sale. Three pieces, one source of truth.

## Status sheet (source of truth)

A spreadsheet, shared view-only, one row per item:

`Item | Details | Condition | Price GBP | Status | Collection | Notes`

- Status: Available, Reserved, Gone. People colour-code rows (for example yellow reserved, red gone). When editing, change values only and keep their formatting.
- Collection: "Office or home collect" vs "Home collect only" for bulky items. Say the area, never the street or postcode.
- **Build a clean buyer-facing sheet**; never share the working inventory. The working one has order numbers, IMEIs, prices paid, other people's names and private notes, and a shared link can't be unshared from people's history.
- **Edit in place** with a Sheets connector so the link never changes. A Drive-only connector can't write into an existing sheet: every change becomes a new file and a new link, and the person ends up marking an old copy. If stuck with Drive only, give a full CSV and these steps: open the sheet, click A1, File > Import > Upload > "Replace data at selected cell".
- The person must set sharing to "Anyone with the link, Viewer" themselves (connectors usually can't). Viewer, not Editor.
- Fix their typos in shared cells only with a find-and-replace they'd agree with, and say you did.

## Sale page

A published web page (artifact or similar) with photos, so buyers can browse without asking:
- Header: one line on why everything is going and the last day. No destination, no move date details beyond "by [date]", no postcode.
- Photo grid, highest price first: swipeable gallery per item, price sticker, condition chip, handover chip ("Can bring to the office" / "Collection only"), optional "Open to offers" chip, or "Best offer" instead of a price.
- "Also for sale" list for items without photos.
- "Reserved and sold" section at the bottom, so people don't chase gone items.
- Link to the status sheet.
- Embed photos as data URIs (resized to about 760 px, quality ~72, metadata stripped) so the page is self-contained; keep it under a few MB.
- Check it at phone width (no horizontal scroll) and desktop before publishing.
- Republish to the same URL for every change, so posted links keep working. Combining two people's sales onto one page worked well; keep a separate private page only if one person wants an item shown only to their audience.
- Pages start private: the person shares them from the page's Share menu.

## Posts

Workplace tools (and many chat apps) don't render markdown tables; pipes paste as raw characters. Use an emoji-led line list:

```
Moving sale: everything must go by [date] 📦

Photos, prices and condition: [PAGE LINK]
Live status: [SHEET LINK]

🚁 [Item], £[price], [one-line hook]
🎧 [Item], £[price], never used
🖥️ [Item], £[price], collection only

Open to offers on: [items]
Plus [small items] from £[x].

Comment or DM to claim. First come first served; I'll mark things Reserved in the sheet.
Most things can come to the office. [Bulky items] are collection only from [area].
```

Friend-posted version for a group the seller can't reach:

```
Posting for a friend: [area] moving sale, everything must go by [date]
A friend of mine is clearing their place. Photos, prices and condition: [PAGE LINK]
[3 to 6 highlights]
Handover in [central area]; [bulky items] collection only from [area].
Comment or message me and I'll put you in touch.
```

Rules that came from the person's feedback:
- Ask before mentioning relocation or destination; they cut it as "too much information".
- A repost round should list everything new since the last post the group actually saw, not since the last draft you wrote.
- When prices went up since an earlier post, "Open to offers" smooths it; decide the floor first.
- Note items that have gone so regulars don't ask.
- Workplace posts go stale in about 48 hours; one repost later in the campaign is enough.
