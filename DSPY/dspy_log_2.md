2025/12/04 12:14:27 INFO dspy.teleprompt.mipro_optimizer_v2: 
RUNNING WITH THE FOLLOWING LIGHT AUTO RUN SETTINGS:
num_trials: 10
minibatch: True
num_fewshot_candidates: 6
num_instruct_candidates: 3
valset size: 67

2025/12/04 12:14:27 INFO dspy.teleprompt.mipro_optimizer_v2: 
==> STEP 1: BOOTSTRAP FEWSHOT EXAMPLES <==
2025/12/04 12:14:27 INFO dspy.teleprompt.mipro_optimizer_v2: These will be used as few-shot example candidates for our program and for creating instructions.

2025/12/04 12:14:27 INFO dspy.teleprompt.mipro_optimizer_v2: Bootstrapping N=6 sets of demonstrations...
Bootstrapping set 1/6
Bootstrapping set 2/6
Bootstrapping set 3/6
  1%|▏         | 4/270 [00:16<18:24,  4.15s/it]
Bootstrapped 4 full traces after 4 examples for up to 1 rounds, amounting to 4 attempts.
Bootstrapping set 4/6
  1%|          | 2/270 [00:12<27:33,  6.17s/it]
Bootstrapped 1 full traces after 2 examples for up to 1 rounds, amounting to 2 attempts.
Bootstrapping set 5/6
  0%|          | 1/270 [00:07<34:58,  7.80s/it]
Bootstrapped 1 full traces after 1 examples for up to 1 rounds, amounting to 1 attempts.
Bootstrapping set 6/6
  0%|          | 1/270 [00:03<14:43,  3.28s/it]
2025/12/04 12:15:07 INFO dspy.teleprompt.mipro_optimizer_v2: 
==> STEP 2: PROPOSE INSTRUCTION CANDIDATES <==
2025/12/04 12:15:07 INFO dspy.teleprompt.mipro_optimizer_v2: We will use the few-shot examples from the previous step, a generated dataset summary, a summary of the program code, and a randomly selected prompting tip to propose instructions.
Bootstrapped 1 full traces after 1 examples for up to 1 rounds, amounting to 1 attempts.
2025/12/04 12:18:59 INFO dspy.teleprompt.mipro_optimizer_v2: 
Proposing N=3 instructions...

2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: Proposed Instructions for Predictor 0:

2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: 0: Polarization denotes stereotyping, vilification, dehumanization, deindividuation, or intolerance of other people’s views, beliefs, and identities. In this study, speeches and articles that are shared on social media that incite division, groupism, hatred, conflict, and intolerance are classified as containing polarization.
Given this sentence, classify it as containing polarization or not.

2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: 1: You are a safety-conscious Arabic text moderation assistant. You will receive one Arabic sentence (dialectal, with informal punctuation, emojis, line breaks, elongations, and Eastern Arabic numerals). Determine whether the sentence contains polarization content (divisive or polarizing language targeting identity-based groups). Polarization includes stereotyping, vilification, dehumanization, deindividuation, or intolerance toward others based on religion, nationality/ethnicity, political actors, or other identity characteristics, as well as calls to action or us-vs-them framing that aims to incite division or hostility.

Rules:
- Output exactly one of two labels: polarization or no polarization (all lowercase).
- If the sentence clearly targets an identity-based group with demeaning or violent language, or advocates exclusion, segregation, or harm against a group, label polarization.
- If the sentence is neutral, informational, celebratory (e.g., sports results), or does not express hostility toward a group, label no polarization.
- Be resilient to dialect variation, negation, sarcasm, informal markers, punctuation noise, and emojis; normalize mentally but do not change content.
- If the sentence is ambiguous or lacks clear polarization cues, default to no polarization.
- Do not include any additional text or formatting in the output; only the single label.
- This task is high-stakes: inaccurate labeling can misclassify user-generated content and affect safety moderation. Apply careful judgment.

2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: 2: You are an Arabic text polarization detector. For each input sentence, determine whether the content expresses polarized, divisive, or inflammatory viewpoints (targeting identity-based groups with us-vs-them framing, dehumanization, calls to action, or endorsement of hostility) or whether it is non-polarized/neutral. Respond with exactly one line in the following format:

Polarization: polarization
or
Polarization: no polarization

