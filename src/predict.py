import os
import numpy as np
import pandas as pd
from src.data import PolarizationDataset
from src.config import NUM_TYPES, NUM_MANIFESTATIONS
from src.thresholds import apply_thresholds


def predict_dev_set(
    trainer, tokenizer, lang, trial_id, thresholds=None, data_dir="./dev_phase"
):
    dev_1 = pd.read_csv(f"{data_dir}/subtask1/dev/{lang}.csv")
    dev_2 = pd.read_csv(f"{data_dir}/subtask2/dev/{lang}.csv")
    dev_3 = pd.read_csv(f"{data_dir}/subtask3/dev/{lang}.csv")

    dev_texts = dev_1["text"].tolist()
    dev_dataset = PolarizationDataset(dev_texts, [[0] * 12] * len(dev_texts), tokenizer)

    predictions = trainer.predict(dev_dataset)
    logits = predictions.predictions
    if isinstance(logits, tuple):
        logits = logits[0]
    probs = 1 / (1 + np.exp(-logits))

    if thresholds is not None:
        polarization_preds, types_preds, manifestations_preds = apply_thresholds(
            probs, thresholds, NUM_TYPES, NUM_MANIFESTATIONS
        )
    else:
        preds = (probs >= 0.5).astype(int)
        polarization_preds = preds[:, 0]
        mask = polarization_preds[:, None]
        types_preds = preds[:, 1 : 1 + NUM_TYPES] * mask
        manifestations_preds = preds[:, 1 + NUM_TYPES :] * mask

    output_1 = dev_1[["id", "text"]].copy()
    output_1["polarization"] = polarization_preds

    output_2 = dev_2[["id", "text"]].copy()
    type_cols = [col for col in dev_2.columns if col not in ["id", "text"]]
    for i, col in enumerate(type_cols):
        output_2[col] = types_preds[:, i]

    output_3 = dev_3[["id", "text"]].copy()
    manifest_cols = [col for col in dev_3.columns if col not in ["id", "text"]]
    for i, col in enumerate(manifest_cols):
        output_3[col] = manifestations_preds[:, i]

    output_1 = output_1.drop(columns=["text"])
    output_2 = output_2.drop(columns=["text"])
    output_3 = output_3.drop(columns=["text"])

    os.makedirs(f"./results/{trial_id}", exist_ok=True)
    os.makedirs(f"./results/{trial_id}/subtask_1", exist_ok=True)
    os.makedirs(f"./results/{trial_id}/subtask_2", exist_ok=True)
    os.makedirs(f"./results/{trial_id}/subtask_3", exist_ok=True)

    output_1.to_csv(f"./results/{trial_id}/subtask_1/pred_{lang}.csv", index=False)
    output_2.to_csv(f"./results/{trial_id}/subtask_2/pred_{lang}.csv", index=False)
    output_3.to_csv(f"./results/{trial_id}/subtask_3/pred_{lang}.csv", index=False)

    return output_1, output_2, output_3
