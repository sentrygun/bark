# Write a function that removes the first occurrence of a string from another string.

def removeFirst(string , substring):
    """Replaces the first instance of substring from string with a blank"""
    return string.replace(substring , "" , 1)
    # This might be overcompact, but I'd just be defining one variable and then returning it anyways.
    #return string

# I initially planned on finding the index values of the first instance and its endpoint
# and using a slice to select only that part and then replace it with a blank, then return
# the altered string, but the replace function can already do this itself with an optional
# argument, so, why reinvent the wheel, especially if I'm using part of the wheel anyways?

print(removeFirst("bark bark meow" , "bark"))

# This has whitespace issues, but the input could just include the whitespace to prevent this issue.

# Write a function that removes all occurrences of a string from another string.
## This is just .replace without a third argument.
### The actual answer slices around the substring's starting and ending indexes and returns a
### value that doesn't include the sliced out portion. I assume doing this for all would just
### involve wrapping this with a while check that repeats this with new variables of the sliced
### out strings until find reports -1, then ending it, which is what I was planning to do from
### the start.