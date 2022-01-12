# Write a function that will return the number of digits in an integer.

import string

def digitCount(int):
    """Returns the number of digits in an integer"""
    count = 0
    int = str(int)
    for x in int:
        if x in string.digits:
            count = count + 1
    return count


print(digitCount(100549))