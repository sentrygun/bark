# Write a function, is_prime, that takes a single integer argument and returns True
# when the argument is a prime number and False otherwise.

#  trial division, tests whether n is a multiple of any integer between 2 and (sqrt)n

def is_prime(n):
    for i in range(2 , n):
        if n % i == 0:
            return False
        else:
            return True

# hitched up on figuring out how to mathematically, and simply, solve for primes.
# shell of code aspect was accurate, though.

print(is_prime(6))