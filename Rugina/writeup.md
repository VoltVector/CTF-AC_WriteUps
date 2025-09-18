# Solution
The name hints at Rust, so trying to input something Rust related gives us this error: "Eroare de sintaxă: Sunt permise doar cuvintele-cheie rugina-like, nu Rust clasic."  (broadly translated as "Syntax error: Only Rust-like keywords are allowed, not classic Rust)
Sending nothing gives us another error: "Eroare de sintaxă: Programul trebuie să definească funcția de intrare: `principal`." (It should start with the `principal` function) 
What the challenge seems to explain is that all of the main functions have been "translated" to romanian. This is tricky since "write", "read" or "println" can have a lot of meanings. The only think we can do now is to try
different words and see which one helps us read the flag file.
After a few tries, this code will reveal the flag: 

``py
principal() {
    scrie!(include_str!("/flag.txt"));
}
``

## Flag
Flag: ctf{73523e676b04e1c2db176d8035648893648b969f5ddf5ac40f8fc5b6c15d8692}

