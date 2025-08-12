"""
Given a positive integer n, find all the distinct divisors of n.
"""

from math import sqrt


def find_divisors(number: int) -> list[int]:

    divisors = set()

    for i in range(1, int(sqrt(number)) + 1):
        if not number % i:
            divisors.add(i)
            divisors.add(number // i)
    
    return sorted(divisors)


if __name__ == "__main__":
    print(find_divisors(36))
