import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer


class PolarizationDataset(torch.utils.data.Dataset):
    def __init__(self, texts, labels, tokenizer, max_length=128):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding=False,
            max_length=self.max_length,
            return_tensors="pt",
        )

        item = {key: encoding[key].squeeze() for key in encoding.keys()}
        item["labels"] = torch.tensor(label, dtype=torch.float)
        return item


def get_label_columns(df):
    return [col for col in df.columns if col not in ["id", "text"]]


def load_data(lang, augmentation=True, data_dir="./dev_phase"):
    if augmentation:
        train_1 = pd.read_csv(f"{data_dir}/subtask1/train/{lang}_augmented.csv")
        train_2 = pd.read_csv(f"{data_dir}/subtask2/train/{lang}_augmented.csv")
        train_3 = pd.read_csv(f"{data_dir}/subtask3/train/{lang}_augmented.csv")
    else:
        train_1 = pd.read_csv(f"{data_dir}/subtask1/train/{lang}.csv")
        train_2 = pd.read_csv(f"{data_dir}/subtask2/train/{lang}.csv")
        train_3 = pd.read_csv(f"{data_dir}/subtask3/train/{lang}.csv")
    return train_1, train_2, train_3


def prepare_datasets(
    train_1, train_2, train_3, tokenizer, test_size=0.20, random_state=42
):
    n_samples = len(train_1)
    indices = np.arange(n_samples)
    train_indices, val_indices = train_test_split(
        indices, test_size=test_size, random_state=random_state
    )

    merged = train_1.merge(
        train_2, on=["id", "text"], how="outer", suffixes=("_1", "_2")
    )
    merged = merged.merge(train_3, on=["id", "text"], how="outer", suffixes=("", "_3"))

    merged_label_columns = get_label_columns(merged)
    texts = merged["text"].tolist()
    labels = merged[merged_label_columns].values.tolist()

    texts_train = [texts[i] for i in train_indices]
    texts_val = [texts[i] for i in val_indices]
    labels_train = [labels[i] for i in train_indices]
    labels_val = [labels[i] for i in val_indices]

    train_dataset = PolarizationDataset(texts_train, labels_train, tokenizer)
    val_dataset = PolarizationDataset(texts_val, labels_val, tokenizer)

    return train_dataset, val_dataset
