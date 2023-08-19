"""
Hello! This is a simple prime number generator.

The programs asks the user for two inputs, the starting number and the final number.
It will then list all the prime numbers from the starting upto the final number(inclusive)

"""

def is_prime(num): # Checks if a number is prime or not
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(start,end): # Checks the number of prime numbers in a range inputted by the user
    prime_nums = [num for num in range(start, end+1) if is_prime(num) == True]
    print_prime(prime_nums, start, end)
    
def print_prime(prime_nums, start, end): # Prints the prime numbers from 1 to n for the user to see
    print(f"\nHere are the prime numbers from {start} to {end}:")
    if prime_nums:
        for num in prime_nums:
            print(f"\t{num}")
    else:            
        print("\tNo prime numbers")
        if start > end:
            print("\t---Make sure that the starting number is less than the final number---")
    
print("\n=====PRIME NUMBER GENERATOR!=====")

while True:
    try:
        start = int(input("Starting number: "))
        end = int(input("Final number: "))        
    except ValueError:
        print("\n\tOnly use numbers!\n")
    else:
        break
    
generate_prime(start, end)