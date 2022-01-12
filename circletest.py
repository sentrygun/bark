import turtle
import math

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * math.pi * radius
    sideLength = circumference / 360
    anyTurtle.up()
    anyTurtle.goto(0, radius)
    anyTurtle.down()
    drawPolygon(anyTurtle, sideLength, 360)
    #anyTurtle.up()
    #anyTurtle.goto(0, 0)
    #anyTurtle.down()
    
def drawFilledCircle(anyTurtle, radius, color):
    anyTurtle.fillcolor(color)
    anyTurtle.begin_fill()
    drawCircle(anyTurtle, radius)
    anyTurtle.end_fill()


wn = turtle.Screen()
wheel = turtle.Turtle()
wheel.speed(0)

#drawCircle(wheel, 20)
drawFilledCircle(wheel, 20, "red")

# When drawing in activecode, a line appears along the radius, suggesting that the fill points don't
# fill in between these points. In vscode, the line along the radius doesn't appear. More specific
# code would avoid the line, but if the bug only appears in activecode, does this matter?

wn.exitonclick()
