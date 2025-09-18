# Solution
We were given a web service that allowed uploading "plugins".
Plugins were .plugin files (actually encrypted ZIPs) containing a manifest, a Python init.py, and assets. The server would decrypt, extract, and execute init.py upon upload.

Further inspection of the server source revealed, a hard-coded 32-byte AES key: SECRET_KEY!123456XXXXXXXXXXXXXXX, the encryption format being: "IV (16 bytes) + AES-CBC(ciphertext(padded_zip))".
After decryption, the server simply zipfile.extractall() into /opt/app/plugins/<uuid>/. Thus, .plugin is just an AES-CBC–encrypted ZIP.

The script helps us exploit the vulnerability.

## Flag
Flag: CTF{9fb64c8a4d81f9d0e1f4108467bee58db112d0d1457fa3716cc6a46231803686}
