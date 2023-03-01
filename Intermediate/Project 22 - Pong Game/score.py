from turtle import Turtle

class Score(Turtle):
    '''A class displaying and keeping track of a player's score in Pong.'''

    def __init__(self, is_left: bool) -> None:
        '''Initializes the score with 0 and displays it on the top of the screen.'''
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        
        x = -1 if is_left else 1
        self.setposition(x*50, 220)

        self.score = -1
        self.increase()

    def increase(self) -> None:
        '''Increments the score and displays the change on the screen.'''
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=('Courier', 50, 'bold'))

    def end_game(self) -> None:
        '''Displays the 'Game over' sign in the center of the screen.'''
        self.setposition(0, 0)
        self.write(f"GAME OVER", align="center", font=('Courier', 50, 'normal'))