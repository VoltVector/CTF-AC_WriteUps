# Solution
The program installs signal handlers and maintains two counters:
    A - increments on SIGALRM (ac in the C code)
    U - increments on SIGUSR1 (uc in the C code)

A helper thread sengs SIGUSR1 to the main thread several times (13 times in the code)
Additionally, there is a repeating timer set up to raise SIGALRM. In the binary, either the timer never increments A before verification or A ends up 0.
The service also prints the low byte of its PID in the banner as "Hello from pid8 = <n>"
The main clue we have to solve this challenge is this verification function: (A << 16) ^ (U << 8) ^ (PID & 255)
(which can be interpreted as "token == ((A << 16) ^ (U << 8) ^ pid8)")

To get the flag, we parse the A, U and pid8 values, compute the token from the previos function (if the service does not print A/U, use the observed defaults 'A=0, U=13'), send the token as a newline-terminated integer. The service verifies and prints FLAG on success.

## Flag
Flag: CTF{cbc4e1be639219dad8912bb764b566200023e15152635eef87be047c41bd995a}
