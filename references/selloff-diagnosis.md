# Diagnosing a sector sell-off

Adapted from Alasdair Mann's portfolio-update reasoning (see `attribution.md`), generalised so it can be applied to any concentrated sector drawdown.

## The question

Is this sell-off **information** (the fundamentals changed) or **plumbing** (leveraged holders were forced out)?

These produce very different actions. Selling into information is prudent. Selling into plumbing is how you donate your position to the buyer who survives.

## Test 1 — uniformity across dissimilar businesses

Line up names with genuinely different fundamentals. If their declines cluster tightly, the market is not discriminating, which points to plumbing rather than fundamentals.

Heuristic: declines within a few percentage points of each other across businesses with different revenue trajectories, backlogs and margins is a plumbing signal.

## Test 2 — volume

An information-driven panic produces volume. A deleveraging does not, because the sellers are being liquidated, not persuaded.

Procedure:

1. Take average daily volume over roughly the last 20 sessions.
2. Divide by average daily volume over the prior ~90 sessions.
3. Ratio near 1.0 or below → no new conviction behind the move.
4. Ratio well above 1.5 → real information is being priced.

Run `scripts/diagnose_selloff.py` on a CSV to compute both tests.

## Test 3 — what kind of drawdown

Use a structural / cyclical / event-driven split (the Goldman taxonomy):

- **Event-driven** — index near highs, no recession, damage concentrated in one sector. Historically the shortest, often measured in months rather than years.
- **Cyclical** — tied to the economic cycle.
- **Structural** — a business model genuinely broke.

Name the category explicitly before arguing about recovery timing.

## The precedence

The August 2007 quant quake (Lo & Khandani) is the cleanest precedent for forced unwinding of crowded positions: losses came from liquidation mechanics, and the hardest-hit strategies rebounded sharply once selling stopped.

**The transferable lesson:** forced selling ends when forced sellers run out, not when the news improves. After it ends, the names sold hardest can snap back fastest — *provided the businesses underneath are intact*. That proviso is the whole trade.

## What the diagnosis does not tell you

- It does not tell you when forced selling ends.
- It does not tell you the business is good. Pair it with the durability test in `SKILL.md`.
- A plumbing read on the sell-off is **not** permission to add leverage into it.
