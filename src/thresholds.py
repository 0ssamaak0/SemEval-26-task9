import numpy as np
from sklearn.metrics import f1_score
from src.config import NUM_TYPES, NUM_MANIFESTATIONS


def find_optimal_thresholds(logits, labels, num_types, num_manifestations):
    probs = 1 / (1 + np.exp(-logits))
    labels = labels.astype(int)

    y1_true = labels[:, 0]
    y2_true = labels[:, 1 : 1 + num_types]
    y3_true = labels[:, 1 + num_types :]

    y1_probs = probs[:, 0]
    y2_probs = probs[:, 1 : 1 + num_types]
    y3_probs = probs[:, 1 + num_types :]

    threshold_range_task1 = np.arange(0.3, 0.75, 0.05)
    threshold_range = np.arange(0.2, 0.85, 0.05)

    best_combined_f1 = 0
    best_thresh_1 = 0.5
    best_thresholds_2 = np.ones(num_types) * 0.5
    best_thresholds_3 = np.ones(num_manifestations) * 0.5

    for thresh_1 in threshold_range_task1:
        y1_pred = (y1_probs >= thresh_1).astype(int)
        mask = y1_pred

        f1_1 = f1_score(y1_true, y1_pred, average="macro", zero_division=0)

        temp_thresholds_2 = np.zeros(num_types)
        for i in range(num_types):
            best_f1 = 0
            for thresh in threshold_range:
                y2_pred_raw = (y2_probs[:, i] >= thresh).astype(int)
                y2_pred = y2_pred_raw * mask
                f1 = f1_score(y2_true[:, i], y2_pred, average="binary", zero_division=0)
                if f1 > best_f1:
                    best_f1 = f1
                    temp_thresholds_2[i] = thresh

        temp_thresholds_3 = np.zeros(num_manifestations)
        for i in range(num_manifestations):
            best_f1 = 0
            for thresh in threshold_range:
                y3_pred_raw = (y3_probs[:, i] >= thresh).astype(int)
                y3_pred = y3_pred_raw * mask
                f1 = f1_score(y3_true[:, i], y3_pred, average="binary", zero_division=0)
                if f1 > best_f1:
                    best_f1 = f1
                    temp_thresholds_3[i] = thresh

        y2_pred_full = np.zeros_like(y2_probs, dtype=int)
        for i in range(num_types):
            y2_pred_full[:, i] = (y2_probs[:, i] >= temp_thresholds_2[i]).astype(int)
        y2_pred_full = y2_pred_full * mask[:, None]

        y3_pred_full = np.zeros_like(y3_probs, dtype=int)
        for i in range(num_manifestations):
            y3_pred_full[:, i] = (y3_probs[:, i] >= temp_thresholds_3[i]).astype(int)
        y3_pred_full = y3_pred_full * mask[:, None]

        f1_2 = f1_score(y2_true, y2_pred_full, average="macro", zero_division=0)
        f1_3 = f1_score(y3_true, y3_pred_full, average="macro", zero_division=0)

        combined_f1 = f1_1 + f1_2 + f1_3

        if combined_f1 > best_combined_f1:
            best_combined_f1 = combined_f1
            best_thresh_1 = thresh_1
            best_thresholds_2 = temp_thresholds_2.copy()
            best_thresholds_3 = temp_thresholds_3.copy()

    return {
        "subtask_1": [round(best_thresh_1, 2)],
        "subtask_2": [round(t, 2) for t in best_thresholds_2.tolist()],
        "subtask_3": [round(t, 2) for t in best_thresholds_3.tolist()],
    }


def apply_thresholds(probs, thresholds, num_types, num_manifestations):
    y1_probs = probs[:, 0]
    y2_probs = probs[:, 1 : 1 + num_types]
    y3_probs = probs[:, 1 + num_types :]

    y1_pred = (y1_probs >= thresholds["subtask_1"][0]).astype(int)

    mask = y1_pred[:, None]

    y2_pred = np.zeros_like(y2_probs, dtype=int)
    for i in range(num_types):
        y2_pred[:, i] = (y2_probs[:, i] >= thresholds["subtask_2"][i]).astype(int)
    y2_pred = y2_pred * mask

    y3_pred = np.zeros_like(y3_probs, dtype=int)
    for i in range(num_manifestations):
        y3_pred[:, i] = (y3_probs[:, i] >= thresholds["subtask_3"][i]).astype(int)
    y3_pred = y3_pred * mask

    return y1_pred, y2_pred, y3_pred
