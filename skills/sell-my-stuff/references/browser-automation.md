# Driving Vinted and eBay in a browser

Save drafts only. Publishing, messaging buyers, accepting offers and cancelling orders are commits that need the person's explicit yes for that specific action. Even with a yes, the host's safety layer may block the click ("unrequested commit in a connected app"). If it does, don't retry or work around it: tell the person the exact one-click path (for example Vinted: Profile, Drafts, Finish editing, Upload; eBay: Seller Hub, Drafts, Resume draft, List it for free).

## Contents
1. Which browser
2. Session hygiene
3. Getting photos into the form
4. Filling fields reliably
5. Vinted form notes
6. eBay form notes
7. Verify, save, report

## 1. Which browser

- **Claude in Chrome** runs in the person's own Chrome with their logins. This is the one that works.
- A **built-in browser pane** usually isn't signed in. If the person is already logged in to eBay/Vinted in Chrome, go straight to Chrome. In a real session the agent tried the unsigned pane first, and the person had to ask "can you use Chrome directly?". Never enter passwords for them.
- If Chrome tools time out or say "extension disconnected", the computer is usually asleep or Chrome is closed. Say so in one line, save what you can, and list exactly what's left so "go" resumes it.

## 2. Session hygiene

- Read the tab list first and work in your own new tab.
- If your tab vanishes or unfamiliar tabs appear (another chat may be listing in the same window), **stop** and ask. Two agents filling forms at once creates duplicate listings.
- A "Leave site?" dialog blocks navigation when a form has unsaved changes. Save the draft first, or confirm the form is disposable before forcing navigation.

## 3. Getting photos into the form

- Upload with a file-upload tool against the hidden `input[type=file]` (find it by query "photo file input"). Never click the visible upload button; it opens a native picker you can't drive.
- Upload tools only accept files this session can read. Files on the person's computer must be staged into the session first (device connector: request folder access, then stage the specific files). Files you created in an outputs folder may also be rejected; copying them into the session's uploads area worked.
- Prepare photos first (metadata stripped, serials blurred), then upload those copies, not the originals.
- Upload all photos for a listing in one call. Wait a few seconds, then confirm the photo count on the page.

## 4. Filling fields reliably

- **Click by element reference, not by coordinates.** Dropdowns on both sites shift the page as they open; coordinate clicks landed on the wrong option (size 4 instead of 8; "New with tags" instead of "New without tags").
- Text inputs: click then type, or set the value directly with a form-input tool. Re-read the value afterwards. A dropped character from typing was caught this way once.
- Price fields sometimes don't keep typed values; set them with the form-input tool and re-read.
- After every few fields, read all inputs back with JavaScript and compare with the plan:

```js
[...document.querySelectorAll('input,textarea,select')]
  .filter(e => !['hidden','file'].includes(e.type))
  .map(e => (e.name||e.id||e.placeholder) + ' = ' +
    ((e.type==='radio'||e.type==='checkbox') ? e.checked : String(e.value).slice(0,60)))
  .filter(s => !/= $|= false$/.test(s))
```

- Batch actions (click, type, wait, screenshot) to save round trips.
- Dismiss cookie, tips and rating pop-ups when they cover the form.

## 5. Vinted form notes (`https://www.vinted.co.uk/items/new`)

- Vinted suggests category and brand from the title and photos. Check both: it guessed the brand as the marketplace the item was bought from once, and picked a near-miss brand for a kitchen gadget.
- Brands not in its list: search the brand, then choose "Use '[typed]' as brand". This sometimes ends up as "List without brand"; acceptable if the description names the brand.
- Size: Vinted asks for the label size. Put the conversion (shoe size equivalence) in title and description.
- Condition is a radio list inside a dropdown: open it, find the radio by its label, click by reference, then re-read.
- Colour and material are optional; skip them if the dropdown keeps jumping the page. Clear wrong auto-filled material.
- Parcel size: the form pre-selects one from the category; set it from the packed size and weight.
- **Save draft** returns you to the profile; the draft shows with 0 views and is not public.

## 6. eBay form notes (start at `https://www.ebay.co.uk/sl/prelist/suggest`)

- Search the model or ISBN. Catalogue matches pull in specs and stock data: only pick one that matches the exact variant. A wrong variant (a "Combo" bundle, a successor model, a different part number) imports wrong specs. Otherwise "Continue without match".
- Books: searching the ISBN finds the catalogue entry and fills title, author and specifics.
- Pick condition on the next step, then continue; eBay creates a draft immediately (`lstng?draftId=...`).
- **Description editor** is a contenteditable inside an iframe titled "Description". Clicking and typing often misses because the page scrolls. What worked: focus it with JavaScript, select its contents, then type:

```js
const f=[...document.querySelectorAll('iframe')].find(fr=>fr.title==='Description');
const d=f.contentDocument; const ed=d.querySelector('[contenteditable=true]')||d.body;
f.scrollIntoView({block:'center'}); f.contentWindow.focus(); ed.focus();
const r=d.createRange(); r.selectNodeContents(ed);
const s=f.contentWindow.getSelection(); s.removeAllRanges(); s.addRange(r);
```
  Setting the HTML-view textarea with a form tool did not stick. Verify by reading the iframe body's `innerText` length.
- Item specifics: use eBay's suggested buttons for Brand and Model when correct. Required ones (Brand, Type, Model, Connectivity; furniture height, length and width) block publishing if empty. **Clear auto-filled values you can't verify** (it added a surround format, impedance and wattage to a speaker, and a wrong material to a shower head).
- Price: set the item price, then turn on offers and set the minimum offer (auto-decline). Record the "Recommended price" shown.
- Delivery: choose collection only for bulky items; set a realistic parcel weight band rather than trusting eBay's estimate.
- **Item location** defaults to the full home postcode on every listing. Suggest the person change it to the area only.
- eBay won't let you reuse other sellers' catalogue photos for used items; books still need one real photo.
- **Save for later** goes to Seller Hub drafts.

## 7. Verify, save, report

Before saving, run the field read-back. After saving, open the drafts list and confirm each one is there. Then report a table: item, channel, price, floor, the platform's suggested price, and anything that blocks publishing (missing size, dimensions, photo). Offer to publish on a yes, and expect you may have to hand that click back.
