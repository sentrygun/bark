# Draw this pretty pattern.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square with sides of size sz"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def spirograph(t, sz, n):
    """Get turtle t to draw a number of squares of size side sz rotated upon themselves a short distance n times"""

    for i in range(n):
        drawSquare(t, sz)
        t.left(18)

def main():
    wn = turtle.Screen()
    spiral = turtle.Turtle()

    wn.bgcolor("green")
    spiral.pencolor("blue")

    spirograph(spiral, 30, 20)
    wn.exitonclick()

main()