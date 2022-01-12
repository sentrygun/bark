# Assign to a variable in your program a triple-quoted string that contains your favorite
# paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some
# inspirational verses, etc.

# Write a function that counts the number of alphabetic characters (a through z,
# or A through Z) in your text and then keeps track of how many are the letter ‘e’. Your
# function should print an analysis of the text like this:

# Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.

import string

teststr = """Assign to a variable in your program a triple-quoted string that contains your favorite 
paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some 
inspirational verses, etc."""

#print(string.ascii_letters)

totalcount = 0
e_count = 0
for chr in teststr:
    if chr in string.ascii_letters:
        totalcount = totalcount + 1
    if chr == "e" or chr == "E":
        e_count = e_count + 1

print("Your text contains" , totalcount , "alphabetic characters, of which" , e_count , "are 'e'.")
