"""RSA Encryption and Decryption
This program either takes a message and a public key and encrypts the message
using the a simplified RSA encryption algorithm, or takes an encrypted message
and a private key and decrypts the message using the RSA decryption algorithm.
The user is prompted to enter a message, choose whether to encrypt or decrypt
the message, and then enter a public or private key. The program then outputs
the encrypted or decrypted message. Additionally, the public modulus is needed
for both encryption and decryption. For the key and modulus, the user can either
enter the values when prompted, or leave them empty to use the values from the
.env file.

Authors: Juniper Pasternak and Clara Siefke
Date: 03/18/2024
"""

import os
import sys
from dotenv import load_dotenv
from CaesarCipherProgram import alpha_to_num, num_to_alpha

def rep_square(base: int, exp: int, mod: int) -> int:
    """Performs repeated squaring to calculate the result of base^exp % mod.

    Args:
        base (int): the base value
        exp (int): the exponent value
        mod (int): the modulus value

    Returns:
        int: the result of base^exp % mod
    """

    result = 1
    square = base
    mask = 1

    # Keep squaring while there are still bits in the exponent
    while mask <= exp:
        if exp & mask:                         # If the current bit is 1
            result = (result * square) % mod   # Multiply the result and the mod it
        square = (square * square) % mod       # Square the square and mod it
        mask <<= 1                             # Move to the next bit (to the left)

    return result

def encrypt(msg: str, pub: int, mod: int) -> list[int]:
    """Encrypts a message using the RSA encryption algorithm.
       The message must be alphabetical and in uppercase.
       Letters are encoded as numbers from 1 to 26.

    Args:
        msg (str): the message to be encrypted
        pub (int): the public key value
        mod (int): the modulus value

    Returns:
        list[int[]: the encrypted message
    """

    # Convert the message to a list of integers in range [1, 26]
    msgInts = [num + 1 for num in alpha_to_num(msg)]
    return [rep_square(num, pub, mod) for num in msgInts]

def decrypt(cipher: list[int], priv: int, mod: int) -> str:
    """Decrypts a message using the RSA decryption algorithm.
       The message will be returned as an alphabetical string in uppercase.

    Args:
        cipher (list[int]): the encrypted message to be decrypted
        priv (int): the private key value
        mod (int): the modulus value

    Returns:
        str: the decrypted message
    """

    # Decrypt the message to a list of integers in range [1, 26]
    msgInts = [rep_square(num, priv, mod) for num in cipher]
    # Convert the message to a string
    decrypted = num_to_alpha([num - 1 for num in msgInts])
    if not decrypted.isalpha():
        raise ValueError("invalid message value (not alphabetical)")

    return decrypted

def main() -> int:
    """Runs the main program.

    Returns:
        int: 0 if the program runs successfully, 1 if there is an error
    """

    # Load the environment variables from the .env file
    load_dotenv()

    # Get the option and make sure it is valid
    option = input("[E] to encrypt | [D] to decrypt:\n").strip().upper()
    if option not in ["E", "D"]:
        print("Invalid option. Please enter 'E' or 'D'.")
        return 1

    # Get the public or private key
    key_type = "public" if option == "E" else "private"
    key = input(f"Please enter the {key_type} key for encryption (if empty, .env will be used):\n")
    if not key:
        key = os.getenv(f"{key_type.upper()}_KEY")
    try:
        key = int(key)
    except ValueError:
        print("Invalid key. Please enter an integer value.")
        return 1

    # Get the modulus
    mod = input("Please enter the modulus (if empty, .env will be used):\n")
    if not mod:
        mod = os.getenv("MODULUS")
    try:
        mod = int(mod)
    except ValueError:
        print("Invalid modulus. Please enter an integer value.")
        return 1

    # Handle encryption
    if option == "E":
        msg = input("Please enter the message to be encrypted:\n")
        msg = msg.strip().replace(" ", "").upper()
        if not msg.isalpha():
            print("Invalid message. Please enter only letters.")
            return 1
        encrypted = " ".join(str(num) for num in encrypt(msg, key, mod))
        print(f"\nThe encrypted message is: {encrypted}")
    # Handle decryption
    else:
        cipher = input("Please enter the message as numbers separated by spaces:\n")
        try:
            cipher = [int(num) for num in cipher.split()]
        except ValueError:
            print("Invalid message. Please enter integer values.")
            return 1
        decrypted = decrypt(cipher, key, mod)
        print(f"\nThe decrypted message is: {decrypted}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
