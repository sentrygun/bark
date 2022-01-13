# Write a function called average that takes a list of numbers as a parameter 
# and returns the average of the numbers.

def average(list):
    """Returns the average of the integers in a list"""
    init = 0

    for num in list:
        if isinstance(num , int):
            # this was an additional line to ensure the function only handled integers (floats could
            # be included by converting integers into floats and then working with floats) in order
            # to avoid doing math to invalid objects, but initial attempts to implement this
            # were along the lines of 'if num == int:', my thought being that I could check to see if
            # a variable was a certain type by seeing if it is equivalent to a type, but this was just
            # skipping the whole loop.
            #
            # turns out, there's a whole function to return a boolean result from checking a variable
            # against a type!

            # print(type(num))
            init += num
    
    # print(len(range(list)))           ## was flipping len and range around, adding too many things
    # print(len(list))
    avg = init / len(list)

    return avg

# Write a Python function named max that takes a parameter containing a nonempty list of integers
# and returns the maximum value. (Note: there is a builtin function named max but pretend you 
# cannot use it.)

def maxAlt(list):
    """Returns the maximum integer value of a list"""
    if isinstance(list[0] , int):
        init = list[0]
    else:
        print("Error: List must be composed of integers.")
        return None
    
    for num in list:
        if isinstance(num , int):
            if num > init:
                init = num
        else:
            print("Error: list must be composed of integers.")
            return None

    return init
    ### these isinstance uses are overkill for the question, i'm just having fun testing to see
    ### how i can use it to skip invalid data or throw errors to the user

def sum_of_squares(xs):
    """Returns the sum of the squares of a list of integers"""
    init = 0
    for num in xs:
        init += num ** 2

    return init

# Write a function to count how many odd numbers are in a list.

def oddCheck(list):
    """Returns the amount of odd integers within a list"""

    result = [x for x in list if x % 2 == 1]
    # i wanted to test doing this in a list comprehension. i could have just done it in a
    # for loop that accumulates a value if x % 2 == 1, but i've done that five hundred times now.
    # the list comprehension makes a new listand then i reference that value to get the result
    # instead. idk, list comprehensions are cool and straightforward, so i think i prefer handling
    # it this way instead? i don't see any reason it would be bad for this in particular.
    
    return len(result)

# Sum all the elements in a list up to but not including the first even number.

def sumFirstOdds(list):
    """Adds together all odd numbers in a list until an even occurs, returns sum of preceding odds"""
    init = 0

    for num in list:
        if num % 2 == 1:
            init += num
        else:
            return init

    return init

## This seems far more straightforward than the book's answer:
# def sum(lst):
    # sum = 0
    # index = 0
    # while index < len(lst) and lst[index] % 2 != 0:
    #     sum = sum + lst[index]
    #     index = index + 1
    # return sum
##
## i get why a while statement works here, but the composition of the while statement to
## prevent an infinite loop and properly iterate down the list is inherently more complex
## than just having a for loop that terminates early.
## 
## i guess it's a way to inject more while loops into the questions, but the for loop version
## came so naturally and simply that i just went straight for that and got the results i wanted easily.


print(sumFirstOdds([1 , 3 , 5 , 7 , 10 , 1111111 , 12]))



# print(oddCheck([1 , 3 , 2 , 4]))

# print(sum_of_squares([2, 3, 4]))

# print(maxAlt([1,5,7,2,9,777,2,7]))

# print(average([1,2,3,4,5,6]))