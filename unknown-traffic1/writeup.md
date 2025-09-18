# Solution
The ICMP echo payloads contain many zero (0) bytes with occasional short letter-bearing chunks. They are numeric prefix + Base64 fragments.
We can extract them with the help of tshark:
"tshark -r unknown-traffic1.pcap -Y "icmp.type==8" -T fields -e data.data > payloads_hex.txt
"

When you strip the numeric prefixes and Base64-decode the fragments, you get small ASCII hex pieces and one ctf{ fragment.
The script provided helps us clean the data and find the flag.
(the middle part is cut off and appears to the end)

## Flag
Flag: ctf{72c8c1090e0bba717671f79de6e941a281e2f51da29865722f98c9fa3b7160e5}
