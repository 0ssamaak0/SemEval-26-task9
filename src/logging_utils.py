import json
from logs import log


def log_experiment_results(eval_results, trial_id, lang, model_name, training_args, num_types, num_manifestations, datasets_merge=None):
    experiment_metadata = {
        "approach": "MTL_no_gate",
        f"model_{lang}": model_name,
        "learning_rate": training_args.learning_rate,
        "num_train_epochs": training_args.num_train_epochs,
        "per_device_train_batch_size": training_args.per_device_train_batch_size,
        "per_device_eval_batch_size": training_args.per_device_eval_batch_size,
        "num_types": num_types,
        "num_manifestations": num_manifestations,
        "datasets_merge": datasets_merge,
        "posweight": "True"
    }

    subtask_1_results = {
        "eval_f1_macro": eval_results.get("eval_subtask_1/f1_macro"),
    }
    subtask_2_results = {
        "eval_f1_macro": eval_results.get("eval_subtask_2/f1_macro"),
    }
    subtask_3_results = {
        "eval_f1_macro": eval_results.get("eval_subtask_3/f1_macro"),
    }

    existing_metadata = {}
    try:
        with open("logs.json", "r", encoding="utf-8") as f:
            logs = json.load(f)
            if isinstance(logs, dict):
                logs = [logs]
            for trial in logs:
                if trial.get("trial_id") == trial_id and "metadata" in trial:
                    existing_metadata = trial["metadata"].copy()
                    break
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    merged_metadata = dict(existing_metadata)
    merged_metadata.update({
        f"model_{lang}": model_name,
        "approach": experiment_metadata["approach"],
        "learning_rate": experiment_metadata["learning_rate"],
        "num_train_epochs": experiment_metadata["num_train_epochs"],
        "per_device_train_batch_size": experiment_metadata["per_device_train_batch_size"],
        "per_device_eval_batch_size": experiment_metadata["per_device_eval_batch_size"],
        "num_types": experiment_metadata["num_types"],
        "num_manifestations": experiment_metadata["num_manifestations"],
        "datasets_merge": experiment_metadata["datasets_merge"]
    })

    log(
        subtask_name="subtask_1",
        language=lang,
        eval_results=subtask_1_results,
        metadata=merged_metadata,
        trial_id=trial_id
    )

    log(
        subtask_name="subtask_2",
        language=lang,
        eval_results=subtask_2_results,
        metadata=None,
        trial_id=trial_id
    )

    log(
        subtask_name="subtask_3",
        language=lang,
        eval_results=subtask_3_results,
        metadata=None,
        trial_id=trial_id
    )

    print(f"\n✓ Experiment results logged to logs.json (trial_id: {trial_id})")
    print(f"  - subtask_1: {lang}")
    print(f"  - subtask_2: {lang}")
    print(f"  - subtask_3: {lang}")
