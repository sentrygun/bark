def getGrade(grade):
    if grade >= 90 and grade <= 100:
        return("A")
    elif grade >= 80 and grade < 90:
        return("B")
    elif grade >= 70 and grade < 80:
        return("C")
    elif grade >= 60 and grade < 70:
        return("D")
    elif grade >= 1 and grade < 60:
        return("F")
    else:
        print("Error: Exam mark must be a number between 1-100")

def main():
    grade = input("Please enter an exam mark between 1-100 to determine grade: ")
    if int(grade) == int:
        print(getGrade(int(grade)))
    else:
        print("A valid integer must be input.")
        main()
# Overcomplication, but, not quite sure how to set things up so that the prompt correctly checks to see
# if the input is actually an integer before running the getGrade function.

main()