"""
Given a number n, find all prime numbers less than or equal to n.
"""

from math import sqrt

def sieve(number: int) -> list[int]:
    
    # Let's suppose all numbers ar primes
    primes = [True] * (number - 1)
    prime = 2

    while (squred_prime := prime * prime) <= number:
        if primes[prime - 2]:
            for i in range(squred_prime - 2, number - 1, prime):
                primes[i] = False

        prime += 1
    
    prime_numbers: list[int] = []

    for prime in range(number - 1):
        if primes[prime]:
            prime_numbers.append(prime + 2)
    
    return prime_numbers


if __name__ == "__main__":
    print(sieve(100))
