import ascii_art
import time
import os
from functions import *

os.system('cls')
print(ascii_art.coffee_logo)
print("Welcome to the Coffee Machine!")
time.sleep(5)

while True:
    selected_drink = make_choice()
    if not enough_resources_for(selected_drink) : continue

    inserted_amount = process_coins(selected_drink)
    if not enough_money_for(selected_drink, inserted_amount) : continue

    buy_drink(selected_drink, inserted_amount)
