# Write a function that reverses its string argument.

def stringReverse(string):
    initial = ""
    for x in string:
        initial = x + initial
    return initial

def mirror(string):
    return string + stringReverse(string)


print(mirror("dog"))