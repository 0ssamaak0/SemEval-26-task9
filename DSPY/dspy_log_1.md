Bootstrapping set 1/6
Bootstrapping set 2/6
Bootstrapping set 3/6
  2%|▏         | 5/214 [00:05<04:03,  1.17s/it]
Bootstrapped 4 full traces after 5 examples for up to 1 rounds, amounting to 5 attempts.
Bootstrapping set 4/6
  2%|▏         | 4/214 [00:04<04:01,  1.15s/it]
Bootstrapped 4 full traces after 4 examples for up to 1 rounds, amounting to 4 attempts.
Bootstrapping set 5/6
  2%|▏         | 5/214 [00:05<04:04,  1.17s/it]
Bootstrapped 4 full traces after 5 examples for up to 1 rounds, amounting to 5 attempts.
Bootstrapping set 6/6
  1%|          | 2/214 [00:02<03:45,  1.07s/it]
2025/12/04 11:59:19 INFO dspy.teleprompt.mipro_optimizer_v2: 
==> STEP 2: PROPOSE INSTRUCTION CANDIDATES <==
2025/12/04 11:59:19 INFO dspy.teleprompt.mipro_optimizer_v2: We will use the few-shot examples from the previous step, a generated dataset summary, a summary of the program code, and a randomly selected prompting tip to propose instructions.
Bootstrapped 2 full traces after 2 examples for up to 1 rounds, amounting to 2 attempts.
2025/12/04 12:00:06 INFO dspy.teleprompt.mipro_optimizer_v2: 
Proposing N=3 instructions...

2025/12/04 12:00:35 INFO dspy.teleprompt.mipro_optimizer_v2: Proposed Instructions for Predictor 0:

2025/12/04 12:00:35 INFO dspy.teleprompt.mipro_optimizer_v2: 0: Polarization denotes stereotyping, vilification, dehumanization, deindividuation, or intolerance of other people’s views, beliefs, and identities. In this study, speeches and articles that are shared on social media that incite division, groupism, hatred, conflict, and intolerance are classified as containing polarization.
Given this sentence, classify it as containing polarization or not.

2025/12/04 12:00:35 INFO dspy.teleprompt.mipro_optimizer_v2: 1: Analyze the following sentence and determine its level of polarization. Classify it as "polarization" if it expresses extreme opinions that could incite conflict or division. Classify it as "no polarization" if it remains neutral and factual without any strong sentiments.

2025/12/04 12:00:35 INFO dspy.teleprompt.mipro_optimizer_v2: 2: Analyze the following sentence and determine if it expresses strong divisive opinions or if it is neutral. Classify the sentence as either "polarization" if it contains polarizing language or "no polarization" if it is neutral.

2025/12/04 12:00:35 INFO dspy.teleprompt.mipro_optimizer_v2: 

2025/12/04 12:00:36 INFO dspy.teleprompt.mipro_optimizer_v2: ==> STEP 3: FINDING OPTIMAL PROMPT PARAMETERS <==
2025/12/04 12:00:36 INFO dspy.teleprompt.mipro_optimizer_v2: We will evaluate the program over a series of trials with different combinations of instructions and few-shot examples to find the optimal combination using Bayesian Optimization.

2025/12/04 12:00:36 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 1 / 13 - Full Evaluation of Default Program ==
Average Metric: 48.00 / 53 (90.6%): 100%|██████████| 53/53 [00:00<00:00, 1728.98it/s]2025/12/04 12:00:36 INFO dspy.evaluate.evaluate: Average Metric: 48 / 53 (90.6%)
2025/12/04 12:00:36 INFO dspy.teleprompt.mipro_optimizer_v2: Default program score: 90.57

/Users/0ssamaak0/miniconda3/envs/nlp/lib/python3.13/site-packages/optuna/_experimental.py:32: ExperimentalWarning: Argument ``multivariate`` is an experimental feature. The interface can change in the future.
  warnings.warn(
2025/12/04 12:00:36 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 2 / 13 - Minibatch ==

Average Metric: 28.00 / 35 (80.0%): 100%|██████████| 35/35 [00:05<00:00,  6.74it/s]2025/12/04 12:00:41 INFO dspy.evaluate.evaluate: Average Metric: 28 / 35 (80.0%)
2025/12/04 12:00:41 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 80.0 on minibatch of size 35 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 3'].
2025/12/04 12:00:41 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0]
2025/12/04 12:00:41 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57]
2025/12/04 12:00:41 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 90.57
2025/12/04 12:00:41 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:00:41 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 3 / 13 - Minibatch ==

