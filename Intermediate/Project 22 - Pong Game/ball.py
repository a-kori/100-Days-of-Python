from turtle import Turtle
from paddle import Paddle
import random

class Ball(Turtle):
    '''A class describing the ball's appearance and behavior in Pong.'''

    def __init__(self) -> None:
        '''Creates a 20x20 white ball and randomly defines its movement direction.'''
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 1

        self.x_increment = random.choice([-1, 1])
        self.y_increment = random.choice([-1, 1])


    def move(self, paddles) -> None:
        '''Triggers the ball's further movement.'''
        # Detect collision with upper/lower wall or paddle edge and bounce back
        if self.ycor() <= -280 or self.ycor() >= 290:
            self.y_increment *= -1
        elif self.paddle_edge_hit(paddles[0]) or self.paddle_edge_hit(paddles[1]):
            self.y_increment *= -1
        
        # Detect collision with paddle and bounce back
        if self.paddle_hit(paddles[0]) or self.paddle_hit(paddles[1]):
            self.x_increment *= -1
            self.move_speed += 1

        self.setposition(self.xcor() + self.x_increment, self.ycor() + self.y_increment)


    def paddle_edge_hit(self, paddle: Paddle) -> bool:
        '''Checks if a paddle was hit on the edge.'''
        if paddle.xcor() > 0:
            if self.xcor() > paddle.xcor() - 9:
                if self.ycor() >= paddle.ycor() - 60 and self.ycor() <= paddle.ycor() - 59:
                    return True
                if self.ycor() <= paddle.ycor() + 60 and self.ycor() >= paddle.ycor() + 59:
                    return True
            return False
        else:
            if self.xcor() < paddle.xcor() + 9:
                if self.ycor() >= paddle.ycor() - 60 and self.ycor() <= paddle.ycor() - 59:
                    return True
                if self.ycor() <= paddle.ycor() + 60 and self.ycor() >= paddle.ycor() + 59:
                    return True
            return False


    def paddle_hit(self, paddle: Paddle) -> bool:
        '''Checks if a paddle was hit on the front.'''
        if paddle.xcor() > 0:
            if self.xcor() >= paddle.xcor() - 10 and self.xcor() <= paddle.xcor() - 9:
                return self.ycor() >= paddle.ycor() - 61 and self.ycor() <= paddle.ycor() + 61
            return False
        else:
            if self.xcor() <= paddle.xcor() + 10 and self.xcor() >= paddle.xcor() + 9:
                return self.ycor() >= paddle.ycor() - 61 and self.ycor() <= paddle.ycor() + 61
            return False
