import ascii_art
import time
import game_data
import random
import os
clear = lambda: os.system('cls')

def data_to_str(item : dict) -> str:
    '''Converts item's data to a printable format'''
    return f"{item['name']}, {item['description']}, from {item['country']}"

def followers_to_str(a : dict, b : dict) -> str:
    '''Converts a and b's number of followers to a printable format'''
    return f"{a['name']} has {a['follower_count']} million followers and {b['name']} - {b['follower_count']} million."

def check_answer(a : dict, b : dict, guess : str) -> bool:
    '''Checks if the user's guess as to the number of followers of a and b was correct.'''
    correct = "a" if a['follower_count'] > b['follower_count'] else "b"

    if a['follower_count'] == b['follower_count']:
        print(f"It turns out they both have {a['follower_count']} million followers! Your answer is considered correct.")
        return True
    elif guess == correct:
        print("You're right! " + followers_to_str(a, b))
        return True
    else:
        print(f"Sorry, that's wrong! " + followers_to_str(a, b))
        return False

def game_loop(data : list, compare_a : dict, score = 0) -> int:
    '''Asks the user to compare two people's / objects' number of followers on Instagram
    and continues to do so if their comparison was right. Returns the user's final
    score after their first wrong guess or if there are no more items to compare.'''

    # Check availability of new items
    data.remove(compare_a)
    if len(data) == 0:
        clear()
        print(ascii_art.game_logo)
        print("Congratulations! You won the game! 🎉")
        return score

    # Display current score and a new pair to compare 
    print(f"Your current score is: {score}.")
    print("\nWho has more followers on Instagram?")
    compare_b = random.choice(data)

    print("\nA: " + data_to_str(compare_a))
    print(ascii_art.vs_logo)
    print("\nB: " + data_to_str(compare_b))

    # Ask for user's guess and evaluate it
    while True:
        guess = input("\nType A or B: ").lower()
        if guess == "a" or guess == "b":
            break
        else:
            print("Invalid input. Try again!")

    clear()
    print(ascii_art.game_logo)

    if check_answer(compare_a, compare_b, guess):
        return game_loop(data, compare_b, score + 1)
    else:
        return score

def start_game():
    '''Starts a new game and updates the game's high score, if needed.'''
    global high_score
    clear()
    print(ascii_art.game_logo)

    data = game_data.data.copy()
    final_score = game_loop(data, random.choice(data))
    print(f"Your final score is: {final_score}.")

    time.sleep(2)
    if final_score == high_score:
        print("\nWow! You've reached this game's high score! Congrats! 😮")
    elif final_score > high_score:
        high_score = final_score
        print("\nWow! You've set a new high score for this game! Congrats! 😮")

    print("\nWould you like to play again?")
    if input("Type 'y' for yes or anything else for no: ").lower() == "y":
        start_game()
    else:
        clear()
        print(ascii_art.game_logo)
        print("\nIt was nice having you! Bye!\n")


high_score = game_data.get_high_score()

clear()
print(ascii_art.game_logo)
print("Welcome to the Higher-Lower Game! 😃")
time.sleep(5)

clear()
print(ascii_art.game_logo)
print("Your main goal in this game is to make as many correct guesses as possible about who has more followers on Instagram!")
print(f"Once you make a wrong guess - you lose! The current high score in this game is: {high_score}.")
input("\nReady for a challenge? 😏 ")

start_game()
game_data.update_high_score(high_score)
