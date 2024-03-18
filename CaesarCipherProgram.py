"""Caesar Cipher Program
This program takes a message and a shift value and either encrypts or decrypts the
message using the Caesar cipher. The user is prompted to enter a message, choose
whether to encrypt or decrypt the message, and then enter a shift value.
The program then outputs the encrypted or decrypted message.

Authors: Clara Siefke and Juniper Pasternak
Date: 03/16/24 to 3/17/2024
"""

import sys

def alphaToNum(alphaStr: str) -> list[int]:
    """Converts a string of capital letters to a list of numbers representing their
       position in the alphabet from 0 to 25.

    Args:
        alphaStr (str): a capital letter string to be converted

    Returns:
        list[int]: a list of integers representing each letter in the alphabet
    """

    # We can take the Unicode value of each letter and subtract the Unicode value
    # of 'A' to get the numerical value of the letter.
    return [ord(char) - ord('A') for char in alphaStr]

def numToAlpha(numList: list[str]):
    """Converts a list of numbers to a string of capital letters.

    Args:
        numList (list[str]): a list of integers in range [0, 25] to be converted

    Returns:
        _type_: a string of capital letters representing each number in the list
    """

    # We can take the numerical value of each letter and add the Unicode value
    # of 'A' to get the Unicode value of the letter.
    return "".join([chr(num + ord('A')) for num in numList])

def shiftMsg(msg: str, shift: int) -> str:
    """Shifts each letter in the message by the shift value and returns the new message.
       For example, if the message is "ABC" and the shift value is 3, the new message
       will be "DEF".

    Args:
        msg (str): _description_
        shift (int): _description_

    Returns:
        str: _description_
    """

    return "".join(numToAlpha(
        [(num + shift) % 26 for num in alphaToNum(msg)])
    )

def main() -> int:
    """Runs the main program.

    Returns:
        int: The exit code. 0 for success, 1 for failure.
    """

    # Get the message and make sure it only contains letters
    message: str = input(
        "Enter a message with (alphabetical) to encrypt/decrypt:\n"
    ).strip().replace(" ", "").upper()
    if not message.isalpha():
        print("Invalid message. Please enter only letters.")
        return 1

    # Get the option and make sure it is valid
    option: str = input("[E] to encrypt | [D] to decrypt:\n").strip().upper()
    if option not in ["E", "D"]:
        print("Invalid option. Please enter 'E' or 'D'.")
        return 1

    # Make sure the shift value is an integer
    try:
        shift = int(input("Enter your secret key (shift value):\n").strip())
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return 1

    # If the user wants to decrypt the message, negate the shift value
    if option == "D":
        shift *= -1

    print("\nYour decrypted message is " + shiftMsg(message, shift))

    return 0

if __name__ == "__main__":
    sys.exit(main())
