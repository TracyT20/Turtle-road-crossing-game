import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
scoreboard=Scoreboard()

# CARS=[]
# #generate cars
# for i in range(8):
#     new_car=CarManager()
#     CARS.append(new_car)
car_manager=CarManager()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > player.finish:
        player.reset_player()
        scoreboard.update_level()
        car_manager.speed_up()
    for car in car_manager.CARS:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on=False


screen.exitonclick()

