# The two spirals in this picture differ only by the turn angle. Draw both.

import turtle

def labyrinth(t, length, angle, sides):
    """Get turtle t to draw a spiral square pattern of increasing side size length and turn angle angle, sides number of times."""

    runningtotal = 0
    for x in range(sides):
        runningtotal = runningtotal + length
        t.right(angle)
        t.forward(runningtotal)

# whoops, that's not what it was asking for, accumulating the angle gets way out of control. Problem just wanted me
# to input a different angle into the original, duh.
# def twisty_labyrinth(t, length, angle, sides):
#     """Get turtle t to draw a spiral twisting square pattern of increasing side size length 
#     and turn angle angle, sides number of times."""

#     runningtotal = 0
#     angletotal = angle
#     for x in range(sides):
#         runningtotal = runningtotal + length
#         angletotal = angletotal + 2
#         t.right(angletotal)
#         t.forward(runningtotal)

# I figured this going in that running a separate accumulator while running the other function wasn't going to work, 
# but I wanted to give it a shot and see what happened anyways. Unsurprisingly, this ain't it.
#def twist(t, length, angle, sides):
#     """Get turtle t to use labyrinth with increasing angle."""

#     angletotal = angle
#     for x in range(sides):
#         angletotal = angletotal + 2
#         labyrinth(t, length, angle, sides)

# Probably don't be in a rush to overcomplicate things! This was time wasted due to not thinking through the
# actual complexity of the problem.

def main():
    wn = turtle.Screen()
    minos = turtle.Turtle()
    minos.pencolor("blue")
    wn.bgcolor("lightgreen")

    minos.speed(0)
    minos.hideturtle()

    #labyrinth(minos, 2, 90, 100)
    labyrinth(minos, 2, 88, 100)


main()