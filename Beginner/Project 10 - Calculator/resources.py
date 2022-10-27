import os
clear = lambda: os.system('cls')

def collectFirstNumber():
    """Asks the user for the first number used in the calculation."""
    while(True):
        try: 
            return float(input("\nWhat's the first number? "))
        except:
            print("Apparently, you've enterd a non-numeric value. Try again!")

def collectNext(operations):
    """Asks the user for an operation and the next number used in the calculation."""
    
    print()
    for operation in operations:
        print(operation)

    while(True):
        operation = input("\nPick an operation: ")
        if operation not in operations:
            print("You should enter one of the operations listed above. Try again!")
        else : break

    while(True):
        try: 
            next_num = float(input("\nWhat's the next number? "))
            break
        except:
            print("Apparently, you've enterd a non-numeric value. Try again!")

    return operation, next_num

def shouldStartNewCalc(result):
    """Asks the user if they want to continue with the current result, start a new calculation or exit the program."""
    while(True):
        choice = input(f"\nType 'c' to continue calculating with {result}, 'n' to start a new calculation, or 'e' to exit the calculator: ").lower()
        if choice == "c":
            return False
        elif choice == "n":
            return True
        elif choice == "e":
            return
        else:
            print("Invalid option. Try again!")

calculator_logo = '''
_____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------.  .--------------.  .--------------.  .--------------. |
|  ___ ___ ___   ___  | | |     ______   |  |            | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   ._____.'  | || ||____|  |____|| || |  |________|  | || |   ._____.'  | |
| |___|___|___| |___| | | |              |  |              |  |              |  |              | |
| | . | 0 | = | | / | | | '--------------'  '--------------'  '--------------'  '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

'''