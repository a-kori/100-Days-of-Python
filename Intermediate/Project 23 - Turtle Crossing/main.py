import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from level_tracker import LevelTracker

# Setting up the screen
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating the level tracker, the car manager and the player's turtle
level_tracker = LevelTracker(screen.window_width(), screen.window_height())
car_manager = CarManager(screen.window_width(), screen.window_height())
player = Player(screen.window_width(), screen.window_height())

# Creating some behind-the-scenes cars
for i in range(200):
    if i % 5 == 0:
        car_manager.generate_car()
    car_manager.move_cars()

# Binding arrow keys to the player's control commands
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Right", fun=player.move_right)
screen.onkey(key="Left", fun=player.move_left)

# Creating and moving the cars forward 
# until the player collides with one
deciseconds = -1
car_frequency = 5
while True:
    deciseconds += 1
    time.sleep(0.1)
    screen.update()

    # Detecting collision with a car
    if car_manager.car_collided_with(player):
        break
    
    # Increasing the cars' speed on each level
    # and the number of cars every two levels
    if player.crossed_finish_line():
        player.set_starting_position()
        car_manager.speed_up()
        
        level_tracker.increase_level()
        if level_tracker.level % 2 == 1 and car_frequency > 1:
            car_frequency -= 1

    # Moving the cars and creating a new one 
    # every 'car_frequency' deciseconds
    if deciseconds % car_frequency == 0:
        car_manager.generate_car()
    car_manager.move_cars()

screen.update()
level_tracker.end_game()
screen.exitonclick()
