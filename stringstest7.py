# Write a function that removes all occurrences of a given letter from a string.

def letterRemove(string , letter):
    """Removes all instances of given letter from given string"""
    result = ""
    for chr in string:
        if chr != letter:
            result = result + chr
    
    return result

print(letterRemove("dog" , "o"))
