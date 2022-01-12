# Make a drawing.

import turtle

wn = turtle.Screen()
draw = turtle.Turtle()

draw.pensize(5)
draw.pencolor("azure")
wn.bgcolor("black")
draw.hideturtle()
draw.speed(10)


for x in range(128):
    draw.forward(x ** 2)
    draw.right(x * 4)

wn.exitonclick