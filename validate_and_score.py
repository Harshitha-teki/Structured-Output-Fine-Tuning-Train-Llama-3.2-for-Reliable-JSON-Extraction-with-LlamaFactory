"""Helper: validate model outputs and compute parse success metrics locally.

Usage:
 - python validate_and_score.py --responses eval/baseline_responses.md --out eval/baseline_scores.csv

This script extracts response blocks from a markdown file, attempts json.loads on each, and writes a CSV with basic metrics.
"""
import argparse
import json
import re
import csv


def extract_blocks(md_path: str):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    parts = re.split(r"^([\w\-]+\.txt)\s*$", text, flags=re.M)
    blocks = []
    for i in range(1, len(parts), 3):
        filename = parts[i].strip()
        content = parts[i+1].strip()
        blocks.append((filename, content))
    return blocks


def safe_parse_json(s: str):
    s = s.strip()
    s = re.sub(r"^```(?:json)?\n", "", s)
    s = re.sub(r"\n```$", "", s)
    try:
        obj = json.loads(s)
        return True, obj, None
    except Exception as e:
        return False, None, str(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--responses', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()

    blocks = extract_blocks(args.responses)

    invoice_keys = ["vendor","invoice_number","date","due_date","currency","subtotal","tax","total","line_items"]
    po_keys = ["buyer","supplier","po_number","date","delivery_date","currency","total","items"]

    rows = []
    for filename, raw in blocks:
        first50 = raw.replace('\n', ' ')[:50]
        is_valid, obj, err = safe_parse_json(raw)
        has_all = False
        key_acc = 0.0
        val_acc = 0.0
        notes = ''
        schema_keys = invoice_keys if 'invoice' in filename.lower() else po_keys
        if is_valid:
            missing = [k for k in schema_keys if k not in obj]
            has_all = len(missing) == 0
            key_acc = (len(schema_keys) - len(missing)) / len(schema_keys)
            # crude value accuracy: count presence only
            val_acc = key_acc
        else:
            notes = f'parse_error: {err}'
        rows.append([filename, first50, str(is_valid).upper(), str(has_all).upper(), f"{key_acc:.2f}", f"{val_acc:.2f}", notes])

    with open(args.out, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['filename','raw_output_first_50_chars','is_valid_json','has_all_required_keys','key_accuracy','value_accuracy','notes'])
        writer.writerows(rows)

    print(f'Wrote {len(rows)} rows to {args.out}')


if __name__ == '__main__':
    main()
