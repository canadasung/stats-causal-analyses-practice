# stats-causal-analyses-practice

Personal practice project applying causal inference techniques from the UBC MDS program. Two tracks: Track 1 is questions answerable by randomized A/B testing; Track 2 is questions that can't be randomized (e.g. smoking → cancer) and need observational causal methods (matching/IPW, diff-in-diff, IV, double ML). Full rationale and dataset list is in `README.md`.

## Status

Scaffolding only — `notebooks/*.ipynb` contain the question, technique focus, data-loading code, and a TODO list per notebook, but no analysis has been written yet. The user is doing the analysis themselves as a learning exercise — don't fill in the TODOs or write the statistical analysis for them unless they explicitly ask; default to letting them drive and only assist when asked (debugging, explaining a method, reviewing what they wrote).

## Layout

- `notebooks/` — one notebook per technique, numbered roughly in the order they're meant to be worked through
- `src/utils.py` — shared path constants (`DATA_RAW`, `DATA_PROCESSED`) and plot styling, nothing analytical
- `data/raw/`, `data/processed/` — gitignored, populated via Kaggle CLI or `causaldata` package per notebook instructions
- `environment.yml` — conda env (`stats-causal`)

## Setup

```bash
conda env create -f environment.yml
conda activate stats-causal
jupyter lab
```
