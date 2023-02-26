from turtle import Turtle
MOVE_DISTANCE = 20
RIGHT = 0 
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self) -> None:
        '''Creates a new snake's body (initially consisting of 3 squares).'''
        self.snake = []
        for i in range(3):
            body_block = Turtle("square")
            body_block.color("white")
            body_block.penup()
            body_block.setposition(-20*i, 0)
            self.snake.append(body_block)
        self.head = self.snake[0]
    
    def move(self) -> None:
        '''Moves the snake by 20 paces in the direction of its current heading.'''
        for block_num in range(len(self.snake) - 1, 0, -1):
            new_pos = self.snake[block_num-1].position()
            self.snake[block_num].setposition(new_pos)
        self.head.forward(MOVE_DISTANCE)
    
    def right(self) -> None: 
        '''Turns the snake's heading to the East, if it's not facing West.'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self) -> None: 
        '''Turns the snake's heading to the North, if it's not facing South.'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self) -> None: 
        '''Turns the snake's heading to the West, if it's not facing East.'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def down(self) -> None: 
        '''Turns the snake's heading to the South, if it's not facing North.'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        