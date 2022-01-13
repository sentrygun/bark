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

# [<expression> for <item> in <sequence> if  <condition>]

def compPrime(n):
    """Return a list of primes below N"""
    primes = []
    compList = [primes.append(i) for i in range(0 , n) if is_prime(i)]
    return compList

def compPrime2(n):
    compList = [i for i in range(0 , n) if is_prime(i)]
    return compList

# these two don't seem to make a considerable difference from each other. variability in the
# run speed means this doesn't seem to complete the task any faster than the naive, which makes
# sense considering it's basically just a reformatted version of the naive.

# is the issue the range? the necessity in checking unnecessary numbers against isPrime?



start = time.time()
# centprime(1000)
# compPrime(1000)
compPrime2(1000)
base_time = time.time() - start

print("Base time:\t", base_time)
# print("My time:\t", my_time)
# print("Score:  \t", my_time / base_time)
