# Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls drawPoly
# from the previous question to have its turtle draw a equilateral triangle.

import turtle

def drawPoly(someturtle, somesides, somesize):
    """Gets someturtle to draw a polygon with somesides number of sides, at a side length of somesize"""

    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360 / somesides)

def drawEquitriangle(someturtle, somesize):
    """Gets someturtle to draw an equilateral triangle of lengths somesize using drawPoly"""

    somesides = 3
    drawPoly(someturtle, somesides, somesize)

def main():
    triangle = turtle.Turtle()
    wn = turtle.Screen()

    drawEquitriangle(triangle, 50)


main()