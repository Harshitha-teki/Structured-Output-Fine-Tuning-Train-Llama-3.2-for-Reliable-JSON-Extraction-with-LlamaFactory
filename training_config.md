# Training Configuration and Justification

Model: Llama-3.2-3B-Instruct (loaded in LlamaFactory)
Fine-tuning method: LoRA (parameter-efficient adapter-based fine-tuning)

Proposed hyperparameters (initial run):
- LoRA rank: 16 — Reason: medium rank balances capacity to learn formatting rules without overfitting on 80 examples.
- LoRA alpha: 32 — Reason: use 2x rank as a standard scaling heuristic that stabilises updates.
- Learning rate: 2e-4 — Reason: conservative mid-range LR for LoRA on small datasets; avoids large steps that memorise examples.
- Epochs: 3 — Reason: dataset of 80 examples; 2–3 epochs should allow learning format without severe overfitting.
- Batch size: Depends on available RAM; start with 8 and increase if resources permit. Use gradient accumulation if single-GPU/CPU RAM is constrained.

Logging & checkpoints:
- Save checkpoint every 500 steps; monitor validation loss on a small held-out subset (10% of training set) to detect overfitting.

Justify tradeoffs:
- Rank 16 chosen to provide enough capacity for structured format learning (JSON constraints) and modest generalisation across layouts. Rank 8 may underfit; rank 32 risks overfitting on 80 examples.
- LR 2e-4 is safe for LoRA with rank 16; higher LR (3e-4) may converge faster but increases overfitting risk.

Screenshots to capture (place in screenshots/):
- training_config.png: full UI panel showing dataset selection and hyperparameters.
- loss_curve.png: final training loss curve.
