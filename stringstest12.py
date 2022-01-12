# Write a function that implements a substitution cipher.

import string

def cipher(input):
    """Scrambles string input by a set substitution cipher"""
    input = input.upper()
    substitute = "RBJIYOAWFHQXVZEDKPSTUMNCGL"
    result = ""
    alpha = string.ascii_uppercase
    

    for x in input:
        # newchar = x.replace(string.ascii_uppercase.index(x) , substitute.index(x))
        # result = result + newchar             ## wrong line of thinking

        #letter = input[x]      # i completely forgot 'for x in input' would give me the letter
                                # rather than the index value and kept trying the wrong things.
        baseIndex = alpha.index(x)
        subChar = substitute[baseIndex]
        result = result + subChar

    return result


def revCipher(input):
    """Unscrambles string input by set substitution cipher, reversing function cipher"""
    input = input.upper()
    substitute = "RBJIYOAWFHQXVZEDKPSTUMNCGL"
    result = ""
    alpha = string.ascii_uppercase

    for x in input:
        scramIndex = substitute.index(x)
        subChar = alpha[scramIndex]
        result = result + subChar
        
    return result

# accounted for issues of upper/lowercasing by paving over the input to make it fully uppercase 
# (accounting for lowercase would just require the cipher to be doubled), but forgot to account
# for spaces.    
        
print(cipher("dddggetnkihs"))
print(revCipher("IIIAAYTZQFWS"))

# string.ascii_uppercase