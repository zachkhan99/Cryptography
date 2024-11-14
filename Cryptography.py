""" cryptography.py
    Zach Khan
    March 10, 2023
    Implements a simple substitution cypher
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

def main():
    keepGoing = True
    while keepGoing:
        response = menu()
        if response == "1":
            plain = input("text to be encoded: ")
            print(encode(plain))
        elif response == "2":
            coded = input("code to be decyphered: ")
            print (decode(coded))
        elif response == "0":
            print ("Thanks for doing secret spy stuff with me.")
            keepGoing = False
        else:
            print ("I don't know what you want to do...")

def menu():
    print("""\nSECRET DECODER MENU

    0) Quit
    1) Encode
    2) Decode
    """)
    response = input("What is your choice? ")
    return response

def encode(plain):
    encString = ('')
    for x in plain.upper():
        for y in alpha:
            if y == x:
                encString += key[alpha.index(y)]
                break
    return encString


def decode(coded):
    decString = ('')
    for x in coded.upper():
        for y in alpha:
            if y == x:
                decString += alpha[key.index(y)]
                break
    return decString

if __name__ == "__main__":

  main()