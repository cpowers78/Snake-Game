from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

sully = Snake()
food = Food()
scoreboard = ScoreBoard()




sully.create_snake()
screen.listen()
screen.onkeypress(sully.up, "Up")
screen.onkeypress(sully.down, "Down")
screen.onkeypress(sully.left, "Left")
screen.onkeypress(sully.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sully.move()
    #Detect collision with food
    if sully.head.distance(food) < 15:
        food.refresh()
        sully.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if sully.head.xcor() > 280 or sully.head.xcor() < -280 or sully.head.ycor() > 280 or sully.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()


    for segment in sully.segments[1:]:
        if sully.head.distance(segment) < 15:
            game_is_on= False
            scoreboard.gameover()








screen.exitonclick()
