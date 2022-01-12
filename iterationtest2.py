# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
# A call to print_triangular_numbers(5) would produce the following output:

# Tn = n(n+1) / 2

def print_triangular_numbers(n):
    for x in range(1 , n+1):
        x = int(x)
        trinum = (x * (x + 1) / 2)
        print(x , "\t" , int(trinum))

print_triangular_numbers(5)