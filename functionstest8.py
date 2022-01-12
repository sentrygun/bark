# Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.

import math

def areaOfCircle(r):
    """Returns area of a circle of r radius."""

    area = math.pi * float(r) ** 2.0
    return area

def main():
    r = input("Input radius of circle: ")

    print("The area of this circle is" , str(areaOfCircle(r)) + ".")

main()