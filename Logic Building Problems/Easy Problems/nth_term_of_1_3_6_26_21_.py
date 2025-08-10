"""
The pattern in this series is nth term is equal to sum of (n-1)th term and n.

n = 2
2nd term equals to sum of 1st term and 2 i.e
A2 = A1 + 2 = 1 + 2 = 3
Similarly,
A3 = A2 + 3 = 3 + 3 = 6 and so on..
We get: 

A(n) = A(n - 1) + n 
     = A(n - 2) + n + (n - 1)
     = A(n - 3) + n + (n - 1) + (n - 2) 
       .
       .
       .
     = A(1) + 2 + 3... + (n-1) + n

A(n) = 1 + 2 + 3 + 4... + (n - 1) + n = n(n + 1) / 2
i.e A(n) is sum of First n natural numbers.
"""

def nth_term(n: int) -> int:
    return n // 2 * (n + 1)

if __name__ == "__main__":
    print(nth_term(4))
