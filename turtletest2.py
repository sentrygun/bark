import turtle
wn = turtle.Screen()
buddy = turtle.Turtle()

for triangleloop in range(2):
    buddy.forward(30)        # triangle 120
    buddy.left(120)
buddy.forward(30)

buddy.up()
buddy.left(30)
buddy.forward(100)
buddy.left(90)
buddy.down()

for squareloop in range(4):
    buddy.forward(30)
    buddy.left(90)

buddy.up()
buddy.forward(100)
buddy.down()

#hexagon = 60
for hexagonloop in range(6):
    buddy.forward(30)
    buddy.left(60)
    
buddy.up()
buddy.backward(200)
buddy.down()

#45
for octogonloop in range(8):
    buddy.forward(30)
    buddy.left(45)

wn.exitonclick