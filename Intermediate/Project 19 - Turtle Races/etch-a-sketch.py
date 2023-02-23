from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
tim.shape("turtle")

screen.listen()
screen.onkey(key="w", fun=lambda: tim.forward(10))
screen.onkey(key="s", fun=lambda: tim.backward(10))
screen.onkey(key="d", fun=lambda: tim.setheading(tim.heading() -10))
screen.onkey(key="a", fun=lambda: tim.setheading(tim.heading() + 10))
screen.onkey(key="c", fun=lambda: screen.reset())

screen.exitonclick()