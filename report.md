# Final Report

## Executive summary

This project produced a focused 80-example curated dataset (50 invoices, 30 purchase orders) and supporting artifacts to fine-tune Llama 3.2 via parameter-efficient LoRA adapters. The objective is deterministic, schema-compliant JSON extraction from unstructured invoices and purchase orders. The repository includes schemas, curated training data, a curation log, training configuration notes, validation tooling, evaluation templates, and prompt-engineering artifacts to support reproducible fine-tuning and analysis.

## Dataset and curation highlights

- `schema/invoice_schema.md` and `schema/po_schema.md` define strict field names, types, and absent-field conventions (use JSON null for missing numeric/date values; use empty string only for textual placeholders).
- `data/curated_train.jsonl` contains 80 curated examples consistent with those schemas. `data/curation_log.md` records curation decisions and edge cases.
- `scripts/generate_full_dataset.py` allows programmatic regeneration of the dataset; `scripts/dataset_tools.py` provides checksum and quick validation utilities.

## Baseline performance

- Baseline model responses should be collected in `eval/baseline_responses.md` (held-out 20 examples). Use `validate_and_score.py` to generate `eval/baseline_scores.csv` and capture parse/coverage metrics.

## Fine-tuning setup and results

- Training recommendations are documented in `training_config.md` (LoRA: r=16, alpha=32, lr=2e-4, epochs=3, sensible batch size). Use FP16 where possible and checkpoint regularly.
- Placeholders for `screenshots/training_config.png` and `screenshots/loss_curve.png` are present; swap these for real screenshots captured during training in LlamaFactory.

## Failure analysis summary

- `eval/failures/` contains templates for five detailed failure analyses. After evaluation, populate these with representative cases demonstrating common extraction mistakes (missing keys, wrong numeric types, date misparsing, and multi-line item issues).

## Prompting vs. Fine-Tuning (approx. 300 words)

Prompting is a fast, low-cost technique for guiding large language models to output structured text. A well-crafted prompt, possibly with a few in-context examples, can produce good results for many extraction tasks without any training. This approach is particularly effective when the input documents are close to the examples used in the prompt and the target schema is simple. Prompt engineering allows rapid iteration and minimal compute cost — it’s ideal for prototyping or when only occasional extraction is needed.

However, prompting is inherently brittle for strict, production-grade extraction. It relies on the model to follow instructions without explicit parameter updates, so small changes in document style, layout, or phrasing can cause schema violations: missing keys, wrong types (strings versus numbers), or inconsistent date formats. Enforcing exact JSON formatting and types by prompt alone often requires complex prompt constructs and post-processing heuristics, which increase engineering overhead and still leave failure modes.

Fine-tuning with LoRA addresses these limitations by updating model parameters to internalize the mapping from document text to structured JSON. Compared to prompting, fine-tuning produces more stable and repeatable outputs, increases parse-success rates, and better enforces schema conventions across varied inputs. The downside is the compute cost and the need for a carefully curated training set to avoid overfitting. For this reason, a hybrid workflow is recommended: use prompting to prototype and generate candidate pairs, curate the dataset, then perform LoRA fine-tuning to obtain robust behavior. For strict JSON extraction at scale, fine-tuning plus light prompt wrappers (for schema toggles) typically delivers the best mix of reliability, maintainability, and inference performance.

## Conclusions and next steps

- The repository now contains the required artifacts for dataset curation, training setup, evaluation templates, and failure-analysis scaffolding.
- Next actionable steps: run LlamaFactory with `data/curated_train.jsonl` and the recommended LoRA settings, capture training screenshots and loss curves, collect baseline and finetuned outputs for 20 held-out documents, run `validate_and_score.py` to produce CSVs, and complete the `eval/failures/` analyses using representative failing cases.

---

Files and directories of interest: `schema/`, `data/`, `eval/`, `prompts/`, `training_config.md`, `report.md`
