# Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.

import turtle

def star(t, length):
    """Gets turtle t to draw a five-pointed star of side size length."""
    for x in range(5):
        t.forward(length)
        t.right(144)

def sky(t, length, stars):
    """Gets turtle t to draw a five-pointed star of side size length, stars number of times with a set distance between each"""
    for x in range(stars):
        star(t, length)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()
    # this only really works up to 5 times before it starts redrawing over already made stars, but that's the scope of the
    # requested program anyways.

def customStar(t, length, sides):
    """Gets turtle t to draw a sides-pointed star of side size length. Sides must be an odd number >=3 for intended function"""
    for x in range(sides):
        t.forward(length)
        t.right(180.0 - (180.0 / sides))


def main():
    wn = turtle.Screen()
    stella = turtle.Turtle()
    wn.bgcolor("lightgreen")
    stella.pencolor("pink")
    stella.pensize(5)
    wn.exitonclick()

    # star(stella, 100)
    #
    # stella.penup()
    # stella.backward(175)
    # stella.pendown()
    # sky(stella, 100, 5)
    customStar(stella, 100, 7)

main()