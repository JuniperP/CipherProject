
#Clara Siefke and Juniper Pasternak | 03/16/24 | Caesar Cipher Program

# alphToNum
# This function takes a string as its parameter and returns an array of the numerical values (still as strings) corresponding to each to each letter.
def alphToNum(a):
    a = a.upper()

    array = []

    for i in range(len(a)):
        array.append(a[i])

    for i in range(len(array)):
        if(array[i] == "A"):
            array[i] = "0"
        elif(array[i] == "B"):
            array[i] = "1"
        elif(array[i] == "C"):
            array[i] = "2"
        elif(array[i] == "D"):
            array[i] = "3"
        elif(array[i] == "E"):
            array[i] = "4"
        elif(array[i] == "F"):
            array[i] = "5"
        elif(array[i] == "G"):
            array[i] = "6"
        elif(array[i] == "H"):
            array[i] = "7"
        elif(array[i] == "I"):
            array[i] = "8"
        elif(array[i] == "J"):
            array[i] = "9"
        elif(array[i] == "K"):
            array[i] = "10"
        elif(array[i] == "L"):
            array[i] = "11"
        elif(array[i] == "M"):
            array[i] = "12"
        elif(array[i] == "N"):
            array[i] = "13"
        elif(array[i] == "O"):
            array[i] = "14"
        elif(array[i] == "P"):
            array[i] = "15"
        elif(array[i] == "Q"):
            array[i] = "16"
        elif(array[i] == "R"):
            array[i] = "17"
        elif(array[i] == "S"):
            array[i] = "18"
        elif(array[i] == "T"):
            array[i] = "19"
        elif(array[i] == "U"):
            array[i] = "20"
        elif(array[i] == "V"):
            array[i] = "21"
        elif(array[i] == "W"):
            array[i] = "22"
        elif(array[i] == "X"):
            array[i] = "23"
        elif(array[i] == "Y"):
            array[i] = "24"
        elif(array[i] == "Z"):
            array[i] = "25"

    for i in range(len(array)):
        array[i] = int(array[i])
    
    return array

# numToAlph
# This functions takes an array of numbers (as integers) and returns a string of letters with each letter corresponding to a number in the array.
def numToAlph(n):
    for i in range(len(n)):
        if(n[i] == 0):
            n[i] = "A"
        elif(n[i] == 1):
            n[i] = "B"
        elif(n[i] == 2):
            n[i] = "C"
        elif(n[i] == 3):
            n[i] = "D"
        elif(n[i] == 4):
            n[i] = "E"
        elif(n[i] == 5):
            n[i] = "F"
        elif(n[i] == 6):
            n[i] = "G"
        elif(n[i] == 7):
            n[i] = "H"
        elif(n[i] == 8):
            n[i] = "I"
        elif(n[i] == 9):
            n[i] = "J"
        elif(n[i] == 10):
            n[i] = "K"
        elif(n[i] == 11):
            n[i] = "L"
        elif(n[i] == 12):
            n[i] = "M"
        elif(n[i] == 13):
            n[i] = "N"
        elif(n[i] == 14):
            n[i] = "O"
        elif(n[i] == 15):
            n[i] = "P"
        elif(n[i] == 16):
            n[i] = "Q"
        elif(n[i] == 17):
            n[i] = "R"
        elif(n[i] == 18):
            n[i] = "S"
        elif(n[i] == 19):
            n[i] = "T"
        elif(n[i] == 20):
            n[i] = "U"
        elif(n[i] == 21):
            n[i] = "V"
        elif(n[i] == 22):
            n[i] = "W"
        elif(n[i] == 23):
            n[i] = "X"
        elif(n[i] == 24):
            n[i] = "Y"
        elif(n[i] == 25):
            n[i] = "Z"

    txt = ""

    for i in range(len(n)):
        txt = txt + n[i]
    
    return txt

# encrypt
# This function takes a string, calls the alphToNum function to convert it into an array of numbers (as integers), adds the length of the array to each value in the array and makes them mod 26, and then calls the numToAlph function to covert the array into a string of letters. It returns this string of letters.
def encrypt(m):

    array = alphToNum(m)

    for i in range(len(array)):
        array[i] = (array[i] + len(array)) % 26

    return numToAlph(array)

# decrypt
# This function takes a string, calls the alphToNum function to convert it into an array of numbers (as integers), subtracts the length of the array from each value in the array and makes them mod 26, and then calls the numToAlph function to covert the array into a string of letters. It returns this string of letters.
def decrypt(m):

    array = alphToNum(m)

    for i in range(len(array)):
        array[i] = (array[i] - len(array)) % 26

    return numToAlph(array)

# main
def main():
    message = input("Enter a message that is fully capitalized and contains no spaces:\n")

    option = input("Enter \"E\" if you wish to encrypt the message. Enter \"D\" if you wish to decrypt the message:\n")

    if(option == "E"):
        print("\nYour encrypted message is " + encrypt(message))
    elif(option == "D"):
        print("\nYour decrypted message is " + decrypt(message))

main()