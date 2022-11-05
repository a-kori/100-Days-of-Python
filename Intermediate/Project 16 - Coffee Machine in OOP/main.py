from functions import *
import ascii_art
import time
import os

os.system('cls')
print(ascii_art.coffee_logo)
print("Welcome to the Coffee Machine!")
time.sleep(5)

while True:
    selected_drink = make_choice()
    if not enough_resources_for(selected_drink) : continue

    process_coins(selected_drink)
    buy_drink(selected_drink)