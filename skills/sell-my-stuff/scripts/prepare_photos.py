#!/usr/bin/env python3
"""Prepare photos for listings or a sale page.

Converts HEIC/HEIF (and any Pillow-readable image) to JPEG, applies EXIF
rotation, resizes so the long edge is at most --max pixels, optionally blurs
rectangles (serial numbers, personal photos, address labels), and saves
WITHOUT metadata, so phone GPS coordinates are dropped.

--blur takes STEM:x0,y0,x1,y1 in a 900x1200 (portrait) or 1200x900 (landscape)
reference frame; boxes are scaled to the real image size. Repeat for more boxes.
Always crop and look at a blurred area afterwards to confirm it is unreadable.

Usage:
    python prepare_photos.py SRC_DIR_OR_FILE OUT_DIR [--max 1600] [--quality 85]
        [--blur IMG_0001:290,735,665,840] [--radius 18] [--only IMG_0001 IMG_0002]

Requires: pip install pillow pillow-heif
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:  # HEIC input will fail with a clear message below
    pass

EXTS = {".heic", ".heif", ".jpg", ".jpeg", ".png", ".webp"}


def parse_blurs(specs):
    boxes = defaultdict(list)
    for spec in specs or []:
        name, coords = spec.split(":", 1)
        vals = [float(v) for v in coords.split(",")]
        if len(vals) != 4:
            raise SystemExit(f"bad --blur {spec!r}: need x0,y0,x1,y1")
        boxes[Path(name).stem].append(tuple(vals))
    return boxes


def process(path, out_dir, args, boxes):
    try:
        im = Image.open(path)
    except Exception as e:  # noqa: BLE001
        print(f"skip {path.name}: {e} (install pillow-heif for HEIC)", file=sys.stderr)
        return
    im = ImageOps.exif_transpose(im).convert("RGB")
    w, h = im.size
    ref_w, ref_h = (900, 1200) if h >= w else (1200, 900)
    n = 0
    for x0, y0, x1, y1 in boxes.get(path.stem, []):
        sx, sy = w / ref_w, h / ref_h
        box = (int(x0 * sx), int(y0 * sy), int(x1 * sx), int(y1 * sy))
        region = im.crop(box).filter(ImageFilter.GaussianBlur(args.radius * max(sx, sy)))
        im.paste(region, box)
        n += 1
    im.thumbnail((args.max, args.max), Image.LANCZOS)
    out = out_dir / (path.stem + ".jpg")
    im.save(out, "JPEG", quality=args.quality, optimize=True, progressive=True)  # no exif passed
    print(f"{out} {im.size[0]}x{im.size[1]}" + (f" blurred {n} box(es)" if n else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--max", type=int, default=1600)
    ap.add_argument("--quality", type=int, default=85)
    ap.add_argument("--radius", type=float, default=18)
    ap.add_argument("--blur", action="append")
    ap.add_argument("--only", nargs="*", help="process only these file stems")
    args = ap.parse_args()

    src = Path(args.src)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    files = [src] if src.is_file() else sorted(p for p in src.iterdir() if p.suffix.lower() in EXTS)
    if args.only:
        wanted = {Path(s).stem for s in args.only}
        files = [p for p in files if p.stem in wanted]
    boxes = parse_blurs(args.blur)
    for p in files:
        process(p, out_dir, args, boxes)


if __name__ == "__main__":
    main()
