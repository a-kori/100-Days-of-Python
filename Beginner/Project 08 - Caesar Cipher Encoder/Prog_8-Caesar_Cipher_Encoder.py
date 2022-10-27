import resources
import string
import time

alphabet = list(string.ascii_lowercase)

def transform(encode, text, shift) :
    if not encode :
        shift = -shift
    result = ""
    
    for char in text :
        try :
            index = alphabet.index(char) + shift
            if index >= len(alphabet) :
                index -= len(alphabet)
            result += alphabet[index]
        except :
            result += char

    return result

resources.clear()
print(resources.encoder_logo)
print("Welcome to the Caesar Cipher Encoder!")
time.sleep(5)

while True:
    resources.clear()
    print(resources.encoder_logo)

    encode = False
    if resources.get_value_from_user("Type 'encode' to encrypt or 'decode' to decrypt a message:", ["encode", "decode"]) == "encode" :
        encode = True
    text = resources.get_value_from_user("Type your message:").lower()
    shift = int(resources.get_value_from_user("Type the shift number between 0 and 25:", [str(x) for x in range (len(alphabet))]))

    print("\nThe " + ("en" if encode else "de") + f"coded message is: {transform(encode, text, shift)}")

    exit_choice = input("\nWould you like to exit the program? Type 'y' for yes or anything else for no: ")
    if exit_choice.lower() == "y" : 
        print()
        exit()
