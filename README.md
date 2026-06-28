# Causal Analyses Practice

Practice project applying causal inference techniques from the UBC MDS program to social-problem-style datasets. Split into two tracks: questions answerable by a randomized A/B test, and questions that can't be randomized (e.g. smoking → cancer) and need observational causal methods.

## Setup

```bash
conda env create -f environment.yml
conda activate stats-causal
jupyter lab
```

## Track 1 — Randomized (A/B testing)

| Notebook | Dataset | Technique focus |
|---|---|---|
| `01_ab_testing_cookiecats.ipynb` | Cookie Cats (Kaggle) | proportion z-test, retention lift, sample ratio mismatch |
| `02_ab_testing_marketing.ipynb` | Marketing A/B Testing (Kaggle) | conversion test, CUPED variance reduction |
| `03_ab_testing_simulated.ipynb` | self-generated | power analysis, sequential testing, validating a test against a known ground-truth effect |

Kaggle datasets aren't auto-downloadable without auth. To fetch them:
1. Get a Kaggle API token: account settings → "Create New Token" → save `kaggle.json` to `~/.kaggle/kaggle.json`.
2. Run:
   ```bash
   kaggle datasets download -d yufengsui/mobile-games-ab-testing -p data/raw --unzip   # Cookie Cats
   kaggle datasets download -d faviovaz/marketing-ab-testing -p data/raw --unzip       # Marketing A/B
   ```

## Track 2 — Observational causal inference (no randomization possible)

| Notebook | Dataset | Technique focus |
|---|---|---|
| `04_matching_ipw_lalonde.ipynb` | Lalonde / NSW job training (`causaldata`) | propensity score matching, IPW |
| `05_diff_in_diff_minwage.ipynb` | Card & Krueger minimum wage (`causaldata`) | difference-in-differences |
| `06_iv_card_college.ipynb` | Card college proximity (`causaldata`) | instrumental variables (2SLS) |
| `07_doubleml_ihdp.ipynb` | IHDP semi-synthetic | double ML / heterogeneous treatment effects, validated against a *known* true effect |
| `08_smoking_cancer_observational.ipynb` | NHANES | matching/IPW + sensitivity analysis on a real "can't randomize this" question |

All `causaldata` datasets load directly in Python — no manual download needed:
```python
from causaldata import lalonde, minwage, card
df = lalonde.load_pandas().data
```

IHDP and NHANES download instructions are in their respective notebooks.

## Why these datasets

- **Lalonde** and **IHDP** are the standard benchmarks in causal inference papers/courses because the true effect is known (IHDP is semi-synthetic, Lalonde has an experimental benchmark to check observational estimates against) — use these to validate that your estimator works *before* trusting it on a real open question.
- **Card & Krueger** and **Card college proximity** are the canonical textbook examples for DiD and IV respectively.
- **NHANES** is real, messy, observational data — good for practicing the full workflow (confounding, sensitivity analysis, no ground truth to check against) on a genuine "social problem" question.

## Repo layout

```
data/raw/        # untouched downloads (gitignored)
data/processed/  # cleaned datasets used by notebooks (gitignored)
notebooks/       # one notebook per technique
src/             # shared loading/plotting helpers
reports/         # write-ups of findings, if any
```
