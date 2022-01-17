# Using the text file studentdata.txt write a program that prints out the names of students 
# that have more than six quiz scores.

# infile = open("studentdata.txt" , "r")

# line = infile.readline()
# while line:
#     scores = line.split()
#     #print(line)
#     if len(scores) > 7:
#         print(scores[0])
#     line = infile.readline()
    
# infile.close()


# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates
# the average grade for each student, and print out the student’s name along with their average grade.

# infile = open("studentdata.txt" , "r")

# line = infile.readline()
# while line:
#     scores = line.split()
#     avg = 0
#     for x in scores[1:]:
#         avg += int(x)
#     avg = avg / len(scores[1:])
    
#     print(scores[0] + ":" , avg)
        
#     line = infile.readline()
# infile.close()

# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates 
# the minimum and maximum score for each student. Print out their name as well.


# infile = open("studentdata.txt" , "r")

# line = infile.readline()
# while line:
#     scores = line.split()
#     min = int(scores[1])
#     max = int(scores[1])
#     for x in scores[1:]:
#         if int(x) > max:
#             max = int(x)
#         elif int(x) < min:
#             min = int(x)
#     print(scores[0] + ": Max:" , str(max) + ", Min:" , str(min) + ".")
#     line = infile.readline()
# infile.close()

# book answer uses max and min functions. makes sense, and makes the whole thing shorter/more
# straightforward, but i opted to write it out long here to recall and practice with some odds
# and ends i haven't touched for a bit. in a non-practice environment i would have looked up
# and utilized the min and max functions instead of making a for loop to cover it.

# book answer also uses a for loop to redefine every number in the dataset as an integer before
# plugging them into the min/max functions inside the print statement. considering the way it's
# being used with the min/max functions, this works fine. probably says something about the
# book answers that there's an unclosed parenthesis causing a syntax error though. did they really
# not double check that the answers work correctly in their own activecode environment?


# At the bottom of this page is a very long file called mystery.txt The lines of this file contain 
# either the word UP or DOWN or a pair of numbers. UP and DOWN are instructions for a turtle to 
# lift up or put down its tail. The pairs of numbers are some x,y coordinates. Write a program 
# that reads the file mystery.txt and uses the turtle to draw the picture described by the commands 
# and the set of points.

import turtle

def mysteryturtle(t):
    infile = open("mystery.txt" , "r")
    line = infile.readline()
    while line:
        contents = line.split()
        if contents[0] == "UP":
            t.penup()
        elif contents[0] == "DOWN":
            t.pendown()
        else:
            t.goto(int(contents[0]) , int(contents[1]))
        line = infile.readline()
    infile.close()

sherlock = turtle.Turtle()
wn = turtle.Screen()

sherlock.speed(10)
mysteryturtle(sherlock)
wn.exitonclick()

## Primary hangup on this was forgetting to reference the correct variable during the if statements,
## accidentally calline 'line' instead of 'contents' when looking for "UP" and "DOWN". gotta avoid
## autopilot when typing out variables!