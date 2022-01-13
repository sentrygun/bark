# import test

# print("hello world")
#  and it's all mirrored

#  and it's all mirrored

# ctrl / - comment line
# ctrl d - select/selectall/mirror cursor
# alt shift click - select at parity with character length

scores = [85, 95, 70]
result = ''
for score in scores:
    # if len(scores) == 1:
    #     step = scores.pop(0)
    #     result += "and " + str(step) + "."
    # else:
        step = scores.pop(0)
        print(scores)
        result += str(step) + ", "

print("The scores are " + result)

# print(type(len(scores)))