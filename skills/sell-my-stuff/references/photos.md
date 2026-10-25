# Photos: getting them, identifying items, preparing them

## Getting the files

- **Cloud folder** (Drive etc.): large binary downloads often don't come back inline; the tool saves a JSON payload (base64 `content`) to disk. Decode it in code. Never print base64 into the conversation. Process in batches (about 10 per worker) for dozens of photos. Files over the connector's size limit (videos) won't download; ask for a photo instead, or reach the file locally.
- **Local folder** via a device/file connector: request access to the folder, list it, then *stage* the files into the session before anything else can read them. Browser upload tools only accept files the session can read (see `browser-automation.md`).
- **Videos**: if `ffmpeg` is available, extract a frame every 2 seconds (`ffmpeg -i in.MOV -vf "fps=1/2,scale=480:-2" out_%02d.jpg`) to identify the item. Check frames for personal contents before using any.

## Identify and match

1. Convert HEIC and resize: `python scripts/prepare_photos.py raw/ jpg/ --max 1200`.
2. Build contact sheets to see 9 to 12 at once: `python scripts/contact_sheet.py jpg/ sheets/ --per 12 --cols 4 --tile 360`. Each tile is labelled with the file number so you can refer back.
3. Crop and zoom on labels for model numbers, sizes, switch types, weights (glove oz, fin size, shoe size), and serials (to blur, not to publish).
4. Match each photo to an inventory row. Note what the photos add:
   - **Extras** (grips, tripods, spare lenses, cases) that raise the price.
   - **Flaws** (scuffs on a base rim, worn soles) that must be disclosed and shown.
   - **Unknown items** with no email trail; price them from the photo and add them.
5. Ask for the facts photos can't show: size labels, battery health, how many batteries, whether wireless still works.

## Privacy redaction before anything is shared

Phone photos carry GPS coordinates. Marketplaces usually strip EXIF, but self-hosted pages and shared folders don't. Re-encode every image without metadata:

```
python scripts/prepare_photos.py raw/ out/ --max 1600 --quality 85 \
  --blur IMG_0001:290,735,665,840 --only IMG_0001 IMG_0002
```

Blur boxes use a 900x1200 (portrait) or 1200x900 (landscape) reference frame and are scaled to the real image. Always crop and look at a blurred area afterwards to confirm it is unreadable.

Blur or drop:
- Serial numbers, IMEIs, MAC addresses on labels.
- Framed personal photos, documents, mail on shelves.
- Delivery labels on boxes (name, address, tracking).
- Drawer and cupboard contents.
- Anything showing the home's location from a window.

## Photo plan per listing

Main shot on a plain background in daylight; all included accessories laid out; close-ups of any flaw; label or model plate (serial blurred); for clothing and shoes, the size label and soles; for electronics, powered on if possible. Keep a table of photo numbers per listing and a list of items still needing photos.
