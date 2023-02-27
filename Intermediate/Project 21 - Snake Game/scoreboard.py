from turtle import Turtle

class Scoreboard(Turtle):
    '''A class displaying and keeping track of the players's score in the Snake Game.'''

    def __init__(self) -> None:
        '''Initializes the score with 0 and displays it on the top of the screen.'''
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0, 275)
        self.color("white")
        self.score = -1
        self.increase()

    def increase(self) -> None:
        '''Increments the score and displays the change on the screen.'''
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Consolas', 12, 'normal'))

    def end_game(self) -> None:
        '''Displays the 'Game over' sign in the center of the screen.'''
        self.setposition(0, 0)
        self.write(f"GAME OVER", align="center", font=('Consolas', 12, 'normal'))