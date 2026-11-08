---
name: ai-infra-bottleneck-investing
description: "Research and screen AI infrastructure investments with a bottleneck-layer framework: map the physical constraints in the AI value chain (compute, power, memory, storage), rank candidates with a three-part durability test, separate information-driven selling from forced deleveraging, and check valuation floors before sizing. Use when asked to analyse AI infrastructure stocks, neoclouds, memory makers or data-centre power plays, or to stress-test a portfolio thesis built on the AI build-out."
license: MIT
---

# AI infrastructure bottleneck investing

A method for evaluating companies that sell the **physical constraints** of the AI build-out, rather than the applications built on top of them.

Derived from a published portfolio framework; see `references/attribution.md` for source and scope. This is a research method, not investment advice.

## Workflow

### 1. Name the bottleneck

State which physical constraint the company sells: compute, power, memory, storage, or networking. One sentence, no adjectives.

**Done when:** you can name the layer and the specific constraint in one sentence.

### 2. Apply the durability test

For neoclouds and infrastructure builders, score all three:

1. **Financial discipline** — can it fund the build without distressed debt or distressed equity?
2. **Chip access** — is there a real, contracted supply path through Nvidia?
3. **Energy access** — contracted power, or better, generation it controls itself.

Three of three required. Most candidates fail at least one, and failing one is usually fatal over a full cycle.

**Done when:** every candidate has pass/fail per criterion, each backed by a dated source.

### 3. Define quality operationally

Quality is not a vibe and not a low multiple. Quality here means management and execution:

- revenue and backlog grew *through* the drawdown
- no need to raise capital at distressed prices

**Done when:** you hold revenue growth and backlog figures covering the same window as the drawdown.

### 4. Check the valuation floor

Compare the current forward multiple against (a) its own cycle history and (b) prior trough multiples.

Then state which of two things is happening: the **multiple** compressed, or **earnings** are about to fall. A cheap multiple is not a price floor if the denominator is cyclical and rolling over.

**Done when:** you can name which of the two is driving the multiple.

### 5. Diagnose the sell-off

Read `references/selloff-diagnosis.md`, then run `scripts/diagnose_selloff.py`.

Core question: were declines *uniform across companies with different fundamentals, on flat volume* (forced deleveraging), or *concentrated and high-volume* (new information)?

**Done when:** you have a verdict plus the volume ratios that support it.

### 6. Map the catalysts

List dated events that could move the sector, with the market's current implied odds. An undated catalyst is a story, not a catalyst.

**Done when:** every catalyst carries a date and a current probability or consensus level.

### 7. Write the falsifier

State the single observation that would prove the thesis wrong.

**Done when:** one sentence exists which, if observed, forces you to change the position.

## Reporting rules

Always separate three tiers in the output:

- **Verified** — company-reported or exchange data, with the date
- **Source claims** — what an article or interview asserts without primary data
- **Inference** — your reasoning on top of either

Never restate a self-reported return as a track record. Never present a valuation floor as a risk floor.

## Guardrails

Read `references/red-flags.md` before publishing any conclusion. It lists the failure modes this framework is most likely to walk into.
