# Write a function called remove_dups that takes a string and creates a new string
# by only adding those characters that are not already present. In other words,
# there will never be a duplicate letter added to the new string.

import string

def remove_dups(input):
    """Takes a string input and returns a string only containing every alphabetic character not
    present in the input"""

    alpha = string.ascii_letters
    result = ""

    for x in alpha:
        if x not in input:
            result = result + x

    return result

print(remove_dups("the quick brown fox jumps over the lazy doTHE QUICK BROWN FOX JUMPS OVER THE LAZY DO"))

#print("the quick brown fox jumps over the lazy do".upper())

#print(string.ascii_letters)