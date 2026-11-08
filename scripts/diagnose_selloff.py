#!/usr/bin/env python3
"""Diagnose whether a sector sell-off looks like forced deleveraging or new information.

Two tests:
  1. Uniformity - are declines clustered across dissimilar businesses?
  2. Volume     - did volume expand, or did the sellers arrive without conviction?

Input CSV columns (header required):
  ticker,peak,current,vol_20d,vol_90d

  peak      peak price (or closing high) for the window
  current   latest price
  vol_20d   average daily volume, last ~20 sessions
  vol_90d   average daily volume, prior ~90 sessions

Usage:
  python3 diagnose_selloff.py moves.csv [--spread-pp 5.0] [--vol-info 1.5] [--vol-plumb 1.2]

Exit codes: 0 = plumbing-leaning, 1 = information-leaning, 2 = mixed/insufficient, 3 = bad input
"""
from __future__ import annotations
import argparse
import csv
import statistics
import sys

def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        need = {"ticker", "peak", "current", "vol_20d", "vol_90d"}
        if not reader.fieldnames or not need.issubset({c.strip() for c in reader.fieldnames}):
            raise ValueError(f"CSV must have columns: {', '.join(sorted(need))}")
        for r in reader:
            try:
                peak = float(r["peak"])
                cur = float(r["current"])
                v20 = float(r["vol_20d"])
                v90 = float(r["vol_90d"])
            except (TypeError, ValueError):
                continue
            if peak <= 0 or v90 <= 0:
                continue
            rows.append({
                "ticker": (r["ticker"] or "").strip(),
                "decline_pct": (cur / peak - 1.0) * 100.0,
                "vol_ratio": v20 / v90,
            })
    return rows

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_path")
    ap.add_argument("--spread-pp", type=float, default=5.0,
                    help="max spread in percentage points for declines to count as uniform (default 5.0)")
    ap.add_argument("--vol-info", type=float, default=1.5,
                    help="volume ratio at or above which selling looks information-driven (default 1.5)")
    ap.add_argument("--vol-plumb", type=float, default=1.2,
                    help="volume ratio at or below which selling looks plumbing-driven (default 1.2)")
    args = ap.parse_args(argv)

    try:
        rows = load(args.csv_path)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 3
    if not rows:
        print("error: no usable rows", file=sys.stderr)
        return 3

    rows.sort(key=lambda r: r["decline_pct"])
    declines = [r["decline_pct"] for r in rows]
    ratios = [r["vol_ratio"] for r in rows]
    spread = max(declines) - min(declines)
    mean_ratio = statistics.fmean(ratios)

    print(f"{'ticker':<10}{'decline':>10}{'vol 20/90':>12}")
    for r in rows:
        print(f"{r['ticker']:<10}{r['decline_pct']:>9.1f}%{r['vol_ratio']:>12.2f}")

    uniform = spread <= args.spread_pp
    quiet = mean_ratio <= args.vol_plumb
    loud = mean_ratio >= args.vol_info

    print()
    print(f"decline spread : {spread:.1f} pp (uniform if <= {args.spread_pp})")
    print(f"mean vol ratio : {mean_ratio:.2f} (quiet if <= {args.vol_plumb}, loud if >= {args.vol_info})")
    print()

    if uniform and quiet:
        print("VERDICT: plumbing-leaning - uniform declines on flat volume.")
        print("         Consistent with forced deleveraging rather than new information.")
        print("         Pair with the durability test before acting: plumbing explains the")
        print("         price move, it does not make the business good.")
        return 0
    if loud and not uniform:
        print("VERDICT: information-leaning - declines dispersed and volume expanded.")
        print("         The market appears to be discriminating. Treat as fundamentals.")
        return 1
    print("VERDICT: mixed - neither signal dominates.")
    print("         Gather more evidence before drawing a conclusion.")
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
