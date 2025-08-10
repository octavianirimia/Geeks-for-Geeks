"""
Given two integer arrays a[] and b[] containing two integers each representing the numerator and denominator of a fraction respectively.
The task is to find the sum of the two fractions and return the numerator and denominator of the result.

Algorithm to Add Two Fractions: 

1. Find a common denominator by finding the LCM (Least Common Multiple) of the two denominators.
2. Change the fractions to have the same denominator and add both terms.
3. Reduce the final fraction obtained into its simpler form by dividing both the numerator and denominator by their largest common factor.
"""

def gcd(a: int, b: int) -> int:
    return a if not b else gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def add_fraction(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    """Add two fractions"""

    den = lcm(a[1], b[1])

    num = a[0] * den // a[1] + b[0] * den // b[1]

    common_factor = gcd(num, den)

    den //= common_factor
    num //= common_factor

    return (num, den)


if __name__ == "__main__":
    print(add_fraction((1, 2), (3, 2)))
    print(add_fraction((1, 3), (3, 9)))
    print(add_fraction((1, 5), (3, 15)))
