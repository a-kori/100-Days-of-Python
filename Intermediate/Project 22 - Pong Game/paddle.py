from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    '''A class describing a paddle's appearance and control functions in Pong.'''

    def __init__(self, screen_width: int, screen_height: int, is_left: bool) -> None:
        '''Creates a paddle of length 100 and width 20 and places 
        it on the left if is_left=True or on the right otherwise.'''
        super().__init__()
        self.screen_height = screen_height

        self.shape("square")
        self.color("white")
        self.setheading(UP)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        if is_left:
            self.setposition(-(screen_width/2 - 50), 0)
        else:
            self.setposition(screen_width/2 - 50, 0)
    

    def move_up(self) -> None:
        '''Moves the paddle up by 20 paces, if still within screen boundary.'''
        boundary = (self.screen_height / 2) - 10
        if self.ycor() + 50 >= boundary: 
            return

        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
    

    def move_down(self) -> None:
        '''Moves the paddle down by 20 paces, if still within screen boundary.'''
        boundary = (self.screen_height / 2) - 10
        if self.ycor() - 50 <= -boundary: 
            return
        
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)
