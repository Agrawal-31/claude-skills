#!/usr/bin/env python3
"""Build labelled contact sheets so many photos can be reviewed at once.

Each tile is labelled with the file stem's trailing number (IMG_0012 -> 0012),
so you can refer back to individual files.

Usage:
    python contact_sheet.py PHOTOS_DIR OUT_DIR [--per 9] [--cols 3] [--tile 420]

Requires: pip install pillow (and pillow-heif for HEIC input)
"""
import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

EXTS = {".heic", ".heif", ".jpg", ".jpeg", ".png", ".webp"}


def label(stem):
    m = re.search(r"(\d+)$", stem)
    return m.group(1) if m else stem[:12]


def font(size):
    for f in ("DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--per", type=int, default=9)
    ap.add_argument("--cols", type=int, default=3)
    ap.add_argument("--tile", type=int, default=420)
    a = ap.parse_args()

    files = sorted(p for p in Path(a.src).iterdir() if p.suffix.lower() in EXTS)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    f = font(max(14, a.tile // 15))
    for i in range(0, len(files), a.per):
        chunk = files[i:i + a.per]
        rows = (len(chunk) + a.cols - 1) // a.cols
        sheet = Image.new("RGB", (a.cols * a.tile, rows * a.tile), "white")
        d = ImageDraw.Draw(sheet)
        for j, p in enumerate(chunk):
            im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
            im.thumbnail((a.tile - 8, a.tile - 8))
            x, y = (j % a.cols) * a.tile, (j // a.cols) * a.tile
            sheet.paste(im, (x + (a.tile - im.width) // 2, y + (a.tile - im.height) // 2))
            d.rectangle([x + 4, y + 4, x + a.tile // 3, y + a.tile // 10], fill="black")
            d.text((x + 8, y + 6), label(p.stem), fill="yellow", font=f)
        name = out / f"sheet{i // a.per + 1}.jpg"
        sheet.save(name, quality=82)
        print(name, [label(p.stem) for p in chunk])


if __name__ == "__main__":
    main()