Average Metric: 29.00 / 35 (82.9%): 100%|██████████| 35/35 [00:05<00:00,  6.01it/s]2025/12/04 12:00:47 INFO dspy.evaluate.evaluate: Average Metric: 29 / 35 (82.9%)
2025/12/04 12:00:47 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 82.86 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 0'].
2025/12/04 12:00:47 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86]
2025/12/04 12:00:47 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57]
2025/12/04 12:00:47 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 90.57
2025/12/04 12:00:47 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:00:47 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 4 / 13 - Minibatch ==

Average Metric: 32.00 / 35 (91.4%): 100%|██████████| 35/35 [00:04<00:00,  7.32it/s]2025/12/04 12:00:51 INFO dspy.evaluate.evaluate: Average Metric: 32 / 35 (91.4%)
2025/12/04 12:00:51 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 91.43 on minibatch of size 35 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:00:51 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43]
2025/12/04 12:00:51 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57]
2025/12/04 12:00:51 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 90.57
2025/12/04 12:00:51 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:00:51 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 5 / 13 - Minibatch ==

Average Metric: 26.00 / 35 (74.3%): 100%|██████████| 35/35 [00:05<00:00,  6.66it/s] 2025/12/04 12:00:57 INFO dspy.evaluate.evaluate: Average Metric: 26 / 35 (74.3%)
2025/12/04 12:00:57 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 74.29 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 2'].
2025/12/04 12:00:57 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43, 74.29]
2025/12/04 12:00:57 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57]
2025/12/04 12:00:57 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 90.57
2025/12/04 12:00:57 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:00:57 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 6 / 13 - Minibatch ==

Average Metric: 30.00 / 35 (85.7%): 100%|██████████| 35/35 [00:04<00:00,  8.10it/s]2025/12/04 12:01:01 INFO dspy.evaluate.evaluate: Average Metric: 30 / 35 (85.7%)
2025/12/04 12:01:01 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 on minibatch of size 35 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:01:01 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43, 74.29, 85.71]
2025/12/04 12:01:01 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57]
2025/12/04 12:01:01 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 90.57
2025/12/04 12:01:01 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:01:01 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 7 / 13 - Full Evaluation =====
2025/12/04 12:01:01 INFO dspy.teleprompt.mipro_optimizer_v2: Doing full eval on next top averaging program (Avg Score: 91.43) from minibatch trials...

Average Metric: 49.00 / 53 (92.5%): 100%|██████████| 53/53 [00:03<00:00, 16.46it/s] 2025/12/04 12:01:04 INFO dspy.evaluate.evaluate: Average Metric: 49 / 53 (92.5%)
2025/12/04 12:01:04 INFO dspy.teleprompt.mipro_optimizer_v2: [92mNew best full eval score![0m Score: 92.45
2025/12/04 12:01:04 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57, 92.45]
2025/12/04 12:01:04 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 92.45
2025/12/04 12:01:04 INFO dspy.teleprompt.mipro_optimizer_v2: =======================
2025/12/04 12:01:04 INFO dspy.teleprompt.mipro_optimizer_v2: 

2025/12/04 12:01:04 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 8 / 13 - Minibatch ==

Average Metric: 29.00 / 35 (82.9%): 100%|██████████| 35/35 [00:02<00:00, 16.34it/s] 2025/12/04 12:01:07 INFO dspy.evaluate.evaluate: Average Metric: 29 / 35 (82.9%)
2025/12/04 12:01:07 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 82.86 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 0'].
2025/12/04 12:01:07 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43, 74.29, 85.71, 82.86]
2025/12/04 12:01:07 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57, 92.45]
2025/12/04 12:01:07 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 92.45
2025/12/04 12:01:07 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:01:07 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 9 / 13 - Minibatch ==

