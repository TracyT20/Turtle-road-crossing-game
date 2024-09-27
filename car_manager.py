from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        # self.shape("square")
        # self.shapesize(1,2)
        # self.color(random.choice(COLORS))
        # self.penup()
        # self.y_axis=random.randint(-250,250)
        # self.goto(250,self.y_axis)
        self.increment=STARTING_MOVE_DISTANCE
        self.CARS = []

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            self.y_axis=random.randint(-250,250)
            new_car.goto(300,self.y_axis)
            self.CARS.append(new_car)


    def move_cars(self):
        for car in self.CARS:
            car.backward(self.increment)

    def speed_up(self):
        self.increment += MOVE_INCREMENT
        for car in self.CARS:
            car.backward(self.increment)


