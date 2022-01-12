# Implement the calculator for the date of Easter.

# The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.

# Ask the user to enter a year. Compute the following:

#         a = year % 19

#         b = year % 4

#         c = year % 7

#         d = (19 * a + 24) % 30

#         e = (2 * b + 4 * c + 6 * d + 5) % 7

#         dateofeaster = 22 + d + e

# Special note: The algorithm can give a date in April. Also, if the year is one of four special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.

# Your program should print an error message if the user provides a date that is out of range.

def easterCheck(year):
    """Takes user input of year and returns the date of that year's Easter Sunday"""

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    dateofeaster = 22 + d + e

    if year == [1954, 1981, 2049, 2076]:
        dateofeaster = dateofeaster - 7

    return dateofeaster

def main():
    year = input("Please input a year to check the date of that year's Easter Sunday (within April): ")
    day = easterCheck(int(year))
    if day > 31:
        month = "April"
        day = int(day) - 31
    else:
        month = "March"
    day = str(day)


    print("Easter Sunday in" , year , "falls on", month , day + ".")

main()