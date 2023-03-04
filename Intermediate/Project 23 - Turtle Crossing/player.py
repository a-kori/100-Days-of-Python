from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270

class Player(Turtle):
    '''A class describing the player's turtle apperance and control in the Turtle Crossing game.'''

    def __init__(self, screen_width: int, screen_length: int) -> None:
        '''Creates the player's turtle of white color and places it at the bottom of the screen.'''
        super().__init__()
        self.screen_width = screen_width
        self.screen_length = screen_length

        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.set_starting_position()


    def set_starting_position(self) -> None:
        self.setposition(0, -self.screen_length/2 + 25)


    def crossed_finish_line(self) -> bool:
        '''Checks if the turtle has crossed the finish line.'''
        return self.ycor() > self.screen_length/2 - 25


    def move_up(self) -> None: 
        '''Moves the turtle upwards by 10 paces.'''
        if self.ycor() + MOVE_DISTANCE <= self.screen_length/2 - 10:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)
            
    
    def move_down(self) -> None: 
        '''Moves the turtle downwards by 10 paces.'''
        if self.ycor() - MOVE_DISTANCE >= -self.screen_length/2 + 10:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)


    def move_right(self) -> None: 
        '''Moves the turtle to the right by 10 paces.'''
        if self.xcor() + MOVE_DISTANCE <= self.screen_width/2 - 10:
            self.setposition(self.xcor() + MOVE_DISTANCE, self.ycor())


    def move_left(self) -> None: 
        '''Moves the turtle to the left by 10 paces.'''
        if self.xcor() - MOVE_DISTANCE >= -self.screen_width/2 + 10:
            self.setposition(self.xcor() - MOVE_DISTANCE, self.ycor())
