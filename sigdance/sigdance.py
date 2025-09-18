#!/usr/bin/env python3
import socket, re, time

HOST = "ctf.ac.upt.ro"
PORT = 9245
A = 0
U = 13
MAX_ATTEMPTS = 5

pat = re.compile(rb"Hello from pid8\s*=\s*(\d+)")

for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        with socket.create_connection((HOST, PORT), timeout=5) as s:
            s.settimeout(5.0)
            buf = b""
            while True:
                part = s.recv(1024)
                if not part:
                    raise ConnectionResetError("server closed connection before greeting")
                buf += part
                m = pat.search(buf)
                if m:
                    break

            pid_low = int(m.group(1))
            token = (A << 16) ^ (U << 8) ^ (pid_low & 255)
            print(f"Got pid8={pid_low}, sending token={token}")

            s.sendall(f"{token}\n".encode())

            resp = []
            while True:
                try:
                    data = s.recv(4096)
                except socket.timeout:
                    break
                if not data:
                    break
                resp.append(data)
            output = b"".join(resp).decode(errors="ignore")
            print(output, end="")
            break

    except (ConnectionResetError, socket.timeout) as e:
        print(f"[attempt {attempt}] connection error: {e!s}; retrying...")
        time.sleep(0.6)
else:
    print("All attempts failed.")
