"""
It is based on the fact that all primes greater than 3 are of the form 6k ± 1, where k is any integer greater than 0.
This is because all integers can be expressed as (6k + i), where i = -1, 0, 1, 2, 3, or 4.
And note that 2 divides (6k + 0), (6k + 2), and (6k + 4) and 3 divides (6k + 3).
So, a more efficient method is to test whether n is divisible by 2 or 3, then to check through all numbers of the form 6k ± 1 <= √n.
This is 3 times faster than testing all numbers up to √n.
"""
from math import sqrt

def is_prime(number: int) -> bool:
    """Check if number is prime"""
    if number == 2 or number == 3:
        return True
    
    if number <= 1 or number % 2 == 0 or number % 3 == 0:
        return False
    
    for i in range(5, int(sqrt(number)) + 1, 6):
        if number % i == 0 or (number + 2) % i == 0:
            return False
    
    return True


if __name__ == "__main__":
    # Test cases
    test_numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 23, 29, 31, 37, 41]
    for num in test_numbers:
        print(f"{num} is prime: {is_prime(num)}")
