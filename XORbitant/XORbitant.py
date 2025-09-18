#!/usr/bin/env python3
import re
from collections import Counter

CIPHER_PATH = "out.bin"
KEYLEN = 69

def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()

data = read_bytes(CIPHER_PATH)
n = len(data)

key = bytearray(KEYLEN)
for pos in range(KEYLEN):
    counts = Counter()
    for i in range(pos, n, KEYLEN):
        counts[data[i] ^ 0x20] += 1
    key[pos] = counts.most_common(1)[0][0]

key_ascii = key.decode('latin-1', errors='replace')
print("Candidate key (space-mode):", key_ascii)

if re.fullmatch(r'CTF\{[0-9a-f]{64}\}', key_ascii):
    dec = bytes(data[i] ^ key[i % KEYLEN] for i in range(n))
    open("decrypted_spacekey.bin", "wb").write(dec)
else:
    print("Doesn't match CTF{64hex}.")

def is_printable(b):
    return (32 <= b < 127) or b in (9,10,13)

best_key = bytearray(KEYLEN)
for pos in range(KEYLEN):
    best_k = 0
    best_score = -1.0
    for k in range(256):
        cnt = tot = 0
        for i in range(pos, min(n, pos + 2000000), KEYLEN):
            v = data[i] ^ k
            tot += 1
            if is_printable(v):
                cnt += 1
        score = cnt / tot if tot else 0.0
        if score > best_score:
            best_score = score
            best_k = k
    best_key[pos] = best_k

best_key_ascii = best_key.decode('latin-1', errors='replace')
print("Printable-score candidate key:", best_key_ascii)

m = re.fullmatch(r'CTF\{([0-9a-f]{64})\}', best_key_ascii)
if m:
    print("Found matching key:", best_key_ascii)
    dec = bytes(data[i] ^ best_key[i % KEYLEN] for i in range(n))
    open("decrypted_bestkey.bin", "wb").write(dec)
else:
    print("No direct perfect match.")