Guidelines:
- Consider polarity even if expressed through sarcasm, negation, or informal punctuation; focus on the underlying intent and the target.
- Identity-based groups include religion, nationality/ethnicity, political actors, or other social identities.
- Polarized content includes demeaning or vilifying a group, portraying them as a threat, advocating exclusion or violence, or urging collective action against a group.
- Non-polarized content includes neutral information, factual reporting, or celebratory statements that do not advocate division or hostility toward a group.
- Handle Arabic dialectal variations, informal spellings, elongations, and emojis by interpreting the meaning; do not misclassify due to dialectal noise.
- If the sentence is empty, unintelligible, or clearly non-polar, output Polarization: no polarization.
- Output must be exactly one of the two allowed lines; no extra text.

2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: 

2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: ==> STEP 3: FINDING OPTIMAL PROMPT PARAMETERS <==
2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: We will evaluate the program over a series of trials with different combinations of instructions and few-shot examples to find the optimal combination using Bayesian Optimization.

2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 1 / 13 - Full Evaluation of Default Program ==
Average Metric: 54.00 / 67 (80.6%): 100%|██████████| 67/67 [00:00<00:00, 1776.11it/s]2025/12/04 12:21:19 INFO dspy.evaluate.evaluate: Average Metric: 54 / 67 (80.6%)
2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: Default program score: 80.6

/Users/0ssamaak0/miniconda3/envs/nlp/lib/python3.13/site-packages/optuna/_experimental.py:32: ExperimentalWarning: Argument ``multivariate`` is an experimental feature. The interface can change in the future.
  warnings.warn(
2025/12/04 12:21:19 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 2 / 13 - Minibatch ==

Average Metric: 28.00 / 35 (80.0%): 100%|██████████| 35/35 [00:34<00:00,  1.02it/s]2025/12/04 12:21:54 INFO dspy.evaluate.evaluate: Average Metric: 28 / 35 (80.0%)
2025/12/04 12:21:54 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 80.0 on minibatch of size 35 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 3'].
2025/12/04 12:21:54 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0]
2025/12/04 12:21:54 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6]
2025/12/04 12:21:54 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 80.6
2025/12/04 12:21:54 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:21:54 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 3 / 13 - Minibatch ==

Average Metric: 26.00 / 35 (74.3%): 100%|██████████| 35/35 [01:09<00:00,  1.99s/it]2025/12/04 12:23:03 INFO dspy.evaluate.evaluate: Average Metric: 26 / 35 (74.3%)
2025/12/04 12:23:03 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 74.29 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 0'].
2025/12/04 12:23:03 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29]
2025/12/04 12:23:03 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6]
2025/12/04 12:23:03 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 80.6
2025/12/04 12:23:03 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:23:04 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 4 / 13 - Minibatch ==

Average Metric: 27.00 / 35 (77.1%): 100%|██████████| 35/35 [00:24<00:00,  1.43it/s]2025/12/04 12:23:28 INFO dspy.evaluate.evaluate: Average Metric: 27 / 35 (77.1%)
2025/12/04 12:23:28 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 77.14 on minibatch of size 35 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:23:28 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14]
2025/12/04 12:23:28 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6]
2025/12/04 12:23:28 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 80.6
2025/12/04 12:23:28 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:23:28 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 5 / 13 - Minibatch ==

Average Metric: 27.00 / 35 (77.1%): 100%|██████████| 35/35 [00:41<00:00,  1.19s/it]2025/12/04 12:24:10 INFO dspy.evaluate.evaluate: Average Metric: 27 / 35 (77.1%)
2025/12/04 12:24:10 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 77.14 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 2'].
2025/12/04 12:24:10 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14, 77.14]
2025/12/04 12:24:10 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6]
2025/12/04 12:24:10 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 80.6
2025/12/04 12:24:10 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:24:10 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 6 / 13 - Minibatch ==

Average Metric: 31.00 / 35 (88.6%): 100%|██████████| 35/35 [00:28<00:00,  1.22it/s]2025/12/04 12:24:38 INFO dspy.evaluate.evaluate: Average Metric: 31 / 35 (88.6%)
2025/12/04 12:24:38 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 88.57 on minibatch of size 35 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:24:38 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14, 77.14, 88.57]
2025/12/04 12:24:38 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6]
2025/12/04 12:24:38 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 80.6
2025/12/04 12:24:38 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:24:38 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 7 / 13 - Full Evaluation =====
2025/12/04 12:24:38 INFO dspy.teleprompt.mipro_optimizer_v2: Doing full eval on next top averaging program (Avg Score: 88.57) from minibatch trials...

