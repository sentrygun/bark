# Write a program to draw this. Assume the innermost square is 20 units per side,
# and each successive square is 20 units bigger, per side, than the one inside it.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawMultiSquare(t, sz, sq):
    """Get turtle t to draw multiple squares of sz side, each sz units larger, up to a total of sq squares"""

    runningtotal = 0
    for i in range(sq):
        runningtotal = runningtotal + sz
        drawSquare(t, runningtotal)
        t.up()
        # these following doubled commands could be shortened by instead travelling the hypotenuse of this effective right
        # triangle, but the equation for that is more complex to write than simply doing the action twice, and the
        # rounding errors may throw off the drawing at larger numbers of squares.
        t.right(90)
        t.forward(sz / 2)
        t.right(90)
        t.forward(sz / 2)

        t.right(180)
        t.down()

def main():
    wn = turtle.Screen()
    buddy = turtle.Turtle()

    wn.bgcolor("green")
    buddy.pencolor("pink")

    drawMultiSquare(buddy, 20, 5)

    wn.exitonclick()

main()