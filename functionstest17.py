# Write a function called fancySquare that will draw a square with fancy corners (sprites on the corners).
# You should implement and use the drawSprite function from above. For an even more interesting look,
# how about adding small triangles to the ends of the sprite legs.

import turtle

def drawSprite(t, legs, length):
    """Get turtle t to draw a sprite with legs number of branches of size length, with small triangles drawn at each end"""
    for x in range(legs):
        t.forward(length)

        t.left(30)
        t.forward(length / 10)
        for x in range(2):
            t.right(120)
            t.forward(length / 10)
        t.left(30)

        t.forward(length)
        t.left(180 + (360 / legs))

def fancySquare(t, squareLength, spriteLegs, spriteLength):
    """Get turtle t to draw a square of side size squareLength, with drawSprite creating a pattern at each corner of
    leg length spriteLength,with a number of legs equal to spriteLegs"""

    for x in range(4):
        t.forward(squareLength)
        drawSprite(t, spriteLegs, spriteLength)
        t.left(90)
        



def main():
    wn = turtle.Screen()
    fancy = turtle.Turtle()
    fancy.speed(0)
    fancy.hideturtle()

    # drawSprite(fancy, 10, 100)
    fancySquare(fancy, 200, 10, 50)
    wn.exitonclick()

main()

# due to the direction the turtle enters into drawSprite from being inconsistent, only every other sprite draws the same
# way. this slight offset probably doesn't matter in a small decorative pattern, but changes would need to be done if
# consistency between each sprite was desired. the fancySquare function could not simply be a loop four times, but would
# need to be broken into two chunks to reset the cursor position before and after every other sprite draw. not within
# the scope of this problem, but, worth noting?