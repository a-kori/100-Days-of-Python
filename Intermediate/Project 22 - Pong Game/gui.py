from turtle import Turtle

def draw_dashed_line(screen_height: int) -> None:
    '''Draws a vertical dashed line in the middle of the screen.'''
    repeat = (screen_height - 40) // 5
    start = (screen_height / 2) - 20 

    tracker = 0
    for i in range(repeat):
        dot = Turtle("square")
        if tracker == 0 or tracker == 4 or tracker == 5:
            dot.color("black")
        else:
            dot.color("white")
        dot.penup()
        dot.shapesize(stretch_len=0.25, stretch_wid=0.25)
        dot.setposition(0, start + 2.5 - 5*i)

        if tracker == 5:
            tracker = 1
        else:
            tracker += 1
