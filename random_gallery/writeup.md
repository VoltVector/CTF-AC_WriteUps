# Solution
The challenge doesn't present too much in the beginning, and the source code doesn't provide much either.
We can try to bruteforce the login page, however, I decided to search for additional hidden directories through fuzzing.
There are many options here, and for this challenge I used `dirsearch`. It lead us to this page: "http://ctf.ac.upt.ro:9117/gallery/"
After that, we go to city -> haunts -> me and we find a qr code with the flag.

## Flag
Flag: ctf{1cd4daf060aee882653595cca4e719d48a3080cd1b76055812145da8a10b47e1}
