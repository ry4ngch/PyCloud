logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

import os
clear = lambda: os.system('clear')
clear()
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = "Y"

# def encrypt(plain_text, shift_amount):
#     full_text = ""
#     try:
#         for t in plain_text:
#             #The letter "z" is at the index 25, there are a total of 26 characters in the alphabet
#             pos = alphabet.index(t)+shift_amount
#
#             #the len() function will return 26 elements in the alphabet array, so match the .index function, we need to minus 1 from len
#             if pos > len(alphabet) - 1:
#                 # pos - len(alphabet) will return 0 when "pos" is calculated as 26
#                 full_text += alphabet[pos - len(alphabet)]
#             else:
#                 full_text += alphabet[pos]
#
#         print(f"The encoded text is {full_text}")
#     except:
#         print("The typed characters are not alphabet")
#
# def decrypt(plain_text, shift_amount):
#     full_text = ""
#     try:
#         for t in plain_text:
#             pos = alphabet.index(t) - shift_amount
#             full_text += alphabet[pos]
#     except:
#         print("The typed characters are not alphabet")
#
#     print(f"The decoded text is {full_text}")
#
# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

def caesar(start_text, shift_amount, cipher_direction):
    full_text = ""
    remove_non_alphabet = ""
    if not start_text.isalpha():
        remove_non_alphabet = input("Do you want to remove those non-alphabet? [Y/N]: \n")
    if shift_amount > len(alphabet) - 1:
        shift_amount = shift_amount%len(alphabet)
    for char in start_text:
        if char in alphabet:
            #The letter "z" is at the index 25, there are a total of 26 characters in the alphabet
            if cipher_direction == "encode":
                pos = alphabet.index(char)+shift_amount
                #the len() function will return 26 elements in the alphabet array, so match the .index function, we need to minus 1 from len
                if pos > len(alphabet) - 1:
                    # pos - len(alphabet) will return 0 when "pos" is calculated as 26
                    full_text += alphabet[pos - len(alphabet)]
                else:
                    full_text += alphabet[pos]
            else:
                pos = alphabet.index(char)-shift_amount
                full_text += alphabet[pos]

        else:
            if not remove_non_alphabet.upper() == "Y":
                full_text += char

    print(f"The {cipher_direction} text is {full_text}")

while restart.upper() == "Y":
    direction = ""
    while not (direction == "decode" or direction == "encode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Do you want to continue decoding and encoding? [Y/N]: \n")
