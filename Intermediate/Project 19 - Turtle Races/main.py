from turtle import Turtle, Screen
import random
POS_X = -230
POS_Y = -110

# Set up a screen with a width of 500 and a height of 400
screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(1.0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# In a pop-up window, ask the user for a bet on which turtle is going to win
user_bet = None
while(user_bet == "" or user_bet not in colors):
    user_bet = screen.textinput(title="Make your bet!", prompt="Who will win the race? Enter a color:")
    user_bet = user_bet.lower().replace(" ", "")
print(f"Your bet is: the {user_bet} turtle wins.")

# Create turtles with different rainbow colors and move them to starting positons
turtles = []
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setposition(POS_X, POS_Y + i*50)
    turtles.append(new_turtle)

# Start the races and find the winner
winner_color = None
while(winner_color == None):
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if(turtle.xcor() > 230):
            winner_color = turtle.color()[0]
            break

# Compare the winner with the user's bet
if(user_bet == winner_color):
    print(f"Your bet was right! The {winner_color} turtle won the race.")
else:
    print(f"Your bet was wrong. The {winner_color} turtle won the race.")

screen.exitonclick()