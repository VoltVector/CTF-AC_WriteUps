# Solution
This challenge gives us 3 long hex blocks labeled P1, P2, P3. Additionally, it makes a hint towards RSA in the description.
The first thing that helped us decode the flag is the consistent formatted shares (all of them start with 80..).
The XOR of the three same-length byte strings gives us printable bytes that decode cleanly with a few formats.
(We have to go through other formats such as "latin-1", "utf-16be", etc.)
By running the script, formats like "utf-8" and "latin-1" help us fully decode and complete the challenge.

## Flag
Flag: ctf{d6b72529c6177d8f648ae85f624a24d6f1edce5ca29bd7cc0b888e117a123892}
