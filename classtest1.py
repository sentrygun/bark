import math

class Point:
    """Represents and manipulates x,y coordinates on a coordinate plane."""

    #def __init__(self) -> None:
    #    pass
    ## huh, why does __init__ autocomplete like this? is this like, an 'empty' constructor
    ## since the class needs a constructor method but if it isn't necessary for the class'
    ## task you may as well bypass it?

    def __init__(self , initX , initY):
        """Create a new point"""
        self.x = initX
        self.y = initY

# Add a distanceFromPoint method that works similar to distanceFromOrigin except that it takes a Point 
# as a parameter and computes the distance between that point and self.

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromPoint(self , point):
        """Determines the distance between a given point and the called Point object"""
        ## in this case, getX/Y wouldn't be necessary to call in the self's coordinates, but would it be a
        ## good idea to call them in like that anyways, for consistency's sake? doesn't seem like much of a
        ## big deal right here, but maybe in some cases the consistent formatting would be smarter than the
        ## 'shortcut'?

        xdiff = point.getX() - self.x
        ydiff = point.getY() - self.y

        dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
        return dist

# a = Point(4 , 3)
# b = Point(5 , 7)

# print(a.distanceFromPoint(b))

# Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point
# about the x-axis.

    def __str__(self):
        return "x = " + str(self.x) + " , y = " + str(self.y)

    def reflectX(self):
        """Returns a new point from given Point object with coordinates reflected across the x axis"""

        # self.y = -self.y

        return Point(self.x , -self.y)

        # being able to make the new point makes sense to me, but this new point needs a name to be called
        # or it'll just be floating in the ether, defined but uncallable.

        # oh, right, in order to name it you'd assign a variable to the result of the function, so you'd
        # still name it normally outside the function, that's not within the wheelhouse of the function.
        # overcomplicating things here, but realizing why i was mistaken is useful, since it'll stick.

        #name = Point(self.x , -self.y)
        
# a = Point(4 , 3)
# aFlip = a.reflectX()
# print(aFlip)

# Add a method slope_from_origin which returns the slope of the line joining the origin to the point
## slope formula = m=(y2-y1)/(x2-x1)

    def slope(self):
        """Returns the slope of a line between the origin to the given Point object"""

        try:
            result = (self.y - 0) / (self.x - 0)
            return result
        except ZeroDivisionError:
            return None
            ## a simple check to see if the x value is 0, which would result in dividing by zero,
            ## would be a better way to avoid dividing by zero, i just wanted to use a test case
            ## to prove out exceptions here!

# a = Point(4 , 3)
# print(a.slope())
# b = Point(0 , 0)
# print(b.slope())

# The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”). The coefficients a and b 
# completely describe the line. Write a method in the Point class so that if a point instance is given 
# another point, it will compute the equation of the straight line joining the two points. It must return 
# the two coefficients as a tuple of two values.



    def line(self , point):
        """Compares called Point object to another Point object and returns a tuple of the slope and y intercept"""

        if self.x == 0 and point.getX() == 0:
            slope = 0
        else:
            slope = (self.y - point.getY()) / (self.x - point.getX())

        yint = self.y - (slope * self.x)

        return (slope , yint)

        ## the question asks 'when will your method fail' which i assume refers to the issue of division by zero, but
        ## that should be accounted for with the if/else statement to assign slope to 0 if both x coordinates are 0,
        ## which should still be valid within the actual line equation.

# a = Point(4 , 3)
# b = Point(8 , 4)
# print(a.line(b))

# Add a method called move that will take two parameters, call them dx and dy. The method will cause the point to move 
# in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)

    def move(self , dx , dy):
        """Modifies the given Point object by shifting it a number of units equal to each given parameter for each axis"""

        self.x = self.x + dx
        self.y = self.y + dy

# a = Point(4 , 3)
# print(a)
# a.move(4 , 4)
# print(a)

# Given three points that fall on the circumference of a circle, find the center and radius of the circle.

## a simple version of this would simply be three points north, south, and east of the origin, all the same distance from
## the origin, but the program has to be able to refer between those and then use any given point on the circle to also be
## able to 'draw' the circle from that.

## the issue here is figuring a universal method to figure the center from three points, from there it's easy to determine
## the radius and it's done.

## take two lines, between i.e. point 1 and 2 and point 1 and 3, determine midpoints, draw perpendicular lines through those
## midpoints, where those perpendicular lines meet is the midpoint.

## that's the math, but how do i determine where the lines intersect through the code? when the points are equal would work,
## but i need to be able to test through the points on the line until that's the case, and be able to compare the two.

## i don't know how i would code out long-form algebraic movement across the = to emulate doing this on paper, nor can i
## find a straightforward equation to implement here. at this point it's just a math problem that i don't know how to
## show my work on in order to plug into code, which is an annoying problem to ram into. also, of course, this exercise
## doesn't have an answer i could reference to figure out the problem, but the incredibly easy move function exercise does
## have one.

# def circleCenter(p1 , p2 , p3):
    # """Returns the center and radius of a circle of three given points"""
    ## an if statement where, if the lines are directly on top of each other, that's the diameter and i can just
    ## pull a radius from that and easily determine the center with that

    ## an else statement where the more complex problem of using the perpendicular lines through the midpoints of the secant
    ## lines to find the center, then comparing the center to one of the points to determine a radius.
    ## the midpoint, slope, line, etc. methods of the Point class would be used in this function that sits outside the class,
    ## largely referencing it, as it's too specific to sit inside the Point class, but can pull everything it needs out of 
    ## that toolbox and utilize the getX and getY functions to pull specific data out of the reference points, which would themselves
    ## be Point objects.

    ## i get how this is an exercise utilizing classes and showing how you can pull methods from a class to create a more complex
    ## function like this one, i just can't figure out how to generate the math to plug into it, which sucks!


