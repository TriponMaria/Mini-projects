import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from turtle import Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Level up
    if player.ycor() > 280:
        scoreboard.level += 1
        scoreboard.score()
        car_manager.increment_speed()
        player.finish()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()