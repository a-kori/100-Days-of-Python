import characters
import random

print("Welcome to the Password Generator!")
while(True) :
    letters_count = int(input("How many letters would you like in your password?\n"))
    numbers_count = int(input("How many numbers would you like?\n"))
    symbols_count = int(input("How many special characters would you like?\n"))

    if letters_count >= 0 and numbers_count >= 0 and symbols_count >= 0 : break
    else : print("Apparently, you chose an inapplicable number of characters at some point. Please, try again.")

password = []
for i in range(0, letters_count) :
    password += random.choice(characters.letters)
for i in range(0, numbers_count) :
    password += random.choice(characters.numbers)
for i in range(0, symbols_count) :
    password += random.choice(characters.symbols)

random.shuffle(password)
print("Your password is: " + "".join(password))