# Write a function findHypot. The function will be given the length of two sides of a
# right-angled triangle and it should return the length of the hypotenuse.
# (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

import math

def findHypot(a , b):
    result = (math.sqrt(a ** 2 + b ** 2))
    return result
# This... had nothing to do with booleans? Why was this in here?

def is_rightangled(a , b , c):
    if abs(c - (findHypot(a , b))) < 0.001:
        return True
    else:
        return False

def main():
    a = input("Input the first known side of the right triangle: ")
    b = input("Input the second known side of the right triangle: ")
    c = input("Input the hypotenuse of this triangle: ")

    a = float(a)
    b = float(b)
    c = float(c)

    #print("The hypotenuse of this triangle is" , str(findHypot(a , b)) + ".")
    if is_rightangled(a, b, c) == True:
        print("This triangle is right angled.")
    else:
        print("This triangle is NOT right angled.")

main()

