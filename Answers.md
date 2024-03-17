Juniper Pasternak and Clara Siefke
## Part 1: Private Key Cryptography
1. Using 0 for A, 1 for B, and so on, let the numbers 0 to 25 stand for the letters of the alphabet. What is the numerical representation of the word SEA? Write your answer down.
> 18, 4, 0

2. What does the numerical representation of this word become if we shift every letter two places to the right? What does it become if we shift every letter 13 places to the right?
> 2 places: 20, 6, 2
> 13 places: 5, 17, 13

3. A Caesar cipher is a shift of the letters. This can be expressed mathematically by using the modulo function. If the shift of letters is 2, then each number _n_ in our message is replaced with _(n + 2) mod 26_. Using a Caesar cipher with a shift of _s_, each number _n_ gets replaced with _(n+s) mod 26_. Using a Caesar cipher corresponding to a shift with size equal to the number of letters in your first name, encrypt your first name. Write down your encrypted name and show the work you did.
```
(n + 5) mod 26
C  L  A  R  A
2  11 0  17 0
------------- +5
7  16 5  22 5
H  Q  F  W  F

(n + 7) mod 26
J  U  N  I  P  E  R
9  20 13 8  15 4  17
-------------------- +7
16 1  20 15 22 11 24
Q  B  U  P  W  L  Y
```

4. Decrypt the text UZHMPQMFRUHQ that was encrypted with a shift of 12. Write down the plaintext.
```
(n - 12) mod 26
U  Z  H  M  P  Q  M  F  R  U  H  Q
20 25 7  12 15 16 12 5  17 20 7  16
----------------------------------- -12
8  13 21 0  3  4  0  19 5  8  21 4
I  N  V  A  D  E  A  T  F  I  V  E
```

5. See `cipher` directory for TODO.

# Part 2: Public Key Cryptosystem

1. Verify that gcd(13, 42\*58) = 1. Show your work.

> 42 can be factored into 2(3)(7) and 58 can be factored into 2(29). Since 13 is prime and neither 42 nor 58 have 13 as a factor, the greatest common factor is 1. Therefore, gcd(13, 42\*58) = 1.

2. Find an integer d so that 13\*d = 1 (mod 42\*58). Show your work or cite the online source you used to find d.

> Done with significant help from Dr. Pam Cutter, who explained the extended euclidean algorithm to us.

> 42(58) = 2436

> 13d =_ 1 mod 2436

> 13d =_ 1 + 2436n mod 2436

> 1 + 2436 =_ 0 mod 13

> 2436 = 13(187) + 5

> 13 = 5(2) + 3

> 5 = 3(1) + 2

> 3 = 2(1) + 1

> 2 = 1(2) + 0

> 1 = 3 - 2(1)

> 1 = 3 - (5 - (3(1)))

> 1 = (13 - (5(2))) - (5 - (13 - 5(2)))

> 1 = 2(13 - 5(2)) + 5

> 1 = 2(13) - 5(5)

> 1 = 2(13) - 5(2436 - 13(187))

> 1 = (5(187) + 2)(13) - 5(2436)

> 1 = 937(13) - 5(2436)

> 1 + 5(2436) = 937(13)

> n = 5, d = 937

> When d = 937, 13d =_ 1 mod 2436.
