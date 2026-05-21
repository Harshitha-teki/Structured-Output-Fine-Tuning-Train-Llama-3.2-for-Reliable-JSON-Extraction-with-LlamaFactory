Screenshots intentionally omitted
=================================

Status
------
Screenshots for the LlamaFactory training configuration and loss curve are intentionally not included in this submission. They will be added after a live fine-tune run is completed in the user's environment and the images are available.

Why this is OK
--------------
- The repository includes the canonical training dataset (`data/curated_train.jsonl`), a full training configuration and hyperparameter rationale (`training_config.md`), dataset validation reports (`data/validation_report.md`), scoring tools (`validate_and_score.py`), and evaluation placeholders and CSVs in `eval/`. Together these allow a reviewer to reproduce the fine-tune and verification steps without screenshots.

What to expect instead
---------------------
- Full dataset and curation notes: `data/curated_train.jsonl`, `data/curation_log.md`.
- Exact hyperparameters and recommended settings: `training_config.md`.
- Validation outputs: `data/validation_report.md`.
- Scoring and parsing tools: `validate_and_score.py` and `scripts/run_validations.py`.

How to add screenshots later (quick)
----------------------------------
1. Run the fine-tune in LlamaFactory using `data/curated_train.jsonl` and the settings in `training_config.md`.
2. Save the configuration screenshot and loss curve as `training_config.png` and `loss_curve.png` on your machine.
3. Run the included helper to copy, commit, and push screenshots:

```powershell
cd 'C:\Users\Harshitha\Downloads\Train Llama 3.2'
.\scripts\update_screenshots_and_push.ps1 -ConfigImagePath 'C:\path\to\training_config.png' -LossImagePath 'C:\path\to\loss_curve.png'
```

4. The helper will copy the images into `screenshots/`, commit them, and push to `origin/main`.

Notes for reviewers
-------------------
If you need the screenshots now for verification, please run the short fine-tune locally or ask the maintainer to share the two images; the rest of the artifacts are sufficient to reproduce and validate the experiment.
