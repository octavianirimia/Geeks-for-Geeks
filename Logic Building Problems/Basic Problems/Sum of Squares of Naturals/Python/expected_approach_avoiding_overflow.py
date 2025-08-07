"""
In the exxpected approach method, sometimes due to large value of n, the value of (n * (n + 1) * (2 * n + 1)) would overflow.
We can avoid this overflow up to some extent using the fact that n*(n+1) must be divisible by 2 and restructuring the formula as (n * (n + 1) / 2) * (2 * n + 1) / 3;
"""

def sum_of_squares(number: int) -> int:
    """Return the sum of the squared numbers from 1 to n"""
    return (number * (number + 1)) // 2 * (2 * number + 1) // 3


if __name__ == "__main__":
    number: int = 3
    print(sum_of_squares(number))