Average Metric: 35.00 / 35 (100.0%): 100%|██████████| 35/35 [00:04<00:00,  7.04it/s]2025/12/04 12:01:12 INFO dspy.evaluate.evaluate: Average Metric: 35 / 35 (100.0%)
2025/12/04 12:01:12 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:01:12 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43, 74.29, 85.71, 82.86, 100.0]
2025/12/04 12:01:12 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57, 92.45]
2025/12/04 12:01:12 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 92.45
2025/12/04 12:01:12 INFO dspy.teleprompt.mipro_optimizer_v2: =========================================


2025/12/04 12:01:12 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 10 / 13 - Minibatch ==

Average Metric: 25.00 / 35 (71.4%): 100%|██████████| 35/35 [00:05<00:00,  6.31it/s]2025/12/04 12:01:17 INFO dspy.evaluate.evaluate: Average Metric: 25 / 35 (71.4%)
2025/12/04 12:01:17 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 71.43 on minibatch of size 35 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 4'].
2025/12/04 12:01:17 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43, 74.29, 85.71, 82.86, 100.0, 71.43]
2025/12/04 12:01:17 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57, 92.45]
2025/12/04 12:01:17 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 92.45
2025/12/04 12:01:17 INFO dspy.teleprompt.mipro_optimizer_v2: ==========================================


2025/12/04 12:01:17 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 11 / 13 - Minibatch ==

Average Metric: 32.00 / 35 (91.4%): 100%|██████████| 35/35 [00:02<00:00, 17.28it/s]  2025/12/04 12:01:19 INFO dspy.evaluate.evaluate: Average Metric: 32 / 35 (91.4%)
2025/12/04 12:01:19 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 91.43 on minibatch of size 35 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 5'].
2025/12/04 12:01:19 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43, 74.29, 85.71, 82.86, 100.0, 71.43, 91.43]
2025/12/04 12:01:19 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57, 92.45]
2025/12/04 12:01:19 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 92.45
2025/12/04 12:01:19 INFO dspy.teleprompt.mipro_optimizer_v2: ==========================================


2025/12/04 12:01:19 INFO dspy.teleprompt.mipro_optimizer_v2: == Trial 12 / 13 - Minibatch ==

Average Metric: 30.00 / 35 (85.7%): 100%|██████████| 35/35 [00:05<00:00,  6.72it/s]2025/12/04 12:01:24 INFO dspy.evaluate.evaluate: Average Metric: 30 / 35 (85.7%)
2025/12/04 12:01:24 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 on minibatch of size 35 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 1'].
2025/12/04 12:01:24 INFO dspy.teleprompt.mipro_optimizer_v2: Minibatch scores so far: [80.0, 82.86, 91.43, 74.29, 85.71, 82.86, 100.0, 71.43, 91.43, 85.71]
2025/12/04 12:01:24 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57, 92.45]
2025/12/04 12:01:24 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 92.45
2025/12/04 12:01:24 INFO dspy.teleprompt.mipro_optimizer_v2: ==========================================


2025/12/04 12:01:24 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 13 / 13 - Full Evaluation =====
2025/12/04 12:01:24 INFO dspy.teleprompt.mipro_optimizer_v2: Doing full eval on next top averaging program (Avg Score: 95.715) from minibatch trials...

Average Metric: 50.00 / 53 (94.3%): 100%|██████████| 53/53 [00:01<00:00, 37.66it/s]   2025/12/04 12:01:26 INFO dspy.evaluate.evaluate: Average Metric: 50 / 53 (94.3%)
2025/12/04 12:01:26 INFO dspy.teleprompt.mipro_optimizer_v2: [92mNew best full eval score![0m Score: 94.34
2025/12/04 12:01:26 INFO dspy.teleprompt.mipro_optimizer_v2: Full eval scores so far: [90.57, 92.45, 94.34]
2025/12/04 12:01:26 INFO dspy.teleprompt.mipro_optimizer_v2: Best full score so far: 94.34
2025/12/04 12:01:26 INFO dspy.teleprompt.mipro_optimizer_v2: =======================
2025/12/04 12:01:26 INFO dspy.teleprompt.mipro_optimizer_v2: 

2025/12/04 12:01:26 INFO dspy.teleprompt.mipro_optimizer_v2: Returning best identified program with score 94.34!