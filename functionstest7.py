# Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to
# and including n. So sumTo(10) would be 1+2+3...+10 which would return the value 55.
# Use the equation (n * (n + 1)) / 2.

def sumTo(n):
    """Returns sum of all integer numbers up to and including n."""
    result = (n * (n + 1)) / 2

    return int(result)

print(sumTo(10))

# This was just a simple test to make sure I remembered that fruitful function = return, but I thought it would require more,
# uh, problem solving?