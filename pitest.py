import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.tracer(100)

fred.up()
fred.speed(0)
fred.hideturtle()

insideCount = 0

numdarts = 10000
for i in range(numdarts):
    randx = random.uniform(-1, 1)
    randy = random.uniform(-1, 1)

    fred.goto(randx, randy)
    # fred.stamp()
    if fred.distance(0,0) <= 1:
        fred.pencolor("red")
        fred.stamp()
        insideCount = insideCount + 1
    else:
        fred.pencolor("blue")
        fred.stamp()

pi = (insideCount / numdarts) * 4

print(pi)

wn.exitonclick()
