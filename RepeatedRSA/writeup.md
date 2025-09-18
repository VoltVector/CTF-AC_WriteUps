# Solution
The challenge gave three RSA moduli n1, n2, n3, a public exponent e = 65537, and a ciphertext C which had been encrypted three times (sequentially) under the three public keys. Because the moduli share primes (n1 = p·q, n2 = p·r, n3 = q·r) the keys are trivially factorable using pairwise GCDs. Factoring the moduli yields the private exponents, and decrypting the ciphertext in reverse order recovers the plaintext flag.

## Flag
Flag: ctf{3c1315f63d550570a690f693554647b7763c3acbc806ae846ce8d25b5f364d10}
