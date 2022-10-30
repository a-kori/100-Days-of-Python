import ascii_art
import data
import time
import os
clear = lambda: os.system('cls')

MENU = "menu"
RESOURCES = "resources"
PROFIT = "profit"

machine = {
    MENU : data.MENU,
    RESOURCES : data.resources.copy(),
    PROFIT : 0
}

def print_error_message(error : str, wait_time = 3):
    '''Informs the user about an invalid input on the console. The message is displayed for 3 seconds.'''

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
    global machine

    clear()
    print(ascii_art.coffee_logo) 

    for ingredient in machine[RESOURCES]:
        print(f"{ingredient.title()}: {machine[RESOURCES][ingredient]}" + ("g" if ingredient == "coffee" else "ml"))
    
    print(f"Profit: ${machine[PROFIT]:.2f}")
    input("\nEnter any key to continue. ")


def refill_machine():
    '''Sets the resources of the machine to their initial values and displays a confirmation message.'''
    global machine
    machine[RESOURCES] =  data.resources.copy()

    clear()
    print(ascii_art.coffee_logo) 
    print("Refill successful!")
    time.sleep(3)


def make_choice() -> dict:
    '''Allows the user to make a choice of a drink and returns the corresponding dict value of the drink.
    Other options include turning the machine off, printing the report on remaining resources or refilling the resources.'''
    global machine

    while True:
        clear()
        print(ascii_art.coffee_logo)

        print("Info: you can turn the machine off by entering 'off', refill its resources by")
        print("entering 'refill' or print the report on remaining resources by entering 'report'.")
        choice = input("\nWhat would you like? (espresso/latte/cappuccino)\n").lower()

        if choice == "off":
            turn_off()
        elif choice == "refill":
            refill_machine()
        elif choice == "report":
            print_report()
        else:
            try:
                return machine[MENU][choice]
            except:
                print_error_message("Invalid input!")


def enough_resources_for(drink : dict) -> bool:
    '''Checks if the machine resources are sufficient for the chosen drink.'''
    global machine

    for this in drink["ingredients"]:
        if machine[RESOURCES][this] < drink["ingredients"][this]:
            print_error_message(f"Sorry, there is not enough {this} to make your coffee.", wait_time = 5)
            return False
    
    return True


def process_coins(drink : dict) -> float:
    '''Asks the user for the number of coins they want to insert and calculates their total value in dollars.'''
    coin_types = {
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickels" : 0.05,
        "pennies" : 0.01
    }
    amount = 0

    while True:
        clear()
        print(ascii_art.coffee_logo)
        cost = drink["cost"]
        print("The price of your " + drink["name"] + f" will be ${cost:.2f}.")
        print("Please, inserts coins here.\n")

        try:
            for type in coin_types:
                coins = int(input(f"Enter the number of {type}: "))
                amount += abs(coin_types[type] * coins)
            return amount
        except:
            print_error_message("Invalid input!")


def enough_money_for(drink : dict, amount : float) -> bool:
    '''Checks if the inserted amount of money is sufficient to buy the selected drink.'''

    if drink["cost"] > amount:
        print_error_message(f"Sorry that's not enough money to make your coffee. ${amount:.2f} refunded.", wait_time = 5)
        return False
    else:
        return True


def update_machine(drink : dict):
    '''Updates the machine's profit and resources after making the selected drink.'''
    global machine

    machine[PROFIT] += drink["cost"]
    for this in drink["ingredients"]:
        machine[RESOURCES][this] -= drink["ingredients"][this]


def buy_drink(drink : dict, amount : float):
    '''Displays the amount of change returned and the purchase confirmation message.'''

    clear()
    print(ascii_art.coffee_logo)
    update_machine(drink)

    change = round(amount - drink["cost"], 2)
    if change > 0.0:
        print(f"Here is your ${change:.2f} change.")
    print("Here is your " + drink["name"] + " ☕. Enjoy!")
    input("\nEnter any key to continue. ")
