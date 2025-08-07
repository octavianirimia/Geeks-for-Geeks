"""
To find the nth term in the Arithmetic Progression series we use the simple formula.

We know the Arithmetic Progression series is like =  2, 3, 4, 5, 6. …. …
In this series 2 is the first term and 3 is the second term of the series.
Common difference = a2 - a1 =  3 – 2 = 1 (Difference common in the series).
so we can write the series as :
t1 = a1
t2 = a1 + (2-1) * d
t3 = a1 + (3-1) * d
.
.
.
tN = a1 + (n-1) * d

tN = a1 + (n-1) * (a2-a1)
"""

def nth_term_of_ap(a1: int, a2: int, n: int) -> int:
    """Return the nth term of the ap"""
    return a1 + (n - 1) * (a2 - a1)


if __name__ == "__main__":
    a1: int = 2
    a2: int = 3
    n: int = 4

    print(nth_term_of_ap(a1, a2, n))
