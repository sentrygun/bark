# Make a turtle stamp clock.

import turtle

wn = turtle.Screen()
clock = turtle.Turtle()

clock.shape('turtle')
clock.color('blue')
wn.bgcolor('green')

clock.stamp()
clock.up()

for hour in range(12):
    clock.forward(100)
    clock.down()
    clock.forward(10)
    clock.up()
    clock.forward(10)
    clock.stamp()
    clock.backward(120)
    clock.right(360 / 12)

wn.exitonclick()