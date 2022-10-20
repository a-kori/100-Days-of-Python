import ascii_pictures
import random

print("Welcome to the Rock-Paper-Scissors game!")
rock_paper_scissors = [ascii_pictures.rock, ascii_pictures.paper, ascii_pictures.scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(rock_paper_scissors[player_choice])

computer_choice = random.randint(0, 2)
print("The computer chose:\n" + rock_paper_scissors[computer_choice])

player_won = False
if player_choice == computer_choice : 
    print("It's a draw!")
    exit()
elif player_choice + computer_choice == 4 : 
    player_won = player_choice < computer_choice
else :
    player_won = player_choice > computer_choice

print("You " + ("win" if player_won else "lose") + "!")