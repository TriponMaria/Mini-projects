import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.speed("fastest")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-230, 230))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def increment_speed(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
