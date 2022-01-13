# This solution works by iterating over all of the scores in the list except the last,
# and dealing with that one separately.

scores = [85, 95, 70]
result = ''
for score in scores[:-1]:
   result = result + str(score) + ', '

# Now, append the last score
result = result + 'and ' + str(scores[-1]) + '.'

print("The scores are " + result)


## This feels like a useful example of using slices to manipulate how much of a list you're controlling
## I went into this problem wanting to use the index value of score within scores to determine if
## it's the end or not, but given the dataset could have duplicates this would cause issues using the
## index method since it would just stop at the first instance of the same value.

## There's probably a good way to pull the current index of the position that a for loop is in, that
## could be checked to determine when you're at the end of the list?

### range(len(list)) can give a range of integers based on the length of the list, this could be used
### to effectively reference index positions of the list within a for statement, which is probably
### what I was looking for here, rather than the slicing method used by the book's answer above.
### example:
###     for position in range(len(aList)):
###        aList[position] = 2 * aList[position]