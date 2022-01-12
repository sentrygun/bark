# Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes a turtle draw a regular polygon.
# When called with drawPoly(tess, 8, 50), it will draw a shape like this:

import turtle

def drawPoly(someturtle, somesides, somesize):
    """Gets someturtle to draw a polygon with somesides number of sides, at a side length of somesize"""

    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360 / somesides)

def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()

    drawPoly(tess, 8, 50)

    wn.exitonclick()

main()

# the assignment calls for colors, background green/pencolor pink