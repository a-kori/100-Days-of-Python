'''Another challenge from Day 19: to make an Etch-A-Sketch app using Turtle Graphics.'''
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
tim.shape("turtle")

screen.listen()
# W = Move forwards
screen.onkey(key="w", fun=lambda: tim.forward(10))
# S = Move backwards
screen.onkey(key="s", fun=lambda: tim.backward(10))
# D = Tilt clockwise
screen.onkey(key="d", fun=lambda: tim.setheading(tim.heading() - 10))
# A = Tilt counter-clockwise
screen.onkey(key="a", fun=lambda: tim.setheading(tim.heading() + 10))
# C = Clear drawing
screen.onkey(key="c", fun=lambda: screen.reset())

screen.exitonclick()