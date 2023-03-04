from turtle import Turtle
import os
HIGH_SCORE_PATH = os.path.dirname(os.path.abspath(__file__)) + "\high_score.txt"

class Scoreboard(Turtle):
    '''A class displaying and keeping track of the player's (high) score in the Snake Game.'''

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
        self.write(f"Score: {self.score}, High Score: {self.get_high_score()}", 
                   align="center", font=('Consolas', 12, 'normal'))

    def end_game(self) -> None:
        '''Displays the 'Game over' sign in the center of the screen and updates the high score.'''
        if self.score > self.get_high_score():
            self.update_high_score(self.score)
        
        self.setposition(0, 0)
        self.write(f"GAME OVER", align="center", font=('Consolas', 12, 'normal'))

    def get_high_score(self) -> int:
        '''Returns the current high score of the game.'''
        with open(HIGH_SCORE_PATH, 'r') as file:
            return int(file.readline())

    def update_high_score(self, new_high_score : int) -> None:
        '''Overwrites the current high score of the game.'''
        with open(HIGH_SCORE_PATH, 'w') as file:
            file.write(str(new_high_score))
