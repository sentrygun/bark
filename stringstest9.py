# Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).

def palindromeDetect(string):
    """Determines if a string is a valid palindrome using stringReverse"""
    if string == stringReverse(string):
        return True
    else:
        return False





def stringReverse(string):
    """Returns a string in reverse order"""
    alter = ""
    for x in string:
        alter = x + alter
    return alter

print(palindromeDetect("doggod"))
print(palindromeDetect("dog"))