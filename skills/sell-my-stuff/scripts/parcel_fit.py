#!/usr/bin/env python3
"""Check whether an item fits a box, how much padding is left, and carrier limits.

Tries all orientations of the item inside the box, reports the best clearance,
then checks the packed parcel against common UK carrier limits (dated; see
references/channels-and-fees.md and re-check before relying on them).

Usage:
    python parcel_fit.py --item 31.1 23.5 18 --weight 2.9 --box 40 30 25
    python parcel_fit.py --item 33 25 20 --weight 2.2 --box 40 30 20 --box 40 30 25 --pad 3
Dimensions in cm, weight in kg (item only; box and padding are estimated).
"""
import argparse
from itertools import permutations

# Checked 2026-10-24 (Vinted help 1227). (name, max L, max W, max H or None, girth limit or None, max kg)
CARRIERS = [
    ("InPost locker/shop (Vinted standard)", 64, 41, 38, None, 2),
    ("Evri (Vinted standard)", None, None, None, 245, 2),
    ("Evri (Vinted heavy)", None, None, None, 245, 15),
    ("Royal Mail 2nd Class medium (Vinted)", 61, 46, 46, None, 2),
    ("Royal Mail medium, heavy (Vinted)", 61, 46, 46, None, 20),
]


def fit(item, box):
    best = None
    for o in permutations(item):
        gaps = [b - i for b, i in zip(sorted(box, reverse=True), o)]
        if min(gaps) >= 0 and (best is None or min(gaps) > min(best[1])):
            best = (o, gaps)
    return best


def box_weight(box):
    area = 2 * (box[0] * box[1] + box[1] * box[2] + box[0] * box[2]) / 10000  # m^2
    return round(area * 0.55 + 0.1, 2)  # single-wall board ~0.5 kg/m^2 plus tape and wrap


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--item", nargs=3, type=float, required=True, metavar=("L", "W", "H"))
    ap.add_argument("--weight", type=float, required=True)
    ap.add_argument("--box", nargs=3, type=float, action="append", required=True, metavar=("L", "W", "H"))
    ap.add_argument("--pad", type=float, default=3.0, help="minimum padding wanted per side, cm")
    a = ap.parse_args()
    for box in a.box:
        b = sorted(box, reverse=True)
        r = fit(a.item, b)
        print(f"\nBox {b[0]:g} x {b[1]:g} x {b[2]:g} cm")
        if not r:
            print("  Item does not fit in any orientation.")
            continue
        o, gaps = r
        per_side = [g / 2 for g in gaps]
        ok = "OK" if min(per_side) >= a.pad else f"TIGHT (< {a.pad:g} cm on a side)"
        print(f"  Item orientation {o[0]:g} x {o[1]:g} x {o[2]:g}; padding per side {', '.join(f'{p:.1f}' for p in per_side)} cm: {ok}")
        packed = round(a.weight + box_weight(b), 2)
        girth = b[0] + 2 * b[1] + 2 * b[2]
        print(f"  Packed weight about {packed} kg; L+2W+2H = {girth:g} cm")
        for name, L, W, H, g, kg in CARRIERS:
            dims_ok = (g is None or girth <= g) and (L is None or (b[0] <= L and b[1] <= W and b[2] <= H))
            print(f"    {'yes' if dims_ok and packed <= kg else 'no ':<4}{name} (max {kg} kg)")


if __name__ == "__main__":
    main()
