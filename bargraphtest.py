import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape

    
    t.left(90)
    if height < 0:
        t.penup()
        t.forward(5)
        t.write(str(height))
        t.back(5)
        t.pendown()
    t.forward(height)
    if height >= 0:
        t.up()                       # draw label for bar
        t.forward(5)
        t.write(str(height))
        t.back(5)
        t.down()

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)

    t.end_fill()                 # stop filling this shape



xs = [48, -50, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
minheight = min(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes

wn.bgcolor("lightgreen")
if minheight > 0:
    lowerbound = 0
else:
    lowerbound = minheight - border

wn.setworldcoordinates(0-border, lowerbound, 40*numbars+border, maxheight+border)

tess = turtle.Turtle()           # create tess and set some attributes
tess.speed(0)
tess.hideturtle()
tess.color("blue")
# tess.fillcolor("red")
tess.pensize(3)



for a in xs:
    if a > 200:
        tess.fillcolor("red")
    elif a >= 100 and a < 200:
        tess.fillcolor("yellow")
    else:
        tess.fillcolor("green")
    drawBar(tess, a)

wn.exitonclick()
