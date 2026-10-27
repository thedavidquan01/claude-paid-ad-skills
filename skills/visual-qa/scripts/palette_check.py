#!/usr/bin/env python3
"""Measure the main colours in an ad image and compare them to a brand palette.

Usage:
  python3 palette_check.py ad.png --palette "#0B3D2E,#F5F1E8,#E4572E" [--colors 16] [--min-share 1] [--threshold 10]

Prints the image size and aspect ratio, the main colours with their share of
pixels, and the nearest palette colour for each, using CIE76 delta E.
A delta E under about 2 is hard to see. Over the threshold is flagged.
Needs Pillow (pip install pillow).
"""
import argparse
from fractions import Fraction

from PIL import Image


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_lab(rgb):
    def lin(c):
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (lin(c) for c in rgb)
    x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e(a, b):
    la, lb = rgb_to_lab(a), rgb_to_lab(b)
    return sum((p - q) ** 2 for p, q in zip(la, lb)) ** 0.5


def main():
    p = argparse.ArgumentParser()
    p.add_argument("image")
    p.add_argument("--palette", required=True, help="Comma-separated hex codes from DESIGN.md")
    p.add_argument("--colors", type=int, default=16)
    p.add_argument("--min-share", type=float, default=1.0, help="Hide colours under this percent of pixels")
    p.add_argument("--threshold", type=float, default=10.0)
    args = p.parse_args()

    img = Image.open(args.image).convert("RGB")
    w, h = img.size
    ratio = Fraction(w, h).limit_denominator(20)
    print(f"Size: {w}x{h}. Aspect ratio about {ratio.numerator}:{ratio.denominator} ({w / h:.3f}).")

    palette = [hex_to_rgb(x) for x in args.palette.split(",") if x.strip()]
    small = img.copy()
    small.thumbnail((300, 300))
    q = small.quantize(colors=args.colors, method=Image.Quantize.FASTOCTREE)
    pal = q.getpalette()
    counts = sorted(q.getcolors(), reverse=True)
    total = sum(c for c, _ in counts)

    print("Main colours (measured from this file; compression can shift colours):")
    for count, idx in counts:
        if count / total * 100 < args.min_share:
            continue
        rgb = tuple(pal[idx * 3: idx * 3 + 3])
        best = min(palette, key=lambda c: delta_e(rgb, c))
        d = delta_e(rgb, best)
        flag = "OFF-PALETTE?" if d > args.threshold else "ok"
        print(f"  #{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}  {count / total * 100:5.1f}%  "
              f"nearest #{best[0]:02X}{best[1]:02X}{best[2]:02X}  dE {d:5.1f}  {flag}")
    print("Photos and gradients produce many in-between colours. Check flagged colours by eye before you call them errors.")


if __name__ == "__main__":
    main()
