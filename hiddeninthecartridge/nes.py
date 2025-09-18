#!/usr/bin/env python3
import re
from pathlib import Path

fn = Path("./space_invaders.nes")
data = fn.read_bytes()

text = data.decode("latin-1", errors="ignore")

pattern = re.compile(r'(?:[0-9a-fA-F]{2}\$\$\$)+[0-9a-fA-F]{2}')

matches = pattern.findall(text)
decoded_parts = []
for m in matches:
    hexstr = m.replace('$$$', '')
    try:
        b = bytes.fromhex(hexstr)
        decoded = b.decode('utf-8', errors='replace')
        decoded_parts.append(decoded)
    except ValueError:
        continue

result = ''.join(decoded_parts)
print(result)
