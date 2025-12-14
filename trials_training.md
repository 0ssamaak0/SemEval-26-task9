# Basic Models

## Bert base uncased ENG - Bert base uncased ARB

### Task 1
Language,Accuracy,Precision,Recall,F1 Binary,F1 Macro,F1 Micro
AR,0.6805,0.5963,0.8667,0.7065,0.6779,0.6805
EN,0.7812,0.74,0.6271,0.6789,0.7565,0.7812

### Task 2
Language,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro
AR,0.0432,0.0324,0.375,0.075,0.0229,0.0207
EN,0.1879,0.187,0.2222,0.2462,0.1628,0.2514

### Task 3
Language,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro,Exact Match
AR,0.3376,0.2119,0.4258,0.2148,0.2797,0.2445,0.4201
EN,0.3929,0.3161,0.5,0.4121,0.3235,0.2973,0.5875

## cardiffnlp/twitter-roberta-base-hate ENG - UBC-NLP/MARBERTv2 ARB

### Task 1
Language,Accuracy,Precision,Recall,F1 Binary,F1 Macro,F1 Micro
AR,0.7929,0.7439,0.8133,0.7771,0.7918,0.7929
EN,0.825,0.7627,0.7627,0.7627,0.812,0.825

### Task 2
Language,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro
AR,0.3426,0.3714,0.4353,0.4704,0.2824,0.3243
EN,0.1569,0.1295,0.1791,0.2393,0.1395,0.1971

### Task 3
Language,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro,Exact Match
AR,0.4697,0.3938,0.5812,0.6717,0.3941,0.3835,0.5266
EN,0.4271,0.3657,0.504,0.4725,0.3706,0.3552,0.6

# Gated Training

## BERT base uncased ENG - BERT base uncased ARB

### Task 1
Language,Accuracy,Precision,Recall,F1 Binary,F1 Macro,F1 Micro
AR,0.6627,0.6154,0.64,0.6275,0.6597,0.6627
EN,0.7875,0.7119,0.7119,0.7119,0.7718,0.7875

### Task 2
Language,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro
AR,0.1111,0.0646,0.2903,0.1155,0.0687,0.0471
EN,0.5441,0.1612,0.74,0.3469,0.4302,0.1384

### Task 3
Language,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro,Exact Match
AR,0.3915,0.2553,0.5211,0.3426,0.3136,0.2187,0.4734
EN,0.4103,0.2978,0.5437,0.4289,0.3294,0.2604,0.6

## microsoft/deberta-v3-base ENG - UBC-NLP/MARBERTv2 ARB

# microsoft/deberta-v3-base ENG - UBC-NLP/MARBERTv2 ARB

## Task 1
Language,Lang_Name,Accuracy,Precision,Recall,F1 Binary,F1 Macro,F1 Micro
AR,Arabic,0.8047,0.7561,0.8267,0.7898,0.8037,0.8047
EN,English,0.7688,0.6774,0.7119,0.6942,0.7541,0.7688

## Task 2
Language,Lang_Name,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro
AR,Arabic,0.4554,0.3843,0.6479,0.6889,0.3511,0.2986
EN,English,0.5734,0.1426,0.7193,0.1439,0.4767,0.1414

## Task 3
Language,Lang_Name,F1 Micro,F1 Macro,Precision Micro,Precision Macro,Recall Micro,Recall Macro,Exact Match
AR,Arabic,0.5132,0.3697,0.6831,0.5208,0.411,0.306,0.5503
EN,English,0.4808,0.367,0.5282,0.432,0.4412,0.3598,0.5875

# Gated inference Only
## FacebookAI/xlm-roberta-large ENG - UBC-NLP/MARBERTv2 ARB

## Task 1

Language	Accuracy	Precision	Recall	F1 Binary	F1 Macro	F1 Micro
AR
Arabic
0.8107	0.7867	0.7867	0.7867	0.8082	0.8107
EN
English
0.7688	0.7115	0.6271	0.6667	0.7448	0.7688

