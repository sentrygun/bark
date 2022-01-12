# Write a function called is_even(n) that takes an integer as an argument and returns
# True if the argument is an even number and False if it is odd.

def is_even(n):
    """Takes integer n and returns a boolean result as to whether is is even"""
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    """Takes integer n and returns a boolean result as to whether it is odd"""
    if is_even(n) == False:
        return True
    else:
        return False