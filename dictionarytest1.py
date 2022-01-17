# Write a program that allows the user to enter a string. It then prints a table 
# of the letters of the alphabet in alphabetical order which occur in the string 
# together with the number of times each letter occurs. Case should be ignored.

import string

def alphaTable(input):
    """Prints a table of the letters of the alphabet within an input and total of
    the occurrences of each, ignoring case."""
    input = input.lower()
    table = {}

    for x in input:
        if x in string.ascii_lowercase:
            if x in table:
                table[x] += 1
            else:
                table[x] = 1
    
    # print(table)
    # table.sort()
    # for (key , value) in table:
    #     print(key , value)

    ## turns out sorted(variable) is a thing you can do. this was not mentioned
    ## anywhere in the chapter! the only time sorting happens is when a dictionary
    ## is turned into a list and then sorted! i'm mad about this! why have the first
    ## question involve something that wasn't even mentioned offhand! argh!

    for x in sorted(table):
        print(x , table[x])

# bark = input("Please enter a sentence: ")

# print(alphaTable(bark))

