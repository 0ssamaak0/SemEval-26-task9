import json


def log(
    subtask_name,
    language,
    eval_results,
    logs_path="logs.json",
    metadata=None,
    trial_id=None,
):
    """
    Updates the logs.json file with evaluation results for a given subtask and language.
    If trial_id is None, creates a new trial and adds it to the logs.
    If trial_id is provided, it updates the relevant trial if found.
    Optionally, add/replace the metadata block if metadata is provided.
    """
    model_name = getattr(globals().get("model", None), "name_or_path", "unknown")
    training_args_obj = globals().get("training_args", None)
    learning_rate = getattr(training_args_obj, "learning_rate", None)
    num_train_epochs = getattr(training_args_obj, "num_train_epochs", None)
    per_device_train_batch_size = getattr(
        training_args_obj, "per_device_train_batch_size", None
    )

    def default_meta():
        if metadata is not None:
            return metadata
        else:
            return {
                "model": model_name,
                "learning_rate": learning_rate,
                "num_train_epochs": num_train_epochs,
                "per_device_train_batch_size": per_device_train_batch_size,
            }

    subtask_dict = {subtask_name: {language: {"eval_results": eval_results}}}

    try:
        with open(logs_path, "r+", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
            # Ensure logs is a list of trials
            if isinstance(logs, dict):
                logs = [logs]
            if trial_id is None:
                # Create a new trial with a new trial_id (incremented or fallback)
                existing_ids = [
                    t.get("trial_id") for t in logs if t.get("trial_id") is not None
                ]
                next_id = (
                    f"{int(max(existing_ids, default='0'))+1:06d}"
                    if existing_ids
                    else "000001"
                )
                new_trial = {
                    "trial_id": next_id,
                    **subtask_dict,
                    "metadata": default_meta(),
                }
                logs.append(new_trial)
            else:
                # Look for existing trial with given trial_id and update it
                found = False
                for trial in logs:
                    if trial.get("trial_id") == trial_id:
                        # Make sure subtask/language block exists
                        if subtask_name not in trial:
                            trial[subtask_name] = {}
                        if language not in trial[subtask_name]:
                            trial[subtask_name][language] = {}
                        trial[subtask_name][language]["eval_results"] = eval_results
                        if metadata is not None:
                            trial["metadata"] = metadata
                        found = True
                        break
                if not found:
                    # If not found, create a new trial with that trial_id
                    new_trial = {
                        "trial_id": trial_id,
                        **subtask_dict,
                        "metadata": default_meta(),
                    }
                    logs.append(new_trial)
            f.seek(0)
            json.dump(logs if len(logs) > 1 else logs[0], f, indent=4)
            f.truncate()
    except FileNotFoundError:
        # If logs file doesn't exist, create a new file with one trial
        init_trial_id = trial_id if trial_id is not None else "000001"
        new_trial = {
            "trial_id": init_trial_id,
            "approach": model_name if model_name else "bert",
            **subtask_dict,
            "metadata": default_meta(),
        }
        with open(logs_path, "w", encoding="utf-8") as f:
            json.dump([new_trial], f, indent=4)


# Example usage
log(
    subtask_name="subtask_1",
    language="ENGLISH",
    eval_results=eval_results,
    metadata={
        "approach": "ALOHA",
        "model": model_name,
        "learning_rate": 32,
        "num_train_epochs": 1234,
        "per_device_train_batch_size": 45,
    },
    trial_id=444645,  # Pass your desired trial_id, or set to None to create new trial
)
