# Cipher Project

## About

This project answers a series of Discrete Math questions related to cryptography.
It also features two python programs to run cryptographic functions.

This project was completed for educational purposes for MATH250 at Kalamazoo College.  
Its answers and programs aim to follow the
[Cipher Project specifications](https://www.cs.kzoo.edu/math250/CipherProj.html).

### Structure

Relevant files can be found in the root directory of this repository:

- [`Answers.md`](Answers.md)
- [`CaesarCipherProgram.py`](CaesarCipherProgram.py)
- [`RSA.py`](RSA.py)
- [`requirements.txt`](requirements.txt)

### Authors

This project was completed collaboratively by Clara Siefke and Juniper Pasternak.
Credit to the professor, Pam Cutter, for her help in [part 2](Answers.md#part-2-public-key-cryptosystem).

### History

This project was last updated on 2024-03-18.
To view a full history, run git log inside the source repository.

## User Instructions

### Prerequisites

- Latest [Python](https://www.python.org/downloads/)

### Setup

Windows:

```bash
python -m pip install -r requirements.txt
```

UNIX-like:

```shell
python3 -m pip install -r requirements.txt
```

### How to Run

Windows:

```bash
python CaesarCipherProgram.py
python RSA.py
```

UNIX-like:

```shell
python3 CaesarCipherProgram.py
python3 RSA.py
```

### Examples

#### Caesar Cipher

```text
>python CaesarCipherProgram.py
[E] to encrypt | [D] to decrypt:
E
Enter your secret key (shift value):
20
Enter a message (alphabetical) to encrypt/decrypt:
HelloWorld

Your encrypted message is: BYFFIQILFX
```

```text
>python CaesarCipherProgram.py
[E] to encrypt | [D] to decrypt:
D
Enter your secret key (shift value):
20
Enter a message (alphabetical) to encrypt/decrypt:
BYFFIQILFX

Your decrypted message is: HELLOWORLD
```

#### RSA

```text
>python RSA.py
[E] to encrypt | [D] to decrypt:
E
Please enter the public key for encryption (if empty, .env will be used):

Please enter the modulus (if empty, .env will be used):

Please enter the message to be encrypted:
HelloWorld

The encrypted message is: 156 205 2497 2497 2116 2475 2116 2222 2497 140
```

```text
>python RSA.py
[E] to encrypt | [D] to decrypt:
D
Please enter the private key for encryption (if empty, .env will be used):

Please enter the modulus (if empty, .env will be used):

Please enter the message as numbers separated by spaces:
156 205 2497 2497 2116 2475 2116 2222 2497 140

The decrypted message is: HELLOWORLD
```
