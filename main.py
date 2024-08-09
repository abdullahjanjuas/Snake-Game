from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

# Building a screen for the game
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Control the screen updates
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

#Control the snake with arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True        
while game_is_on:
    # Update the screen after each move
    screen.update()
    # Add a small delay to control the speed
    time.sleep(0.1) 
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset_snake()
    
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
            
            
screen.exitonclick()
