import os
import pandas
import turtle
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = PROJECT_PATH + "/blank_states_img.gif"


def display_text(text: str, x_cor: int, y_cor: int) -> None:
    '''Displays the passed text on the screen at the passed coordinates.'''
    display = turtle.Turtle()
    display.hideturtle()
    display.penup()
    display.setposition(x_cor, y_cor)
    display.write(text, align="center", font=("Arial", 8, "bold"))


def should_quit_game() -> bool:
    '''Ask the user if they want to quit the game.'''
    answer_quit = None
    while not answer_quit:
        answer_quit = screen.textinput(title="Game Paused", prompt="Would you like to quit the game? (yes/no)")
    return answer_quit.strip().lower() == "yes"


# Setting up the screen and blank_states_img.gif as background image
screen = turtle.Screen()
screen.setup(width=730, height=495)
screen.title("Name the States")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Saving data from 50_states.csv into a pandas dataframe
us_states = pandas.read_csv(PROJECT_PATH + "/50_states.csv")

# Asking the user to name a state and displaying
# it on the map until all 50 states are named.
states_left = list(us_states.state)
while len(states_left) > 0:
    answer_state = screen.textinput(title=f"{50 - len(states_left)}/50 States Correct", prompt="What's another US state name?")

    if not answer_state:
        if should_quit_game(): 
            break
    else:
        answer_state = answer_state.strip().title()
        search_result = us_states[us_states.state == answer_state]

        if len(search_result) > 0 and answer_state in states_left:
            states_left.remove(answer_state)
            display_text(search_result.state.item(), int(search_result.x), int(search_result.y))

# Saving unnamed states to a csv file and finishing the program
pandas.DataFrame(states_left).to_csv(PROJECT_PATH + "/unnamed_states.csv")
screen.exitonclick()
