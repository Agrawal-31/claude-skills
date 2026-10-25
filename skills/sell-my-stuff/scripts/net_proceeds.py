#!/usr/bin/env python3
"""What a UK private seller nets, and roughly what the buyer pays, per channel.

FEE TABLE IS DATED (checked 24 Oct 2026). Re-check the official pages listed
in references/channels-and-fees.md and edit FEES below if anything changed.

Usage:
    python net_proceeds.py 120                      # all channels for a £120 sale
    python net_proceeds.py 120 --postage 3.50 --channel ebay --international
    python net_proceeds.py 40 --cost-box 1.20       # subtract your packaging cost
"""
import argparse

FEES = {
    "checked": "2026-10-24",
    # eBay UK private sellers: no final value fee (excl. Motors); 3% if buyer is outside the UK.
    "ebay_seller_pct": 0.0,
    "ebay_international_pct": 0.03,
    # eBay buyer protection fee on private sellers' items (reported Feb 2025 rollout; verify).
    "ebay_buyer_flat": 0.75,
    "ebay_buyer_tiers": [(300.0, 0.04), (4000.0, 0.02)],
    # Vinted UK: no seller fee; buyer fee published as 3-8% + £0.30-£0.80.
    "vinted_buyer_low": (0.03, 0.30),
    "vinted_buyer_high": (0.08, 0.80),
}


def ebay_buyer_fee(price):
    fee, lower = FEES["ebay_buyer_flat"], 0.0
    for upper, pct in FEES["ebay_buyer_tiers"]:
        portion = max(0.0, min(price, upper) - lower)
        fee += portion * pct
        lower = upper
    return fee


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("price", type=float, help="item sale price in GBP")
    ap.add_argument("--postage", type=float, default=0.0, help="postage the buyer pays (passed through)")
    ap.add_argument("--cost-box", type=float, default=0.0, help="your packaging cost")
    ap.add_argument("--channel", choices=["ebay", "vinted", "direct", "all"], default="all")
    ap.add_argument("--international", action="store_true", help="eBay buyer outside the UK")
    a = ap.parse_args()
    p = a.price
    print(f"Fee table checked {FEES['checked']}. Re-verify before quoting.\n")
    rows = []
    if a.channel in ("ebay", "all"):
        intl = (p + a.postage) * FEES["ebay_international_pct"] if a.international else 0.0
        net = p - p * FEES["ebay_seller_pct"] - intl - a.cost_box
        rows.append(("eBay", net, f"£{p + ebay_buyer_fee(p) + a.postage:.2f}"))
    if a.channel in ("vinted", "all"):
        lo = p * FEES["vinted_buyer_low"][0] + FEES["vinted_buyer_low"][1]
        hi = p * FEES["vinted_buyer_high"][0] + FEES["vinted_buyer_high"][1]
        rows.append(("Vinted", p - a.cost_box, f"£{p + lo + a.postage:.2f} to £{p + hi + a.postage:.2f}"))
    if a.channel in ("direct", "all"):
        rows.append(("Colleagues/local", p - a.cost_box, f"£{p:.2f}"))
    print(f"{'Channel':<18}{'You net':>10}   Buyer pays (incl. postage)")
    for name, net, buyer in rows:
        print(f"{name:<18}{'£%.2f' % net:>10}   {buyer}")


if __name__ == "__main__":
    main()
