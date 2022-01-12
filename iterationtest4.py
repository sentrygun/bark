# Modify the walking turtle program so that rather than a 90 degree left or right turn
# the angle of the turn is determined randomly at each step.

import random
import turtle

# Define the following: a movement function involving the window and a turtle, a collision check
# involving two turtles, an isinScreen check involving the window and a turtle. 

def isInScreen(w , t):
    """Checks whether turtle t is within the visible bounds of screen w and returns a boolean"""

    leftBound = -w.window_width() / 2
    rightBound = w.window_width() / 2
    bottomBound = -w.window_height() / 2
    topBound = w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX < leftBound or turtleX > rightBound:
        stillIn = False
    if turtleY < bottomBound or turtleY > topBound:
        stillIn = False
    return stillIn


def turtleMove(t):
    """Moves turtle t in 50 unit steps at random angles"""
    coin = random.randrange(0 , 2)
    if coin == 0:
        t.left(random.randrange(0 , 360))
    else:
        t.right(random.randrange(0 , 360))
    t.forward(50)


def turtleRandomizer(w, t):
    """Places turtle t in a random position within screen w"""
    leftBound = -w.window_width() / 2
    rightBound = w.window_width() / 2
    bottomBound = -w.window_height() / 2
    topBound = w.window_height() / 2

    t.penup()

    t.goto(random.randrange(int(leftBound) , int(rightBound)) , random.randrange(int(bottomBound) , int(topBound)))

    t.pendown()

def collisionCheck(t1 , t2):
    """Checks whether turtles t1 and t2 are within 2 units, and returns a boolean"""
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def turtleBounce(w , t1 , t2):
    """Extends turtleMove for two turtles t1 and t2 infinitely by rotating a turtle when it approaches
    another turtle or the bounds of screen w"""
    while isInScreen(w , t1) == True and isInScreen(w , t2) == True and collisionCheck(t1 , t2) == False:
        turtleMove(t1)
        turtleMove(t2)
    if isInScreen(w , t1) == False or collisionCheck(t1 , t2) == True:
        t1.right(180)
        t1.forward(200)
        turtleMove(t1)
    if isInScreen(w , t2) == False or collisionCheck(t1 , t2) == True:
        t2.right(180)
        t2.forward(200)
        turtleMove(t2)
    turtleBounce(w , t1 , t2)


def main():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    wn = turtle.Screen()


    turtleRandomizer(wn , t1)
    turtleRandomizer(wn , t2)

    turtleBounce(wn , t1 , t2)
    wn.exitonclick()

# Rewriting this from the top down was time-consuming, but the code had started to become messy
# and reorienting myself helped to actually nail down what I wanted out of this.

main()

        









# def isInScreen(w,t):
#     leftBound = - w.window_width() / 2
#     rightBound = w.window_width() / 2
#     topBound = w.window_height() / 2
#     bottomBound = -w.window_height() / 2

#     turtleX = t.xcor()
#     turtleY = t.ycor()

#     stillIn = True
#     if turtleX > rightBound or turtleX < leftBound:
#         stillIn = False
#     if turtleY > topBound or turtleY < bottomBound:
#         stillIn = False

#     return stillIn

# def turtle_randomizer(w , t):
#     """Places turtle t randomly within the bounds of the drawing space w, within 50 units"""
#     t.penup()

#     leftBound = - w.window_width() / 2
#     rightBound = w.window_width() / 2
#     topBound = w.window_height() / 2
#     bottomBound = -w.window_height() / 2
#     # These come in as floats, but I need ints as arguements for randrange?

#     #print(type(leftBound))
#     #print(w.window_width)

#     t.goto(random.randrange(leftBound, rightBound) , random.randrange(bottomBound, topBound))

#     # the problem was that i had topBound , bottomBound listed in the second randrange, which was the
#     # wrong way around. the range was invalid which was spitting errors.

#     t.pendown()

# def collision_detection(t1 , t2):
#     """Reads the distance between turtles t1 and t2 and returns a boolean as to whether they are within
#     2 units of each other."""
#     if turtle.distance(t1 , t2) > 2:
#         return False
#     else:
#         return True

# def turtle_move(w , t1 , t2):
#     """Gets turtles t1 and t2 to move about at random angles within window w, turning 180 degrees
#     when collision_detection returns True or when approaching the bounds of window w"""


#     if isInScreen(w , t) or collision_detection():
#         coin = random.randrange(0, 2)
#         if coin == 0:
#             t.left(random.randrange(0 , 360))
#         else:
#            t.right(random.randrange(0 , 360))

#     t.forward(50)


# t1 = turtle.Turtle()
# t2 = turtle.Turtle()

# wn = turtle.Screen()

# t1.shape('turtle')
# t2.shape('turtle')
# t1.pencolor('blue')
# t2.pencolor('red')

# turtle_randomizer(wn , t1)
# turtle_randomizer(wn , t1)

# turtle_move(wn , t1)
# turtle_move(wn, t2)

# # leftBound = - wn.window_width() / 2
# # rightBound = wn.window_width() / 2
# # topBound = wn.window_height() / 2
# # bottomBound = -wn.window_height() / 2

# # t.penup()

# # t.goto(random.randrange(leftBound , rightBound) ,
# # random.randrange(bottomBound , topBound))

# # t.pendown()

# # t2.penup()

# # t2.goto(random.randrange(leftBound , rightBound) ,
# # random.randrange(bottomBound , topBound))

# # t2.pendown()


# # if isInScreen(wn,t):
# #     coin = random.randrange(0, 2)
# #     if coin == 0:
# #         t.left(random.randrange(0 , 360))
# #     else:
# #         t.right(random.randrange(0 , 360))

# #     coin2 = random.randrange(0 , 2)
# #     if coin2 == 0:
# #         t2.left(random.randrange(0 , 360))
# #     else:
# #         t2.right(random.randrange(0 , 360))

# #     t.forward(50)
# #     t2.forward(50)

# wn.exitonclick()