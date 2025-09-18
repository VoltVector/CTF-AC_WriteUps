# Solution
"enc.py" does a bytewise XOR of plaintext with the key bytes, repeating the key accross the plaintext. In other words, it is repeated-key XOR (equivalently: Vigenère over bytes). This implies:

- If the key length L is known (or guessed), then bytes at plaintext positions congruent modulo L were XORed with the same single key byte. Therefore each such column is a separate single-byte XOR problem.

- Single-byte XOR can be attacked by trying all 256 byte values and scoring the result for how "plaintext-like" it becomes.

The provided "decode.py" assumes KEYLEN = 69 and looks for a CTF{[0-9a-f]{64}} formatted key.

## Flag
Flag: CTF{940a422746b832e652a991d88d31eb4d0ab2774a1f9a637e746b9226dfd44bca}
