# Write a program called alice_words.py that creates a text file named alice_words.txt
# containing an alphabetical listing of all the words, and the number of times each occurs,
# in the text version of Alice’s Adventures in Wonderland.

import re

def aliceCount(filepath):
    """Takes a filepath to a .txt file and prints a sorted table of every word and its
    number of occurrences"""

    infile = open(str(filepath) , "r" , encoding="utf-8")
    ## this was initially throwing errors at around the 800th character, testing smaller
    ## chunks worked, so i looked up the error specifically and learned that the encoding
    ## of the file being opened must be specified, or else it might not read the file
    ## correctly. adding the encoding parameter fixed this. i couldn't find a specific
    ## listing of when to specify it, and open()'s documentation is vague in the vsc
    ## tooltip, but when i had it the wrong way around it threw an error, so it wasn't
    ## hard to tell i needed to resort it to the correct way.

    table = {}
    regex = re.compile('[^a-zA-Z]')
    # regex defined outside loop to prevent pointless reassigning every loop

    line = infile.readline()
    while line:
        contents = line.split()

        ## let's try regex here to strip out all non alphabetic characters
        #regex = re.compile('[^a-zA-Z]')
        for word in contents:
            regex.sub('', word)
        ## this should identify anything that isn't upper/lowercase letters and
        ## remove them, returning the filtered result.
        ## i like the idea of playing with regex here to experiment rather than the
        ## clunky one-by-one replaces the book's answer uses to convert every
        ## bit of punctuation into blanks. i get why the book doesn't just throw
        ## regex in randomly, of course.
            word = word.lower()
            if word.isalpha():
                if word in table:
                    table[word] += 1
                else:
                    table[word] = 1

        line = infile.readline()
        ## is it the right take to read the file line by line like this? is it faster to apply
        ## the loop per line like this, or should i be reading the entire file at once and
        ## applying the loop to the whole thing? the latter sounds inefficient, but isn't the 
        ## former basically the same thing? does this matter? i don't know.
    
    print("Word\t\t\tCount")

    for x in sorted(table):
        if len(x) > 12:
            tab = "\t"
            #### turns out the longest word is longer than 12. another loop makes the table
            #### print cleanly based on this dataset.
        elif len(x) >= 8 and len(x) <= 12:
            tab = "\t\t"
        else:
            tab = "\t\t\t"
            ### this aligns the table up to what's visible in my terminal. if any word
            ### in the text exceeds 15 characters then another loop would be necessary.
            ### a more elegant solution might be able to adjust this on the fly, but
            ### i'm working with what i know here.
        print(x + tab + str(table[x]))
        ## the tabbing in the print result is a little weird. i need to create a loop to check
        ## word length to determine the number of tabs needed
    
    keylist = list(table.keys())
    print(max(keylist , key=len))
    ### This returns the longest word in the dictionary, after creating a list out of the keys
    ### in the dictionary to reference. i learned here that you can define a key= argument
    ### to tell max what to count based on, which solved my problem of figuring out how to
    ### apply max without just iterating over the entire list and comparing each word to an
    ### accumulator.


    infile.close()

aliceCount("alice.txt")

## regex worked, and i understand why! that's pretty rad!