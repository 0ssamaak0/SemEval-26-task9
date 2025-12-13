import numpy as np
from sklearn.metrics import f1_score
from src.config import NUM_TYPES, NUM_MANIFESTATIONS


def compute_metrics(eval_pred):
    logits = eval_pred.predictions
    labels = eval_pred.label_ids

    if isinstance(logits, tuple):
        logits = logits[0]

    probs = 1 / (1 + np.exp(-logits))
    preds = (probs >= 0.5).astype(int)
    labels = labels.astype(int)

    y1_true = labels[:, 0]
    y1_pred = preds[:, 0]

    mask = y1_pred[:, None]

    y2_pred_raw = preds[:, 1 : 1 + NUM_TYPES]
    y3_pred_raw = preds[:, 1 + NUM_TYPES :]

    y2_pred = y2_pred_raw * mask
    y3_pred = y3_pred_raw * mask

    y2_true = labels[:, 1 : 1 + NUM_TYPES]
    y3_true = labels[:, 1 + NUM_TYPES :]

    return {
        "subtask_1/f1_macro": f1_score(
            y1_true, y1_pred, average="macro", zero_division=0
        ),
        "subtask_2/f1_macro": f1_score(
            y2_true, y2_pred, average="macro", zero_division=0
        ),
        "subtask_3/f1_macro": f1_score(
            y3_true, y3_pred, average="macro", zero_division=0
        ),
    }
