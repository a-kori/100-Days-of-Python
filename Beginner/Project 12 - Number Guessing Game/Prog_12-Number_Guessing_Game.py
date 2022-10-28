from resources import game_logo
import random
import os
clear = lambda: os.system('cls')

EASY_LEVEL = 10
HARD_LEVEL = 5

def get_number_of_attempts():
    '''Asks the player for their difficulty level of choice.
    Return value: the number of attempts corresponding to the chosen level - 5 attempts for hard and 10 attempts for easy.'''
    difficulty = input("\nChoose a difficulty level. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL
    else:
        print("Invalid input! Try again.")
        return get_number_of_attempts()

def player_guessed(attempts_left : int):
    '''Asks the player to guess the number until they run out of attempts or the number is guessed.
    Return value: a boolean value, which indicates if the player has guessed the number.'''
    if attempts_left == 0:
        return False

    print(f"\nYou have {attempts_left} attempt" + ("s" if attempts_left > 1 else "") + " remaining to guess the number.")
    while True:
        try: 
            guess = int(input("Make a guess: "))
            break
        except:
            print("Apparently, you've entered a non-integer value for your guess. Try again.\n")

    if guess > number:
        print("Too high!" + (" Try again." if attempts_left > 1 else ""))
        return player_guessed(attempts_left - 1)
    elif guess < number:
        print("Too low!" + (" Try again." if attempts_left > 1 else ""))
        return player_guessed(attempts_left - 1)
    else:
        return True

clear()
print(game_logo)
print("Welcome to the Number Guessing Game! ✨\n")

while True:
    print("I'm thinking of a number between 1 and 100... 🤔")
    number = random.randint(1, 100)

    attempts = get_number_of_attempts()
    if(player_guessed(attempts)):
        print(f"\nCongratulations! You've guessed the number {number}! 🎉")
    else:
        print(f"\nUnfortunately, you've run out of attempts! The hidden number was {number}. 🙁")

    print("\nWould you like to play again?", end = " ")
    if input("Type 'y' for yes or anything else for no: ").lower() == "y":
        clear()
        print(game_logo)
    else:
        break

clear()
print(game_logo)
print("\nAlright! Goodbye! 🙂\n")