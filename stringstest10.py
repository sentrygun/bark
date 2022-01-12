# Write a function that counts how many non-overlapping occurences of a substring appear in a string.

# plan: use index to find the string's left side, then use that information with the string length
# to determine where to slice to begin the next search loop. continue until end of string.

import string

def howMany(input, substring):
    """Returns the number of instances of substring within input"""

    instance = 0
    start = 0
    #end = None                 # not necessary here, not counting characters, find has own fail condition
    #chrlimit = len(input)

    #while chr < len(input):
    while input.find(substring , start) != -1:
        instance = instance + 1
        start = input.find(substring , start) + len(substring)
    return instance


print(howMany("bark meow bark meow bark" , "meow"))