# Answers

Juniper Pasternak and Clara Siefke

## Notes

Let =\_ denote modular equivalence (or congruency)

## Part 1: Private Key Cryptography

1. Using 0 for A, 1 for B, and so on, let the numbers 0 to 25 stand for the letters of the alphabet. What is the numerical representation of the word SEA? Write your answer down.

> 18, 4, 0

2. What does the numerical representation of this word become if we shift every letter two places to the right? What does it become if we shift every letter 13 places to the right?

> 2 places: 20, 6, 2  
> 13 places: 5, 17, 13  

3. A Caesar cipher is a shift of the letters. This can be expressed mathematically by using the modulo function. If the shift of letters is 2, then each number _n_ in our message is replaced with _(n + 2) mod 26_. Using a Caesar cipher with a shift of _s_, each number _n_ gets replaced with _(n+s) mod 26_. Using a Caesar cipher corresponding to a shift with size equal to the number of letters in your first name, encrypt your first name. Write down your encrypted name and show the work you did.

```text
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

```text
(n - 12) mod 26
U  Z  H  M  P  Q  M  F  R  U  H  Q
20 25 7  12 15 16 12 5  17 20 7  16
----------------------------------- -12
8  13 21 0  3  4  0  19 5  8  21 4
I  N  V  A  D  E  A  T  F  I  V  E
```

5. See `cipher` directory for TODO.

## Part 2: Public Key Cryptosystem

1. Verify that gcd(13, 42\*58) = 1. Show your work.

> 42 can be factored into 2(3)(7) and 58 can be factored into 2(29). Since 13 is prime and neither 42 nor 58 have 13 as a factor, the greatest common factor is 1. Therefore, gcd(13, 42\*58) = 1.

2. Find an integer d so that 13\*d = 1 (mod 42\*58). Show your work or cite the online source you used to find d.

> Done with significant help from Dr. Pam Cutter, who explained the extended euclidean algorithm to us.  
> 42(58) = 2436  
> 13d =\_ 1 mod 2436  
> 13d =\_ 1 + 2436n mod 2436  
> 1 + 2436 =\_ 0 mod 13  
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
> When d = 937, 13d =\_ 1 mod 2436.  

3. Encipher the message ATTACK using the RSA cipher with public key n = 43*59 and e = 13. Show your work.

> p = 43  
> q = 59  
> e = 13  
> n = pq = 43(59) = 2537  
> gcd(e, (p-1)(q-1)) = gcd(13, (43-1)(59-1)) = gcd(13, 42(58)) = 1  
> d = 937  
> "A" = 0, "B" = 1, "C" = 2... "Z" = 25  
> "ATTACK" = 1, 20, 20, 1, 3, 11  
> c =\_ m^e mod (p-1)(q-1)  
> (p-1)(q-1) = (43 - 1)(59 - 1) = 42(58) = 2436  
> c("A") =\_ 0^13 mod 2537 = 0 mod 2537  
> 19 = 19 mod 2537  
> 19^2 = 361 mod 2537  
> 19^4 = 130321 =\_ 934 mod 2537  
> 19^8 = (19^4)^2 =\_ 934^2 = 872356 =\_ 2165 mod 2537  
> 19^13 = 19^(8+4+1) = 19^8 \* 19^4 \* 19^1 =\_ 2165(934)(19) = 38420090 =\_ 2299 mod 2537  
> c("T") =\_ 19^13 mod 2537 =\_ 2299 mod 2537  
> 2 = 2 mod 2537  
> 2^2 = 4 mod 2537  
> 2^4 = 16 mod 2537  
> 2^8 = 256 mod 2537  
> 2^13 = 2^(8+4+1) = 2^8 \* 2^4 \* 2^1 =\_ 256(16)(2) = 8192 =\_ 581 mod 2537  
> c("C") =\_ 2^13 mod 2537 =\_ 581 mod 2537  
> 10 = 10 mod 2537  
> 10^2 = 100 mod 2537  
> 10^4 = 10000 =\_ 2389 mod 2537  
> 10^8 = (10^4)^2 =\_ 2389^2 = 5707321 =\_ 1608  
> 10^13 = 10^(8+4+1) = 10^8 \* 10^4 \* 10^1 =\_ 1608(2389)(10) = 38415120 =\_ 2403 mod 2537  
> c("K") =\_ 10^13 mod 2537 =\_ 2403 mod 2537  
> The encrypted message is 0, 2299, 2299, 0, 581, 2403.  
