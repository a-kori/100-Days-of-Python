import resources
import random
import time

while True :

    resources.clear()
    print(resources.hangman_logo)
    print("Welcome to the game!")

    chosen_word = random.choice(resources.word_list)
    hidden_word = []
    for i in range(len(chosen_word)) :
        hidden_word += "_"

    current_stage = len(resources.stages) - 1
    used_letters = []
    status_string = ""

    time.sleep(5)
    while True :
        resources.clear()

        print(resources.stages[current_stage])
        print("\nYou word is:")
        print(" ".join(hidden_word))
        print("\n" + status_string)

        guess = input("\nGuess a letter: ").lower()
        if len(guess) > 1 :
            status_string = "You entered more than one letter! Try again."
            continue
        elif guess in used_letters :
            status_string = f"Seems like you've already used the letter '{guess}'! Try again."
            continue
        elif guess == "" :
            status_string = ""
            continue
        else : 
            used_letters += guess

        in_chosen_word = False
        for i in range(len(chosen_word)) :
            if chosen_word[i] == guess :
                in_chosen_word = True
                hidden_word[i] = guess
        
        if in_chosen_word :
            status_string = "Your guess was right!"
            if "_" not in hidden_word : 
                status_string = resources.hangman_logo + f"\nYou guessed the word '{chosen_word}'! Congratulations!\n"
                break
        else :
            current_stage -= 1
            status_string = f"The letter '{guess}' is not in the word. You lose a life."
            if current_stage == 0 :
                status_string = resources.stages[0] + f"\nUnfortunately, you lost all your lives. The hidden word was '{chosen_word}'. Better luck next time!\n"
                break

    resources.clear()
    print(status_string)

    choice = input("\nWould you like to play again? Type 'y' for yes or anything else for no: ")
    if choice.lower() != "y" : 
        print()
        exit()