## Task 2

Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro
AR
Arabic
0.5734	0.5602	0.529	0.5255	0.626	0.6022
EN
English
0.4104	0.3393	0.3022	0.2791	0.6395	0.6228

## Task 3

Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro	Exact Match
AR
Arabic
0.6231	0.5819	0.5704	0.5254	0.6864	0.6679	0.5325
EN
English
0.4416	0.4285	0.3455	0.3434	0.6118	0.6018	0.5375


# Gated Inference Ensemble (Arabic Only)
# Use the plot


# Augmentation MARBERT

## Task 1

Language	Accuracy	Precision	Recall	F1 Binary	F1 Macro	F1 Micro
AR
Arabic
0.8402	0.8	0.8533	0.8258	0.8391	0.8402

## Task 2

Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro
AR
Arabic
0.6174	0.5955	0.5509	0.5392	0.7023	0.6718

## Task 3

Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro	Exact Match
AR
Arabic
0.6543	0.6072	0.5828	0.5381	0.7458	0.7101	0.5325


# Soft Gating
## cardiffnlp/twitter-roberta-base-hate ENG - UBC-NLP/MARBERTv2 ARB

### Task 1
Language	Accuracy	Precision	Recall	F1 Binary	F1 Macro	F1 Micro
AR
Arabic
0.8107	0.7867	0.7867	0.7867	0.8082	0.8107
EN
English
0.8	0.7455	0.6949	0.7193	0.782	0.8

### Task 2
Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro
AR
Arabic
0.5662	0.5621	0.4742	0.4788	0.7023	0.697
EN
English
0.587	0.4175	0.551	0.375	0.6279	0.4973

### Task 3

Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro	Exact Match
AR
Arabic
0.6112	0.569	0.5331	0.4984	0.7161	0.7207	0.5266
EN
English
0.5155	0.4984	0.4337	0.4251	0.6353	0.6255	0.5562


# Thresholds (MTL_Thresholds)

## cardiffnlp/twitter-roberta-base-hate ENG - UBC-NLP/MARBERTv2 ARB

### Task 1


Language	Accuracy	Precision	Recall	F1 Binary	F1 Macro	F1 Micro
AR
Arabic
0.8107	0.7867	0.7867	0.7867	0.8082	0.8107
EN
English
0.85	0.7692	0.8475	0.8065	0.842	0.85


### Task 2


Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro
AR
Arabic
0.5814	0.5969	0.5906	0.6257	0.5725	0.5794
EN
English
0.7	0.4493	0.6702	0.4187	0.7326	0.4877


### Task 3

Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro	Exact Match
AR
Arabic
0.6122	0.5718	0.5906	0.5513	0.6356	0.5951	0.5207
EN
English
0.5323	0.4956	0.4612	0.4364	0.6294	0.5907	0.55

# Final Submission
## Arabic: MARBERTv2, no thresholds
## English: cardiffnlp/twitter-roberta-base-hate, MTL_Thresholds_1

### Task 1
Language	Accuracy	Precision	Recall	F1 Binary	F1 Macro	F1 Micro
AR
Arabic
0.8402	0.8	0.8533	0.8258	0.8391	0.8402
EN
English
0.85	0.7692	0.8475	0.8065	0.842	0.85

### Task 2
Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro
AR
Arabic
0.6174	0.5955	0.5509	0.5392	0.7023	0.6718
EN
English
0.7	0.4493	0.6702	0.4187	0.7326	0.4877

### Task 3

Language	F1 Micro	F1 Macro	Precision Micro	Precision Macro	Recall Micro	Recall Macro	Exact Match
AR
Arabic
0.6543	0.6072	0.5828	0.5381	0.7458	0.7101	0.5325
EN
English
0.5323	0.4956	0.4612	0.4364	0.6294	0.5907	0.55


# DSPY Trials