from turtle import Turtle
import random

class Food(Turtle):
    '''A class describing food pieces and their behavior in the Snake Game.'''

    def __init__(self) -> None:
        '''Creates a food piece in a shape of 10x10 blue circle.'''
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.locate_randomly()
    
    def locate_randomly(self) -> None:
        '''Places the food piece at a random location.'''
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.setposition(rand_x, rand_y)