Average Metric: 57.00 / 67 (85.1%): 100%|██████████| 67/67 [00:35<00:00,  1.91it/s]  2025/12/04 12:25:14 INFO dspy.evaluate.evaluate: Average Metric: 57 / 67 (85.1%)
2025/12/04 12:25:14 INFO dspy.teleprompt.mipro_optimizer_v2: [92mNew best full eval score![0m Score: 85.07
2025/12/04 12:25:14 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6, 85.07]
2025/12/04 12:25:14 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 85.07
2025/12/04 12:25:14 INFO dspy.teleprompt.mipro_optimizer_v2: =======================
2025/12/04 12:25:14 INFO dspy.teleprompt.mipro_optimizer_v2: 

2025/12/04 12:25:14 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 8 / 13 - Minibatch ==

Average Metric: 28.00 / 35 (80.0%): 100%|██████████| 35/35 [00:28<00:00,  1.22it/s]2025/12/04 12:25:42 INFO dspy.evaluate.evaluate: Average Metric: 28 / 35 (80.0%)
2025/12/04 12:25:42 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 80.0 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 0'].
2025/12/04 12:25:42 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14, 77.14, 88.57, 80.0]
2025/12/04 12:25:42 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6, 85.07]
2025/12/04 12:25:42 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 85.07
2025/12/04 12:25:42 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:25:42 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 9 / 13 - Minibatch ==

Average Metric: 26.00 / 35 (74.3%): 100%|██████████| 35/35 [00:28<00:00,  1.23it/s]2025/12/04 12:26:11 INFO dspy.evaluate.evaluate: Average Metric: 26 / 35 (74.3%)
2025/12/04 12:26:11 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 74.29 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:26:11 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14, 77.14, 88.57, 80.0, 74.29]
2025/12/04 12:26:11 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6, 85.07]
2025/12/04 12:26:11 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 85.07
2025/12/04 12:26:11 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:26:11 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 10 / 13 - Minibatch ==

Average Metric: 28.00 / 35 (80.0%): 100%|██████████| 35/35 [00:27<00:00,  1.29it/s]2025/12/04 12:26:38 INFO dspy.evaluate.evaluate: Average Metric: 28 / 35 (80.0%)
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 80.0 on minibatch of size 35 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 4'].
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14, 77.14, 88.57, 80.0, 74.29, 80.0]
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6, 85.07]
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 85.07
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: ==========================================


2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 11 / 13 - Minibatch ==

Average Metric: 27.00 / 35 (77.1%): 100%|██████████| 35/35 [00:00<00:00, 2206.83it/s]2025/12/04 12:26:38 INFO dspy.evaluate.evaluate: Average Metric: 27 / 35 (77.1%)
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 77.14 on minibatch of size 35 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14, 77.14, 88.57, 80.0, 74.29, 80.0, 77.14]
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6, 85.07]
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 85.07
2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: ==========================================


2025/12/04 12:26:38 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 12 / 13 - Minibatch ==

Average Metric: 24.00 / 35 (68.6%): 100%|██████████| 35/35 [00:36<00:00,  1.05s/it]2025/12/04 12:27:14 INFO dspy.evaluate.evaluate: Average Metric: 24 / 35 (68.6%)
2025/12/04 12:27:14 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 68.57 on minibatch of size 35 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 1'].
2025/12/04 12:27:14 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 74.29, 77.14, 77.14, 88.57, 80.0, 74.29, 80.0, 77.14, 68.57]
2025/12/04 12:27:14 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6, 85.07]
2025/12/04 12:27:14 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 85.07
2025/12/04 12:27:14 INFO dspy.teleprompt.mipro_optimizer_v2: ==========================================


2025/12/04 12:27:14 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 13 / 13 - Full Evaluation =====
2025/12/04 12:27:14 INFO dspy.teleprompt.mipro_optimizer_v2: Doing full eval on next top averaging program (Avg Score: 80.0) from minibatch trials...

Average Metric: 52.00 / 67 (77.6%): 100%|██████████| 67/67 [00:30<00:00,  2.16it/s]2025/12/04 12:27:45 INFO dspy.evaluate.evaluate: Average Metric: 52 / 67 (77.6%)
2025/12/04 12:27:45 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [80.6, 85.07, 77.61]
2025/12/04 12:27:45 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 85.07
2025/12/04 12:27:45 INFO dspy.teleprompt.mipro_optimizer_v2: =======================
2025/12/04 12:27:45 INFO dspy.teleprompt.mipro_optimizer_v2: 

2025/12/04 12:27:45 INFO dspy.teleprompt.mipro_optimizer_v2: Returning best identified program with score 85.07!

Optimized validation metrics: {'f1_macro': 0.8499103942652331, 'accuracy': 0.8507462686567164, 'precision': 0.896551724137931, 'recall': 0.7878787878787878, 'f1_binary': 0.8387096774193549, 'f1_micro': 0.8507462686567164}