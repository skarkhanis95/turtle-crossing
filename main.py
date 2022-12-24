from turtle import Turtle,Screen

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
def move():
    player.forward(5)
player = Turtle()
player.shape("turtle")
player.setheading(90)
screen.listen()
screen.onkey(fun=move, key="Up")

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()