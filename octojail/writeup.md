# Solution
The service reads a single line of input consisting only of octal digits, grouped in triplets (each triplet = one byte). It decodes that into raw bytes and threats them as a tar archive. The server extracts safe members from the tar into uploads/ and then tries to import and run() a plugin.py from uploads/plugin.py (or plugin.py).
The extracted plugin.py is executed by the service and therefore can access arbitrary files the service process can read.

Any code in "run()" runs with the server's privileges, and the safe_extract() only blocks absolute paths (name.startswith("/")) and .. in names, but allows simple filenames like plugin.py. That’s enough to place a file that the server then executes.
Additionally, the octal-triplet encoding is merely a transport constraint, not a security control. Once decoded, the server treats bytes as a normal tar file.

We can now create a script that attempts to open() the flag location, create an in-memory tar and encode the raw tar bytes into octal triplets.

## Flag
Flag: ctf{0331641fadb35abb1eb5a9640fa6156798cba4538148ceb863dfb1821ac69000}
