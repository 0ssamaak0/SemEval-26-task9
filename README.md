## 0ssamaak0 at SemEval-2026 Task 9

Multilingual polarization detection (Arabic + English) across three linked subtasks:
- Subtask 1: binary polarized vs. non‑polarized.
- Subtask 2: multi-label type (political, racial/ethnic, religious, gender/sexual, other).
- Subtask 3: multi-label manifestation (stereotype, vilification, dehumanization, extreme language, lack of empathy, invalidation).

## What’s in this repo
- `src/`: multitask model, training, thresholds, metrics, prediction.
- `dev_phase/`: SemEval training/dev splits per subtask and language.
- `figures/`: plots used in the paper (label skew, gating, dialectness, model selection).
- `main.tex`: paper with full method/results; `results/`: per-run CSVs; `EDA/figures/`: exploratory plots.

## Approach (from `main.tex`)
- Shared encoder MTL (MARBERTv2 for Arabic; hate-speech RoBERTa for English) with three heads.
- Inference-time hard gating: Subtask 1 mask zeros Subtasks 2–3 outputs for non‑polarized texts.
- Class-weighted BCE; grid-searched per-label thresholds (helps English).
- Data augmentation: ~15% Arabic paraphrased; English left as-is.
- Baselines: single-task fine-tuning and DSPy prompting/optimization—both trail the gated encoder.

## Data highlights
- ~3.4k AR / ~3.2k EN train; Codabench dev used as test.
- English: strong skew (non-polarized dominant; political label dominates Subtask 2).  
  ![Type label distribution](figures/subtask_2_label_distribution.pdf)
- Arabic: mix of MSA and dialectal text; dialectness mostly low.  
  ![ALDi histogram](figures/aldi_histogram.pdf)

## Model insights
- Domain-specialized encoders win: MARBERTv2 (AR) and hate-speech RoBERTa (EN).  
  ![Model comparison](figures/model_selection_comparison.pdf)
- Inference gating beats no/ training-time gating for subtasks 2–3.  
  ![Gating comparison](figures/gating_strategy_comparison.pdf)
- ARBERT–MARBERT ensemble via ALDi routing underperforms MARBERT alone.  
  ![Ensemble](figures/arbertmarbert.pdf)

## Headline results (F1 Macro, dev as test)
- Subtask 1: 0.839 (AR) / 0.842 (EN)
- Subtask 2: 0.596 (AR) / 0.449 (EN)
- Subtask 3: 0.607 (AR) / 0.496 (EN)

## Reproducing
1) Install deps (PyTorch + HF Transformers).  
2) Train: see `src/training.py` and config in `src/config.py`.  
3) Predict/eval: `src/predict.py` with saved checkpoints; adjust thresholds via `src/thresholds.py`.