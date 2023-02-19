import time
import random
from turtle import Turtle, Screen

def square_challenge(tim: Turtle):
    '''Draws a square with the edge size of 100.'''
    for _ in range(4):
        tim.right(90)
        tim.forward(100)


def dashed_line_challenge(tim: Turtle):
    '''Draws a dashed line with a dash/gap size of 10.'''
    for _ in range(15):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


def shapes_challenge(tim: Turtle):
    '''Draws an equilateral triangle, a square, an equilateral pentagon, hexagon, heptagon, octagon, nonagon and decagon, changing the color for each shape.'''
    egdes_count = 3
    for _ in range(7):
        tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for _ in range(egdes_count):
            tim.right(360 / egdes_count)
            tim.forward(100)
        egdes_count += 1


def random_walk_challenge(tim: Turtle):
    '''Draws a random walk with a thick brush, changing the color on each step.'''
    tim.speed("normal")
    tim.pensize(15)

    for _ in range(200):
        tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tim.setheading(random.randint(0, 3)*90)
        tim.forward(30)


def spirograph_challenge(tim: Turtle):
    '''Draws a spirograph with a different color for each circle.'''
    tim.speed("fastest")
    degree = 0
    while(degree < 360):
        tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tim.circle(100)
        degree += 6
        tim.setheading(degree)


def perform_challenges():
    '''Performs all the 5 challenges from the lesson with a pause of 1 second between each one.'''
    screen = Screen()
    screen.colormode(255)

    tim = Turtle()
    tim.shape("turtle")

    challenges = [square_challenge, dashed_line_challenge, shapes_challenge, random_walk_challenge, spirograph_challenge]
    for challenge in challenges:
        time.sleep(1)
        screen.reset()
        challenge(tim)

    screen.exitonclick()