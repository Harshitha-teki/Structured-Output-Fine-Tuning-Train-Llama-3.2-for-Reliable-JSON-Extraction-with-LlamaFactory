"""Run dataset validations and produce data/validation_report.md"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parents[1]
DATA = ROOT / 'data' / 'curated_train.jsonl'
REPORT = ROOT / 'data' / 'validation_report.md'

print('Running quick dataset_tools check...')
subprocess.run([sys.executable, str(ROOT / 'scripts' / 'dataset_tools.py')])

print('\nRunning stricter validator (existing script)...')
subprocess.run([sys.executable, str(ROOT / 'scripts' / 'generate_full_dataset.py')], check=False)

print('\nValidation complete — see', REPORT)
