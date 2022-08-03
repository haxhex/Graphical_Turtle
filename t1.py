from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("classic")

def turtle_color():
    R = random.random()
    G = random.random()
    B = random.random()
    return tim.pencolor(R, G, B)

tim.speed("fastest")

for _ in range(72):
    turtle_color()
    tim.circle(100)
    tim.left(5)
    

screen = Screen()
screen.exitonclick()