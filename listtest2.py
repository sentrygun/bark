# Create a list called myList with the following six items:
# 76, 92.3, “hello”, True, 4, 76.
# Begin with the empty list shown below, and add 6 statements to add each item, one per item. 
# The first three statements should use the append method to append the item to the list,
# and the last three statements should use concatenation.

# myList = [76 , 92.3 , "hello" , True , 4 , 76]

myList = []

myList.append(76)
myList.append(92.3)
myList.append("hello")

myList += [True]
myList += [4]
myList += [76]

# print(myList)

# Starting with the list of the previous exercise, write Python statements to do the following:

#     Append “apple” and 76 to the list.
#     Insert the value “cat” at position 3.
#     Insert the value 99 at the start of the list.
#     Find the index of “hello”.
#     Count the number of 76s in the list.
#     Remove the first occurrence of 76 from the list.
#     Remove True from the list using pop and index.

myList.append("apple")
myList.append(76)
myList.insert(3 , "cat")
myList.insert(0 , 99)
#myList.index("hello")
#myList.count(76)
myList.remove(76)
myList.pop(myList.index(True))
print(myList)