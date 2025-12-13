import torch
import pandas as pd
from transformers import TrainingArguments, EarlyStoppingCallback


def compute_pos_weights(df, label_cols):
    labels = df[label_cols].values
    pos = labels.sum(axis=0)
    neg = (labels == 0).sum(axis=0)
    weights = torch.tensor(neg / (pos + 1e-5), dtype=torch.float)
    return weights


def get_training_args(
    trial_id, num_epochs=10, learning_rate=2e-5, train_batch_size=32, eval_batch_size=16
):
    return TrainingArguments(
        output_dir=f"./results/{trial_id}",
        num_train_epochs=num_epochs,
        learning_rate=learning_rate,
        per_device_train_batch_size=train_batch_size,
        per_device_eval_batch_size=eval_batch_size,
        weight_decay=0.01,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="eval_subtask_1/f1_macro",
        save_total_limit=2,
        logging_steps=50,
    )


def get_early_stopping_callback(patience=3):
    return EarlyStoppingCallback(early_stopping_patience=patience)
