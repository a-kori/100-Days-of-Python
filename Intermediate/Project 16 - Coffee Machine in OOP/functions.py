from menu import *
from coffee_maker import *
from money_machine import *
import ascii_art
import time
import os
clear = lambda: os.system('cls')

coffee_m = CoffeeMaker()
money_m = MoneyMachine()
menu = Menu()

def print_error_message(error : str, wait_time = 3):
    '''Informs the user about an error. The message is displayed for wait_time seconds (or 3 by default).'''

    clear()
    print(ascii_art.coffee_logo)
    print(f"{error}\nTry again in {wait_time} seconds.")
    time.sleep(wait_time)


def turn_off():
    '''Turns the coffee machine off by printing a goodbye message and exiting the programm.'''
    clear()
    print(ascii_art.coffee_logo)
    print("It was nice having you! Bye! 👋\n")
    exit()


def print_report():
    '''Prints a report of how much water, milk and coffee is left in the machine, as well as on how much profit the machine has made so far.'''
    global coffee_m, money_m
    
    clear()
    print(ascii_art.coffee_logo) 

    coffee_m.report()
    money_m.report()
    
    input("\nEnter any key to continue. ")


def refill_machine():
    '''Sets the resources of the machine to their initial values and displays a confirmation message.'''
    global coffee_m
    coffee_m = CoffeeMaker()

    clear()
    print(ascii_art.coffee_logo) 
    print("Refill successful!")
    time.sleep(3)


def make_choice() -> MenuItem:
    '''Allows the user to make a choice of a drink and returns the corresponding dict value of the drink.
    Other options include turning the machine off, printing the report on remaining resources or refilling the resources.'''
    global menu

    while True:
        clear()
        print(ascii_art.coffee_logo)

        print("Info: you can turn the machine off by entering 'off', refill its resources by")
        print("entering 'refill' or print the report on remaining resources by entering 'report'.")
        choice = input(f"\nWhat would you like? ({menu.get_items()})\n").lower()

        if choice == "off":
            turn_off()
        elif choice == "refill":
            refill_machine()
        elif choice == "report":
            print_report()
        elif choice == "":
            continue
        else:
            result = menu.find_drink(choice)
            if result != None:
                return result
            else:
                print_error_message("Invalid input! No such item found!")


def enough_resources_for(drink : MenuItem) -> bool:
    '''Checks if the machine resources are sufficient for the chosen drink.'''
    global coffee_m

    if not coffee_m.is_resource_sufficient(drink):
        input("\nEnter any key to continue. ")
        return False
    return True


def process_coins(drink : MenuItem):
    '''Asks the user for the number of coins they want to insert and calculates their total value in dollars.'''
    global money_m

    while True:
        clear()
        print(ascii_art.coffee_logo)
        print(f"The price of your {drink.name} will be ${drink.cost:.2f}.")

        try:
            money_m.process_coins()
            break
        except:
            print_error_message("Invalid input!")
            money_m.money_received = 0


def buy_drink(drink : MenuItem):
    '''Displays the amount of change returned and the purchase confirmation message.'''
    global money_m, coffee_m

    clear()
    print(ascii_art.coffee_logo)
    
    if money_m.make_payment(drink.cost):
        print()
        coffee_m.make_coffee(drink)

    input("\nEnter any key to continue. ")
