# Write a program that asks the user for the number of sides, the length of the side, the color,
# and the fill color of a regular polygon. The program should draw the polygon and then fill it in.

polysides = input("Please input the number of sides of the regular polygon:")
polysides = int(polysides)

polylength = input("Please input the length of the sides of the regular polygon:")
polylength = int(polylength)

polycolor = input("Please input the color of the lines of the regular polygon:")
polyfill = input("Please input the color of the inside of the regular polygon:")

import turtle
wn = turtle.Screen()
buddy = turtle.Turtle()

# repeat for loop based on number of sides, determine forward by length, define turtle color and fill up front

buddy.pencolor(polycolor)
buddy.fillcolor(polyfill)

buddy.begin_fill()
for sides in range(polysides):
    buddy.forward(polylength)
    buddy.left(360 / polysides)
buddy.end_fill()

wn.exitonclick