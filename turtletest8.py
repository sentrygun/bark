# A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is
# 360 / n degrees. Write a program to draw a sprite where the number of legs is provided by the user.

import turtle

legs = input("Please input the number of legs of the sprite: ")

wn = turtle.Screen()
sprite = turtle.Turtle()



for x in range(int(legs)):
    sprite.forward(50)
    sprite.back(50)
    sprite.right(360 / int(legs))

wn.exitonclick()