# Modify this code so it prints each subtotal, the total cost, and average 
# price to exactly two decimal places.


def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            ## note: cannot format inside of a print call, so a separate variable must be made that is
            ## printed instead
            print('Subtotal: ${:.2f}'.format(total))
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()
