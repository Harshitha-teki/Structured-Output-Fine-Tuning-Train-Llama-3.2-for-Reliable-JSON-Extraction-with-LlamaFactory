# Training Checklist

- [ ] Confirm `data/curated_train.jsonl` contains 80 lines (50 invoices, 30 POs).
- [ ] Run `python scripts/dataset_tools.py` to get checksum and quick validation.
- [ ] Upload `data/curated_train.jsonl` to LlamaFactory UI and set LoRA hyperparams as in README.
- [ ] Start training with FP16, monitor loss, and save checkpoints.
- [ ] After training, run 20 held-out examples and save outputs to `eval/finetuned_responses.md`.
- [ ] Run `python validate_and_score.py` to create `eval/finetuned_scores.csv` and compare with baseline.
