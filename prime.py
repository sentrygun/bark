import fractions, math
import time

def is_prime(n):
    """Returns true if n is prime, false otherwise."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def centprime(n): # the naive implementation
    """Return a list of primes below N"""
    primes = []
    for i in range(0, n):
        if is_prime(i):
            primes.append(i)
    return primes



start = time.time()
centprime(1000)
base_time = time.time() - start

print("Base time:\t", base_time)
# print("My time:\t", my_time)
# print("Score:  \t", my_time / base_time)
