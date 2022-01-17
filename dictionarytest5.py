# Write a function named translator that takes a parameter containing a sentence
# in English (no punctuation and all words in lowercase) and returns that sentence
# translated to Pirate.

def pirateTranslate(input):
    # first, fill a dictionary with the file containing all the pirate words
    piratedict = {}

    infile = open("piratedictionary.txt" , "r")
    line = infile.readline()
    while line:
        contents = line.split()
        piratedict[contents[0]] = contents[1:]
        line = infile.readline()

    #print(list[piratedict])
    infile.close()
    ## with the dictionary created from the source file, now an input can be accepted
    ## and morphed according to the dictionary

    inputlist = input.split()     # converts string to list of words that can be checked against

    # print(input)
    # print(inputlist)            # non-translated words aren't split as of this step

    output = []
    for word in inputlist:
        if word in piratedict:
            word = piratedict[word]
            output += word
        else:
            #output += word
            output += [word]
            ## if non-translated words are added to the accumulator as just word here,
            ## the result is a list composed of the contents of the string. if instead
            ## [word] is added to the accumulator, the result is the whole word.
            ##
            ## i suppose by adding a string to a list, i'm equating the string to being
            ## a list, which results in adding a list composed of each character in the
            ## string. if you want to concatenate lists, you need to add two lists.
            ## this works fine in the translated words, because those are already
            ## list objects.
            ##
            ## the book uses append to fill out the target list with words rather than
            ## concatenating them like i did. this makes sense and is probably the
            ## smarter way to do it, but stumbling into this problem, testing a weird
            ## idea, and then realizing why that worked was a good learning experience.

    # print(output)
    # ''.join(output)

    print(' '.join(output))


pirateTranslate("the lawyer is a galley")
# bark = "bark"