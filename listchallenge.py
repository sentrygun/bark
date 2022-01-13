# Challenge For each word in words, add ‘d’ to the end of the word if the word ends in
# “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these
# past tense words to a list called past_tense.

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for item in words:
    if item[-1] == "e":
        # append "d" to end of word
        item += "d"
        past_tense += [item]
        # print(past_tense)
    else:
        # append "ed" to end of word
        item += "ed"
        past_tense += [item]
        

# add modified words to new list, print new list
print(words)
print(past_tense)