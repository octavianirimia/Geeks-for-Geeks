"""
Sum of first n natural numbers = (n * (n+1)) / 2

For example: n = 5
Sum = (5 * (5 + 1)) / 2 = (5 * 6) / 2 = 30 / 2 = 15

How does this work?

We can prove this formula using induction.
It is true for n = 1 and n = 2
For n = 1, sum = 1 * (1 + 1)/2 = 1
For n = 4, sum = 4* (4 + 1)/2 = 10
Let it be true for k = n-1.
Sum of k numbers = (k * (k+1))/2
Putting k = n-1, we get
Sum of k numbers = ((n-1) * (n-1+1))/2
                 = (n - 1) * n / 2
If we add n, we get,
Sum of n numbers = n + (n - 1) * n / 2
                 = (2n + n2 - n)/2
                 = n * (n + 1)/2
"""

def sum_of_natural_numbers(n: int):
    """Return the sum of the first n natural numbers"""
    return n * (n + 1) // 2


if __name__ == "__main__":
    number: int = 3
    print(sum_of_natural_numbers(number))
