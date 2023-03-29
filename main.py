from turtle import Screen
from paddle import Paddle

# Create and modify the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Arcade Game!")
screen.tracer(0)

# Variables

game_is_on = True

# Create a paddle
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=paddle1.go_up, key="Up")
screen.onkey(fun=paddle1.go_down, key="Down")
screen.onkey(fun=paddle2.go_up, key="w")
screen.onkey(fun=paddle2.go_down, key="s")

while game_is_on:
    screen.update()

screen.exitonclick()
