# Solution
Opening the pcap in Wireshark shows many repeated HTTP GET requests of the form: "GET /data?chunk=123&data=VGhpcy1pc...", where each request has two parameters:
 - chunk = an index number
 - data = a base64-like string

To reconstruct the hidden data, we extract all (chunk, data) pairs. For each index, keep the most frequently seen value (since there's a chance there are duplicates)
Then, we sort by chunk index, concatenate all data strings and base64-decode the result.

The decoded bytes strat with: 89 50 4E 47 0D 0A 1A 0A. This is the PNG magic header. The image is a QR-code. Reading it will reveal us the flag.

## Flag

Flag: ctf{da8978b239f7e78370c36501ee6a0458e7c4dd870463e44ca6f9b949549ebf1b}
