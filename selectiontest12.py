# 3 criteria must be taken into account to identify leap years:

# The year is evenly divisible by 4;

# If the year can be evenly divided by 100, it is NOT a leap year, unless;

# The year is also evenly divisible by 400. Then it is a leap year.

# Write a function that takes a year as a parameter and returns True if the year
# is a leap year, False otherwise.

def leapCheck(n):
    """Determines whether year n is a leap year and returns a boolean"""

    if n % 4 == 0 and (n % 100 != 0 or n % 400):
        return True
    else:
        return False

def main():
    year = input("Please input the current year: ")

    if leapCheck(int(year)) == True:
        print(year , "is a leap year.")
    else:
        print(year , "is NOT a leap year.")

main()