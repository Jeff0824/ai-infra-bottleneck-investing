# AI infrastructure bottleneck investing

An agent skill for evaluating companies that sell the **physical constraints** of the AI build-out — compute, power, memory, storage — rather than the applications built on top.

## What it does

A seven-step workflow that forces the analysis to be checkable:

1. Name the bottleneck (which physical constraint does this company sell?)
2. Durability test — finances, chip access, energy access (3 of 3 required)
3. Define quality operationally — grew through the drawdown, no distressed raise
4. Check the valuation floor — is the *multiple* cheap, or are *earnings* about to fall?
5. Diagnose the sell-off — information, or forced deleveraging? (with a script)
6. Map dated catalysts
7. Write the falsifier

Plus a red-flag checklist and a reporting rule that separates verified facts from source claims from inference.

## Install

Copy the directory into your agent's skills folder:

```bash
cp -r ai-infra-bottleneck-investing ~/.openclaw/workspace/skills/
```

Or clone and symlink:

```bash
git clone <this-repo> ~/skills/ai-infra-bottleneck-investing
ln -s ~/skills/ai-infra-bottleneck-investing ~/.openclaw/workspace/skills/ai-infra-bottleneck-investing
```

## The diagnostic script

`scripts/diagnose_selloff.py` takes a CSV of price declines and volume ratios and returns a verdict:

```bash
python3 scripts/diagnose_selloff.py moves.csv
```

```
ticker       decline   vol 20/90
NBIS          -33.1%        1.04
BE            -33.0%        1.04
SFTBY         -32.1%        0.95
HXSCL         -31.4%        0.65
SNDK          -30.4%        0.70

decline spread : 2.7 pp (uniform if <= 5.0)
mean vol ratio : 0.88 (quiet if <= 1.2, loud if >= 1.5)

VERDICT: plumbing-leaning - uniform declines on flat volume.
```

Exit codes: `0` plumbing-leaning, `1` information-leaning, `2` mixed, `3` bad input. Stdlib only, no dependencies.

## Structure

```
SKILL.md                      the seven-step workflow
references/selloff-diagnosis.md
references/red-flags.md
references/attribution.md
scripts/diagnose_selloff.py
```

## Attribution and disclaimer

The framework is derived from a public portfolio update by **Alasdair Mann** (Edelbridge, Substack). See `references/attribution.md`. The method is credited; the text is not reproduced. Critique of the source's weaker claims is included deliberately.

**Not investment advice.** Verify every figure against primary filings.