class Rectangle:
    def __init__(self , point , widthinput , heightinput):
        self.width = widthinput
        self.height = heightinput

        self.loc = point
        self.locX = point.getX()
        self.locY = point.getY()

    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height

    def getloc(self):
        return self.loc

    def getlocX(self):
        return self.locX

    def getlocY(self):
        return self.locY

    def __str__(self):
        return "Lower-left point: " + str(self.loc) + " Width: " + str(self.width) + " Height: " + str(self.height)

# Add a method area to the Rectangle class that returns the area of any instance:

    def area(self):
        """Returns the area of the Rectangle object"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle object"""
        return (self.width * 2) + (self.height * 2)

# Write a transpose method in the Rectangle class that swaps the width and the height of any rectangle instance:

    def transpose(self):
        """Mutates a Rectangle object to swap the width and height properties"""
        h = self.width
        w = self.height
        self.height = h
        self.width = w

# Write a new method in the Rectangle class to test if a Point falls within the rectangle. For this exercise, assume that a rectangle 
# at (0,0) with width 10 and height 5 has open upper bounds on the width and height, i.e. it stretches in the x direction from [0 to 10), 
# where 0 is included but 10 is excluded, and from [0 to 5) in the y direction. So it does not contain the point (10, 2).

    def testBounds(self , input):
        """Returns a boolean as to whether or not the input Point object falls within the bounds of the called Rectangle object"""
        if input.getX() in range(self.loc.getX() , self.width + 1
        ) and input.getY() in range(self.loc.getY() , self.height + 1):
        ## the exercise asks to define a range with an open upper bound, such that the end number of the width/height
        ## is not included. but, if the bottom and left edges of the rectangle are valid points for 'inside' in this case,
        ## why wouldn't the edges of the rectangle on the top and right edges be valid?
        ## testing seems to show doing it the way i'm doing it works all the way to the edges of the shape without going over,
        ## so what's the point of excluding a sliver along only two sides of the shape? i understand the idea behind an open end
        ## on a range, but it just doesn't make sense in this case.

        ## in order to align to what the exercise is asking, i'd need to reformat the statement to ask if it's >= the x/y coordinate
        ## and < the x/y coordinates with the width/height+1 added, so that i can easily include every number except the actual right
        ## edges. easy to swap that in, but, why?

            return True
        else:
            return False

    def testBoundary(self , x , y):
        """testBounds, but with a reference to x/y coordinates rather than a reference to a Point object"""
        if x in range(self.loc.getX() , self.width + 1
        ) and y in range(self.loc.getY() , self.height + 1):
            return True
        else:
            return False

    def diagonal(self):
        """Returns the length of a diagonal line running from the creation point of the Rectangle object to its furthest corner"""
        return math.sqrt((self.width ** 2) + (self.height ** 2))

# In games, we often put a rectangular “bounding box” around our sprites in the game. We can then do collision detection between, say, 
# bombs and spaceships, by comparing whether their rectangles overlap anywhere.

# Write a function to determine whether two rectangles collide. Hint: this might be quite a tough exercise! Think carefully about all 
# the cases before you code.

def collisionTest(r1 , r2):
    """Returns a boolean as to whether two Rectangle objects overlap"""
    ## i need to be able to reference each point inside of one rectangle, and then i can run testBounds on it within the other for each
    ## point. like in image processing, i can nest a for loop inside a for loop to iterate over the entirety of a rectangular object.
    ## each point has to be checked, if you take a shortcut (like one of the user answers posted in the discussions) you run the risk of
    ## the colliding object being able to slide through the sides on certain edges, or even exist within the other collided object as long
    ## as it didn't touch the edges.

    ### the only issue i see with relating this to image processing by pixel is that it's upside down, originating from the lower left
    ### corner as opposed to the upper left corner. time to test and see if this makes a difference/how i need to change it to make it work!

    for row in range(r1.getlocY() , r1.getheight() + 1):
        for col in range (r1.getlocX() , r1.getwidth() + 1):
            ## i probably need to rewrite the bounding check to make sure it isn't just creating a ton of objects that it only references
            ## once. maybe it's not a big deal, but that sounds like a terrible idea to let happen.
            if r2.testBoundary(col , row) == True:
                return True
    ### as i figured, this goes downward, so it's probably checking an equivalently sized rectangle, underneath r1. i can use this, i just
    ### need to ensure i start at the upper left corner. i get the feeling there's a better way to check this, or an easy way to flip it,
    ### but nothing comes to mind at the moment.

    ### unfortunately, i'm coming up dry on how to write it such that it starts from the upper left, or ways to flip it the other way around.
    ### it's also very possible this is a terrible way to actually implement this!

    return False
    

        

r = Rectangle(Point(0 , 0) , 10 , 5)
r2 = Rectangle(Point(0 , 0) , 5 , 2)
r3 = Rectangle(Point(55 , 55) , 20 , 20)
# print(r.area())
# print(r.perimeter())
# print(r)
# r.transpose()
# print(r)
# print(r.testBounds(Point(0 , 2)))
# print(r.testBounds(Point(-5, -5)))
# print(r.testBounds(Point(10 , 5)))
# print(r.testBounds(Point(10.1 , 5.1)))
print(collisionTest(r , r2))
print(collisionTest(r , r3))