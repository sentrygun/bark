# Write a function called drawSprite that will draw a sprite. The function will need parameters for the turtle,
# the number of legs, and the length of the legs. Invoke the function to create a sprite with 15 legs of length 120.

import turtle

def drawSprite(t, legs, length):
    """Get turtle t to draw an image with legs lines coming from the origin, of size length"""

    for x in range(legs):
        t.forward(length)
        
        t.penup()
        t.backward(length)
        t.pendown()
        # penup and pendown are unnecessary since the line would just draw back over itself,
        # but are included for the sake of cleanliness.

        t.right(360 / legs)
        

def main():
    wn = turtle.Screen()
    spider = turtle.Turtle()

    drawSprite(spider, 15, 120)

main()