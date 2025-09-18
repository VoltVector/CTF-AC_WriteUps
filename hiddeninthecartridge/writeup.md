# Solution
Since this is a .nes ROM, running "strings" help us find out if there are any embedded messages.
Among them, the are some repeating sequences like: "66$$$32$$$35$$$38"
To get the flag, we removed the '$' from the sequence, and then we convert from hex to a clear format.

## Flag
Flag: ctf{9f1b438164dbc8a6249ba5c66fc0d6195b5388beed890680bf616021f2582248}
