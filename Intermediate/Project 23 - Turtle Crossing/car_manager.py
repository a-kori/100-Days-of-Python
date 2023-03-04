from turtle import Turtle
import random
UP = 90
DOWN = 270

class CarManager:
    '''A class managing the movement of cars in the Turtle Crossing game.'''

    def __init__(self, screen_width: int, screen_length: int) -> None:
        '''Initializes the car manager with an empty list of cars.'''
        self.cars = []
        self.move_distance = 5
        self.screen_width = screen_width
        self.screen_length = screen_length


    def generate_car(self) -> None:
        '''Generates a new car with a random y coordinate and a random color.'''
        car = Turtle("square")
        car.setheading(180)
        car.shapesize(stretch_len=2, stretch_wid=1)

        rand_r = random.randint(0, 255)
        rand_g = random.randint(0, 255)
        rand_b = random.randint(0, 255)
        car.color((rand_r, rand_g, rand_b))

        car.penup()
        rand_y = random.randint(-self.screen_length/2 + 60, self.screen_length/2 - 45)
        car.setposition(self.screen_width/2 + 20, rand_y)

        self.cars.append(car)


    def move_cars(self) -> None:
        '''Moves the cars forward within the screen boundaries.'''
        for car in self.cars:
            if car.xcor() > -self.screen_width/2 - 20:
                car.forward(self.move_distance)
            else:
                self.cars.remove(car)
    

    def car_collided_with(self, player: Turtle) -> bool:
        '''Checks if the given player has collided with any of the cars.'''
        head_up = 6.7 if player.heading() == UP else 0.0
        head_down = 6.7 if player.heading() == DOWN else 0.0

        for car in self.cars:
            if player.xcor() > car.xcor() - 30 and player.xcor() < car.xcor() + 30:
                if player.ycor() + head_up > car.ycor() - 20 and player.ycor() - head_down < car.ycor() + 20:
                    return True
        return False


    def speed_up(self) -> None:
        '''Increases the moving distance by 5 paces.'''
        self.move_distance += 3
