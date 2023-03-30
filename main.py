from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Create and modify the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Arcade Game!")
screen.tracer(0)

# Variables
game_is_on = True
collision_with_wall = 285
collision_with_paddle = 325
out_of_bounds = 385

# Create a paddle
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score_r = Scoreboard((100, 200))
score_l = Scoreboard((-100, 200))

screen.listen()
screen.onkey(fun=paddle1.go_up, key="Up")
screen.onkey(fun=paddle1.go_down, key="Down")
screen.onkey(fun=paddle2.go_up, key="w")
screen.onkey(fun=paddle2.go_down, key="s")


while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > collision_with_wall or ball.ycor() < -collision_with_wall:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle1) < 50 and ball.xcor() > collision_with_paddle \
            or ball.distance(paddle2) < 50 and ball.xcor() < -collision_with_paddle:
        ball.bounce_x()

    # Detect when the R paddle misses
    if ball.xcor() > out_of_bounds:
        ball.reset_position()
        score_l.increase_score()

    # Detect when the L paddle misses
    if ball.xcor() < -out_of_bounds:
        ball.reset_position()
        score_r.increase_score()

screen.exitonclick()
