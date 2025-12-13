import wandb

wandb.init(mode="disabled")

from transformers import AutoTokenizer, DataCollatorWithPadding, Trainer
from src.config import NUM_TYPES, NUM_MANIFESTATIONS, MODEL_NAMES
from src.data import load_data, prepare_datasets
from src.model import SharedMTLModel
from src.metrics import compute_metrics
from src.training import (
    compute_pos_weights,
    get_training_args,
    get_early_stopping_callback,
)
from src.predict import predict_dev_set
from src.logging_utils import log_experiment_results
from src.thresholds import find_optimal_thresholds

# ============ CONFIGURATION ============
languages = ["arb", "eng"]
model_names = [MODEL_NAMES[1], MODEL_NAMES[-1]]
trial_id = "MTL_run"
# languages[i] pairs with model_names[i]
# =======================================


def get_model_short_name(model_name):
    return model_name.split("/")[-1]


def run_experiment(lang, model_name, trial_id):
    print(f"\n{'='*60}")
    print(f"Running: lang={lang}, model={model_name}")
    print(f"Trial ID: {trial_id}")
    print(f"{'='*60}\n")

    train_1, train_2, train_3 = load_data(lang)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    train_dataset, val_dataset = prepare_datasets(train_1, train_2, train_3, tokenizer)

    pos_weight_2 = compute_pos_weights(train_2, train_2.columns[2:])
    pos_weight_3 = compute_pos_weights(train_3, train_3.columns[2:])
    model = SharedMTLModel(
        model_name, NUM_TYPES, NUM_MANIFESTATIONS, pos_weight_2, pos_weight_3
    )

    training_args = get_training_args(trial_id)
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=compute_metrics,
        data_collator=DataCollatorWithPadding(tokenizer),
        callbacks=[get_early_stopping_callback()],
    )

    trainer.train()
    eval_results = trainer.evaluate()
    print(
        f"\nValidation Results (before threshold optimization):",
        f"\n  subtask_1 f1_macro: {eval_results['eval_subtask_1/f1_macro']:.4f}",
        f"\n  subtask_2 f1_macro: {eval_results['eval_subtask_2/f1_macro']:.4f}",
        f"\n  subtask_3 f1_macro: {eval_results['eval_subtask_3/f1_macro']:.4f}",
    )

    val_predictions = trainer.predict(val_dataset)
    val_logits = val_predictions.predictions
    if isinstance(val_logits, tuple):
        val_logits = val_logits[0]

    val_labels = val_predictions.label_ids
    thresholds = find_optimal_thresholds(
        val_logits, val_labels, NUM_TYPES, NUM_MANIFESTATIONS
    )

    print(f"\nOptimal thresholds found:")
    print(f"  Subtask 1: {thresholds['subtask_1']}")
    print(f"  Subtask 2: {thresholds['subtask_2']}")
    print(f"  Subtask 3: {thresholds['subtask_3']}")

    eval_results_optimized = compute_metrics(val_predictions, thresholds=thresholds)
    eval_results_optimized = {f"eval_{k}": v for k, v in eval_results_optimized.items()}
    print(
        f"\nValidation Results (after threshold optimization):",
        f"\n  subtask_1 f1_macro: {eval_results_optimized['eval_subtask_1/f1_macro']:.4f}",
        f"\n  subtask_2 f1_macro: {eval_results_optimized['eval_subtask_2/f1_macro']:.4f}",
        f"\n  subtask_3 f1_macro: {eval_results_optimized['eval_subtask_3/f1_macro']:.4f}",
    )

    log_experiment_results(
        eval_results_optimized,
        trial_id,
        lang,
        model_name,
        training_args,
        NUM_TYPES,
        NUM_MANIFESTATIONS,
        thresholds=thresholds,
    )

    predict_dev_set(trainer, tokenizer, lang, trial_id, thresholds=thresholds)
    print(f"\n✓ Completed: {trial_id}")

    return eval_results_optimized, thresholds


def main():
    results = {}

    for lang, model_name in zip(languages, model_names):
        eval_results, thresholds = run_experiment(lang, model_name, trial_id)
        results[(model_name, lang)] = {
            "eval_results": eval_results,
            "thresholds": thresholds,
        }

    print("\n" + "=" * 60)
    print(f"ALL EXPERIMENTS COMPLETED (trial_id: {trial_id})")
    print("=" * 60)
    for (model_name, lang), data in results.items():
        print(f"\n{get_model_short_name(model_name)} | {lang}:")
        print(f"  F1 Task1: {data['eval_results']['eval_subtask_1/f1_macro']:.4f}")
        print(f"  F1 Task2: {data['eval_results']['eval_subtask_2/f1_macro']:.4f}")
        print(f"  F1 Task3: {data['eval_results']['eval_subtask_3/f1_macro']:.4f}")


if __name__ == "__main__":
    main()
