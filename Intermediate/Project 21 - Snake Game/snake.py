from turtle import Turtle
MOVE_DISTANCE = 20

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
    
    def move(self) -> None:
        '''Moves the snake by 20 paces in the direction of its current heading.'''
        for block_num in range(len(self.snake) - 1, 0, -1):
            new_pos = self.snake[block_num-1].position()
            self.snake[block_num].setposition(new_pos)
        self.snake[0].forward(MOVE_DISTANCE)
        