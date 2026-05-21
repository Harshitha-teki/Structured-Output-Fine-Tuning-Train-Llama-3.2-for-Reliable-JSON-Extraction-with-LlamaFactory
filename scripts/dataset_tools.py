import json
from pathlib import Path
import hashlib

ROOT = Path(__file__).parents[1]
DATA = ROOT / 'data' / 'curated_train.jsonl'

def checksum_file(p: Path):
    h = hashlib.sha256()
    for chunk in p.read_bytes().splitlines():
        h.update(chunk)
    return h.hexdigest()

def quick_validate(p: Path = DATA):
    lines = p.read_text(encoding='utf-8').strip().splitlines()
    ok = True
    for i, L in enumerate(lines, 1):
        try:
            obj = json.loads(L)
        except Exception as e:
            print('line', i, 'not json:', e)
            ok = False
            continue
        if 'output' not in obj:
            print('line', i, 'missing output')
            ok = False
            continue
        try:
            json.loads(obj['output'])
        except Exception as e:
            print('line', i, 'output not json:', e)
            ok = False
    if ok:
        print('quick-validate: OK')
    else:
        print('quick-validate: FAIL')

if __name__ == '__main__':
    print('Checksum:', checksum_file(DATA))
    quick_validate()
