# Use the drawsquare function we wrote in this chapter in a program to draw the image shown below.
# Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the
# ending point of the last square when the program ends.)


import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawSeries(t, total, sz):
    """Get turtle t to draw total number of squares of sz side"""

    for i in range(total):
        drawSquare(t, sz)
        t.up()
        t.forward(sz + 10)
        t.down()


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

#drawSquare(alex,20)
drawSeries(alex, 5, 20)

wn.exitonclick()
