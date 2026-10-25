# Listing templates

Write every listing as a copy-paste block first, in the order the app asks for fields. This pack is the fallback when browser automation fails, and the person can list from a phone with it open.

## Title rules

- eBay: up to 80 characters. Vinted: keep it short and searchable.
- Lead with brand and model, then the spec buyers filter on (size, capacity, switch type, dimensions), then the strongest condition phrase ("Never Used", "Flown Under 5 Times", "Boxed").
- Include the numbers people search: "40x20x25" for cabin bags, shoe size and manufacturer size, model numbers that distinguish variants (an ANC vs non-ANC part number).
- State limitations that change the product: "Wired", "US Plug + UK Adapter".
- Count characters before pasting.

## Description rules

- First line: what it is and its condition in plain words.
- Second: anything a buyer could return it for (faults, missing parts, region, sizing quirk). Disclosure here is cheaper than a "not as described" case.
- Then what's included, a few key specs, new price if it helps ("£60 new"), and handover or postage.
- No personal details (move dates, destinations, family names, home postcode). "Smoke-free home" is optional filler; drop it if the person dislikes it.
- Use square brackets for facts only the person knows, and never publish with brackets left in.

## eBay block

```
## [Item]
Title (<= 80 chars):
[title]

Category to search: [e.g. Cameras & Photography > Drones]
Catalogue match: [use / continue without match, and why]
Condition: [New / Opened - never used / Used / For parts]
Format: Buy It Now, offers on
Price: £[ask]   Auto-decline below: £[floor]   (Auto-accept: £[optional])
eBay recommended price seen: £[x]
Postage: [tracked small parcel / collection only]   Item location: [area only]
Required item specifics: Brand: … Model: … MPN: … Type: … Connectivity: … [dimensions for furniture]
Photos in order: [main, accessories, close-up of flaw, label]
Must be in the box: [PSU, cables, remote]
Must disclose: [fault, region plug, sizing]
Description:
[text]
```

## Vinted block

```
## [Item]
Title:
[title]
Description:
[text]
Category: [Vinted usually suggests one from the title; check it]
Brand: [exact brand, or "Use [typed] as brand", or "List without brand"]
Size: [the label size Vinted asks for; explain shoe-size equivalence in the description]
Condition: [New with tags / New without tags / Very good / Good / Satisfactory]
Colour (optional, up to 2): [ ]   Material (optional): [ ]
Price: £[list]   Lowest offer to accept: £[floor]
Parcel size: [Small / Medium / Large], packed weight about [x] kg
Photos in order: [ ]
```

## Colleague / friends sheet row

`Item | Details | Condition | Price GBP | Status | Collection | Notes`

Condition vocabulary that people understood: Unused, Like new boxed, Very good, Good. Status: Available, Reserved, Gone. Notes can carry "Open to offers" or "Best offer" (no price).

## Disclosure checklist

- Batteries: holds charge? how many? swollen? (swollen lithium: do not post)
- Wireless still works? (if not: "wired only")
- Region: plug type, warranty validity, language
- Sizing: manufacturer size vs UK size
- Cosmetic marks: where, and photographed
- Accessories: what's in, what's missing
- Account locks removed (phones, speakers, streaming sticks)
- Previously returned or repaired
