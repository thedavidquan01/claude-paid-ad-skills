#!/usr/bin/env python3
"""Monday read: judge each ad on CAC with the 2x, 5x, and 10x rules.

Usage:
  python3 monday_read.py export.csv --target-cac 100 [--near 1.25]

The CSV needs one row per ad (or per ad and day) with the ad name, spend,
and conversions since the ad launched. Campaign name is optional. A campaign
whose name contains SCALE marks a scaling copy. Ad names that follow
DATE_BRIEF-VARIANT_TOPIC-ANGLE_PERSONA_STAGE_LEVER_FORMAT are split into
their parts. Uses only the Python standard library.

It never reads clicks, CTR, or hook rate. Judge on CAC, not clicks.
"""
import argparse
import csv
import sys
from collections import OrderedDict

ALIASES = {
    "ad": ["ad name", "ad", "creative name", "name"],
    "campaign": ["campaign name", "campaign"],
    "spend": ["amount spent (usd)", "amount spent", "spend", "cost", "total spent"],
    "conversions": ["results", "conversions", "purchases", "customers", "conv."],
}
PARTS = ["date", "brief_variant", "topic_angle", "persona", "stage", "lever", "format"]


def find_col(headers, key):
    lower = {h.lower().strip(): h for h in headers}
    for alias in ALIASES[key]:
        if alias in lower:
            return lower[alias]
    for alias in ALIASES[key]:
        for low, orig in lower.items():
            if low.startswith(alias):
                return orig
    return None


def num(value):
    value = (value or "").replace(",", "").replace("$", "").strip()
    if value in ("", "-", "--"):
        return 0.0
    return float(value)


def parse_name(name):
    """Split an ad name on underscores. Returns None if it does not fit."""
    bits = name.strip().split("_")
    if len(bits) != len(PARTS):
        return None
    parsed = dict(zip(PARTS, bits))
    bv = parsed["brief_variant"].split("-")
    ta = parsed["topic_angle"].split("-", 1)
    parsed["brief"] = bv[0]
    parsed["version"] = bv[1] if len(bv) > 1 else "?"
    parsed["topic"] = ta[0]
    parsed["angle"] = ta[1] if len(ta) > 1 else "?"
    return parsed


def call(spend, conv, target, near, scaling):
    """Return (call, change one thing next) using the Part 1 rules."""
    multiple = spend / target
    cac = spend / conv if conv else None
    if scaling:
        if cac is not None and cac <= target:
            return "scaling", "Still at target CAC. Raise the budget about 20% and check again in 2 to 3 days."
        return "scaling", "Above target CAC. Step back to the last budget that held target."
    if conv >= 10 and cac <= target:
        return "winner", "Copy it into its own SCALE campaign. Then change one thing, such as only the first line."
    if multiple < 2:
        return "invest", "Still reading. Let it reach 2x target CAC before you judge it."
    if conv == 0:
        return "cut", "No conversions at 2x. Check tracking first. If tracking works, cut it."
    if multiple >= 10:
        return "cut", "Reached 10x without 10 conversions at target. Cut it and take the next cell."
    if multiple >= 5:
        if cac <= target:
            return "invest", "At target past 5x. Keep going to prove it by 10x."
        return "cut", "Past 5x and above target CAC. Cut it."
    if cac <= target * near:
        return "invest", "Converting near target. Keep investing up to 5x."
    return "cut", "Converting well above target at 2x or more. Cut it."


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv")
    p.add_argument("--target-cac", type=float, required=True, help="The most you can pay to win one customer")
    p.add_argument("--near", type=float, default=1.25,
                   help="CAC up to this multiple of target counts as near target (default 1.25, change to suit)")
    args = p.parse_args()
    target = args.target_cac

    with open(args.csv, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("No rows found.")
    headers = list(rows[0].keys())
    cols = {k: find_col(headers, k) for k in ALIASES}
    missing = [k for k in ("ad", "spend", "conversions") if cols[k] is None]
    if missing:
        sys.exit(f"Missing columns: {missing}. Found: {headers}")
    print("Columns used: " + ", ".join(f"{k}={v}" for k, v in cols.items() if v))
    print(f"Target CAC: {target:,.2f}. Read at 2x ({2 * target:,.0f}). Invest up to 5x ({5 * target:,.0f}). "
          f"Prove at 10x ({10 * target:,.0f}). Winner = 10 conversions at or under target CAC.\n")

    ads = OrderedDict()
    for r in rows:
        camp = r[cols["campaign"]] if cols["campaign"] else ""
        key = (camp, r[cols["ad"]].strip())
        t = ads.setdefault(key, {"spend": 0.0, "conv": 0.0})
        t["spend"] += num(r[cols["spend"]])
        t["conv"] += num(r[cols["conversions"]])

    print("| Cell | Brief | Version | Lever | Spend (x target CAC) | Conversions | CAC | Call | Change one thing next |")
    print("|---|---|---|---|---|---|---|---|---|")
    counts = {"cut": 0, "invest": 0, "winner": 0, "scaling": 0}
    unparsed = []
    for (camp, name), t in ads.items():
        parsed = parse_name(name)
        if parsed:
            cell = f"{parsed['persona']} x {parsed['angle']}"
            brief, version, lever = parsed["brief"], parsed["version"], parsed["lever"]
        else:
            unparsed.append(name)
            cell, brief, version, lever = name, "?", "?", "?"
        scaling = "scale" in camp.lower()
        c, nxt = call(t["spend"], t["conv"], target, args.near, scaling)
        counts[c] += 1
        cac = f"{t['spend'] / t['conv']:,.0f}" if t["conv"] else "n/a"
        print(f"| {cell} | {brief} | {version} | {lever} | {t['spend']:,.0f} ({t['spend'] / target:.1f}x) | "
              f"{t['conv']:.0f} | {cac} | {c} | {nxt} |")

    print(f"\nNew winners this week: {counts['winner']}. Count what you learn, not what you launch.")
    print(f"Calls: {counts['winner']} winner, {counts['scaling']} scaling, {counts['invest']} invest, {counts['cut']} cut.")
    if unparsed:
        print("Names that do not follow the naming convention: " + "; ".join(unparsed))


if __name__ == "__main__":
    main()
