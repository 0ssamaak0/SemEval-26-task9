# slides
Shared-encoder multi-task learning (MTL)
Shared-Encoder Multi-Task Learning with Strict Hierarchical Inference
Strict Hierarchical Gated Multitask learning
Hierarchically-Gated Multi-Task Learning with a Shared Encoder (HG-MTL)

We follow the general line of hierarchical multi-task learning where a shared encoder feeds multiple task-specific heads for related subtasks, as in hierarchical text classification and hate-speech systems.
Our setup is closest to AlKhamissi & Diab (2022), who jointly model offensive language, hate speech, and fine-grained hate categories with shared parameters and apply a self-consistency correction step over the hierarchy of subtasks.
Similar ideas of hierarchy-aware or conditional multi-task prediction appear in hierarchical patent classification with multi-task transformers  ￼ and in conditional multi-task toxicity detection  ￼.
We adopt a particularly strict hierarchical gating: if the top-level “polarized vs. non-polarized” head predicts non-polarized, we zero out all lower-level type and manifestation labels, enforcing hierarchy consistency at inference time.



# Ideas
- Use AlDi to visualize train data ✅
- ARBERT: MSA & MARBERT: Dialects (Merging?)
- DSPY
- Adapters? 
- Aux task learning e.g., Sentiment?

# MLT No gate
https://gemini.google.com/app/e857eeb52a287c91


# Dsearchers
- Gemini: https://gemini.google.com/share/c0a27c2a3eeb
- ChatGPT: https://chatgpt.com/share/6930107a-a47c-8000-a8f1-8d780935eefa
- PPL: https://www.perplexity.ai/search/i-want-you-to-help-me-with-a-r-i3CXW6upS.2McwauOGJQBw#0


- Gated Hierarchical Multi-Task Learning (GH-MTL): explicitly models the logical dependencies between subtasks. (DeBERTa-v3 for English and MARBERTv2 for Arabic), integrated via late-fusion ensembling.
- we advocate for the application of Asymmetric Loss (ASL) and Supervised Contrastive Learning (SCL), alongside SetFit (Sentence Transformer Fine-tuning)
- Model Ensemble

# Qs
- Model Size Limitations
- External & Synthetic Data? Reannoation etc.
<!-- - Can I participate in the competition using only 1 or 2 languages? -->

# TODOs
- Use ACL Tempelate
