# Before vs After: Baseline vs Finetuned

This document summarizes the quick parse/structure comparisons between the base Llama 3.2 outputs and the fine-tuned model outputs using `validate_and_score.py`.

Current summary (auto-generated):

- Baseline CSV: `eval/baseline_scores.csv`
- Finetuned CSV: `eval/finetuned_scores.csv`

- Total baseline rows: 1
- Total finetuned rows: 1

- Baseline parse-success rate: 0 / 1 = 0.0
- Finetuned parse-success rate: 0 / 1 = 0.0

Notes:

- Both response files currently contain placeholder text (not valid JSON). After you run the baseline and the finetuned model on the held-out 20 documents and paste the verbatim responses into `eval/baseline_responses.md` and `eval/finetuned_responses.md`, re-run:

```powershell
python validate_and_score.py --responses eval/baseline_responses.md --out eval/baseline_scores.csv
python validate_and_score.py --responses eval/finetuned_responses.md --out eval/finetuned_scores.csv
```

- Then refresh this comparison by re-running the script or re-generating this file.

Interpretation guide (quick):

- Parse-success rate = fraction of responses that were valid JSON.
- Key coverage = average key_accuracy from the CSV (higher is better).
- Value accuracy = approximate (presence-based) accuracy; refine with field-level checks if needed.

Next steps (automated):

- I can automatically re-run the scoring and update this file whenever you paste real model responses. If you'd like that automation, say so and I'll wire a small watcher script.
# Before vs After: Parse Success Comparison

Metric | baseline (base model) | post fine-tuning
---|---:|---:
parse success rate | TBD | TBD
avg key accuracy | TBD | TBD
avg value accuracy | TBD | TBD
responses with markdown fences | TBD | TBD
responses with prose preamble | TBD | TBD
responses with wrong schema keys | TBD | TBD

Fill in the numeric values after running the baseline and fine-tuned evaluations and computing the CSV aggregates.
