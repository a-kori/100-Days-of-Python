from turtle import Turtle

class LevelTracker(Turtle):
    '''A class displaying the player's level in Turtle Crossing.'''

    def __init__(self, screen_width: int, screen_length: int) -> None:
        '''Initializes the level with 1 and displays it on the top left of the screen.'''
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

        x = (screen_width / 2) - 20
        y = (screen_length / 2) - 30
        self.setposition(-x, y)

        self.level = 0
        self.increase_level()


    def increase_level(self) -> None:
        '''Increments the level and displays the change on the screen.'''
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 15, "normal"))


    def end_game(self) -> None:
        '''Displays the 'Game over' sign in the center of the screen.'''
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
