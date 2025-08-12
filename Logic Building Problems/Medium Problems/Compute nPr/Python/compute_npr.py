"""
Given two numbers, n and r, the task is to compute nPr, which represents the number of ways to arrange r elements from a set of n elements.
It is calculated using the formula n!/(n−r)!, where "!" denotes the factorial operation.
"""

def factorial(number: int) -> int:
    result: int = 1

    for i in range(2, number + 1):
        result *= i
    
    return result


if __name__ == "__main__":

    n: int = 5
    r: int = 2

    print(factorial(n) // factorial(n - r))
