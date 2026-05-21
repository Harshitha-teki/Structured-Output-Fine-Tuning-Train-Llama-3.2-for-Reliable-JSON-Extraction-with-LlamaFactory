# Project: Structured Output Fine-Tuning (Llama 3.2)

This workspace contains curated training data, schema docs, evaluation templates, prompts, and helper scripts for the LlamaFactory fine-tuning exercise.

Quickstart:
1. Inspect `schema/` and `data/curated_train.jsonl`.
2. Upload `data/curated_train.jsonl` to LlamaFactory and follow `training_config.md`.
3. Run baseline and finetuned evaluations in the LlamaFactory inference tab and paste raw outputs into `eval/` files.
4. Use `validate_and_score.py` to compute parse success metrics.

LlamaFactory upload & LoRA training snippet
-----------------------------------------

1) Prepare dataset
- Ensure `data/curated_train.jsonl` is present and contains 80 JSONL lines (50 invoices, 30 POs). Each line must be a JSON object with keys: `instruction`, `input`, `output` where `output` is a JSON-string matching your schema.

2) In LlamaFactory (local Gradio UI)
- Model: choose Llama 3.2 (base) or nearest available.
- Task: Supervised Fine-Tuning (SFT) with LoRA adapter.
- Upload dataset: select `data/curated_train.jsonl`.

3) Recommended LoRA hyperparameters (start here, tune if needed)
- Rank (r): 16
- Alpha: 32
- Learning rate: 2e-4
- Batch size (per device): 16 (or highest that fits GPU memory)
- Epochs: 3
- Weight decay: 0.0
- Warmup steps: 100
- Save/checkpoint every epoch

4) Simple training checklist
- Confirm dataset encoding: UTF-8 without BOM.
- Confirm `output` strings are valid JSON (use `python -m json.tool` or the `validate_and_score.py` script).
- Use mixed-precision (fp16) if available.
- Monitor training loss; expect smooth decrease. If loss diverges, reduce lr by 2x and retry.
- After training, run the same 20 held-out examples in inference and save raw responses to `eval/finetuned_responses.md`.

5) Post-training evaluation
- Paste baseline raw responses into `eval/baseline_responses.md` and finetuned responses into `eval/finetuned_responses.md`.
- Run `validate_and_score.py` to produce CSV scores and compare `eval/baseline_scores.csv` vs `eval/finetuned_scores.csv`.

If you want, I can also generate a short one-page checklist PDF or prepare exact Gradio UI screenshots with instructions — say which you'd prefer.
