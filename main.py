from turtle import Turtle, Screen

# Create and modify the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Arcade Game!")
screen.tracer(0)

# Variables
position = (350, 0)
game_is_on = True

# Create a paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(position)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(fun=go_up, key="Up")
screen.onkey(fun=go_down, key="Down")

while game_is_on:
    screen.update()

screen.exitonclick()
