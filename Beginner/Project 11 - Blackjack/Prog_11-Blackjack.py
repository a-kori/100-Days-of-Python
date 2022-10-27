import os
clear = lambda: os.system('cls')
import random
import time
import resources
from resources import card_stack

def dealers_turn():
    '''Determines dealer's cards according to the rules of Blackjack.
    Returns the dealer's final score.'''
    score = resources.update_score(dealer_cards)

    if score >= 17:
        return score
    else:
        dealer_cards.append(random.choice(card_stack))
        return dealers_turn()

def players_turn():
    '''Asks the player if they want to get another card or pass, until their score exceeds 21 or they choose to pass.
    Returns the player's final score.'''
    clear()
    print(resources.blackjack_logo)

    score = resources.update_score(player_cards)
    print("\nYour cards: " + resources.cards_to_str(player_cards))
    print(f"Your score: {score}")
    print(f"Dealer's first card: {resources.card_to_str(dealer_cards[0])}")

    if score > 21:
        return score

    while True:
        choice = input("\nType 'a' to get another card or 'p' to pass: ").lower()

        if choice == "a":
            player_cards.append(random.choice(card_stack))
            return players_turn()
        elif choice == "p":
            return score
        else:
            print("You've entered an invalid input! Try again.")

def find_winner():
    '''Determines the winner according to the rules of Blackjack.
    Has no return value.'''
    clear()
    print(resources.blackjack_logo)
    print(f"\nYour cards: {resources.cards_to_str(player_cards)}")
    print(f"Your score: {player_score}")

    if player_score > 21:
        print("\nIt's a bust! You lose... 🙁")
        print("Better luck next time! 🍀")
    else:
        print(f"\nDealer's cards: {resources.cards_to_str(dealer_cards)}")
        print(f"Dealer's score: {dealer_score}")

        if dealer_score > 21:
            print("\nThe dealer went over! You win! 🎉")
        elif dealer_score > player_score:
            print("\nYou lose... 🙁")
            print("Better luck next time! 🍀")
        elif player_score > dealer_score:
            print("\nCongratulations! You win! 🎉")
        else:
            print("It's a draw! 🤝")

clear()
print(resources.blackjack_logo)
print("Welcome to the game of Blackjack! 😎")
time.sleep(5)

while True:
    dealer_cards = [random.choice(card_stack) for _ in range (2)]
    dealer_score = dealers_turn()

    player_cards = [random.choice(card_stack) for _ in range (2)]
    player_score = players_turn()

    find_winner()

    print("\nWould you like to play again?", end = " ")
    choice = input("Type 'y' for yes or anything else for no: ").lower()
    if choice != "y":
        break

clear()
print(resources.blackjack_logo)
print("GG!\n")