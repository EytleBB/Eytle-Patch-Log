#!/usr/bin/env python3
"""Generate the newest-first date index; run from any working directory."""
import json
import re
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'logs'
dates = sorted((p.stem for p in root.iterdir() if p.is_file() and re.fullmatch(r'\d{4}-\d{2}-\d{2}\.txt', p.name)), reverse=True)
for value in dates:
    date.fromisoformat(value)
(root / 'index.json').write_text(json.dumps(dates, separators=(',', ':')), encoding='utf-8')
print(f'{len(dates)} log entries indexed')
