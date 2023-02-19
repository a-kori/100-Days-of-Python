import os
import colorgram
from turtle import Turtle, Screen

PAINTING_PATH = os.path.dirname(os.path.abspath(__file__)) + "\hirst.jpg"
POS_X = -375
POS_Y = -200

# Extract all existing colors from the Hirst dot painting
colors = [color.rgb for color in colorgram.extract(PAINTING_PATH, 2 ** 32)]

# Delete background colors, which are the first 4
for _ in range(4):
    colors.pop(0)

# 'Recreate' the painting with extracted colors using Turtle Graphics
screen = Screen()
screen.colormode(255)

brush = Turtle()
brush.shape("arrow")
brush.speed("normal")
brush.penup()
brush.setposition(POS_X, POS_Y)

color_index = 0
for offset in range(10):
    brush.setposition(POS_X, POS_Y + offset*50)
    for _ in range(16):
        brush.color(colors[color_index])
        color_index = (color_index + 1) % len(colors)

        brush.pendown()
        brush.dot(20)

        brush.penup()
        brush.forward(50)

screen.exitonclick()