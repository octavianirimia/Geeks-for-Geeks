"""
Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively, the problem is to find the nth term of the series. 
Examples :

Input : a1 = 2,  a2 = 3,  n = 4
Output : 5
Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. 

Input : a1 = 1, a2 = 3, n = 10
Output : 19
Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.
"""

def nth_term_of_ap(a1: int, a2: int, n: int) -> int:
    """Return the nth term of the ap"""
    ratio: int = a2 - a1

    nth_term: int = a1

    for _ in range(1, n):
        nth_term += ratio
    
    return nth_term


if __name__ == "__main__":
    a1: int = 2
    a2: int = 3
    n: int = 4

    print(nth_term_of_ap(a1, a2, n))
