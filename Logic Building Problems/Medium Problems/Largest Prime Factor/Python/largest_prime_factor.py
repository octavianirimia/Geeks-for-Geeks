"""
Given a positive integer n ( 1 <= n <= 1015). Find the largest prime factor of a number.
"""

from math import sqrt


def largest_prime_factor(number: int) -> int:

    maximum_prime = -1

    # Check for 2 factoring
    while not number % 2:
        number //= 2
        maximum_prime = 2
    
    # Check for 3 factoring
    while not number % 3:
        number //= 3
        maximum_prime = 3
    
    # Now we check for the number of the form 6k +- 1 until the sqrt(number)
    for i in range(5, int(sqrt(number)) + 1, 6):
        print(number, i)
        while not number % i:
            number //= i
            maximum_prime = i
        
        while not number % (i + 2):
            number //= (i + 2)
            maximum_prime = (i + 2)
    
    if number >= 4:
        maximum_prime = number
    
    return maximum_prime
    

if __name__ == "__main__":
    print(largest_prime_factor(15))
