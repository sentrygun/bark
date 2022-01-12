# Draw a pentagram.

import turtle
wn = turtle.Screen()
penta = turtle.Turtle()

for x in range(5):
    penta.forward(50)
    penta.right(144)
wn.exitonclick