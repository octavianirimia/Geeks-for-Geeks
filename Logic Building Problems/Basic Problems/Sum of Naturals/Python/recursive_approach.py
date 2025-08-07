"""
Using Recursion - O(n) and O(n) Space
In this approach, we use recursion to find the sum of the first n natural numbers. The function calls itself with (n-1) until it reaches the base case of n = 1.
Each call adds the current value of n to the sum of smaller values, effectively building the result in a top-down manner. 
"""

def sum_of_integers(number: int) -> int:
    """Sum the first n numbers recursively"""

    if number == 1:
        return 1
    
    return number + sum_of_integers(number - 1)


if __name__ == "__main__":
    number: int = 3
    print(sum_of_integers(number))
