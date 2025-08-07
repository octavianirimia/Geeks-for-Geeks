"""
Using Loop - O(n) Time and O(1) Space
Calculate the sum of all integers from 1 to n by iterating through a loop.
"""

def sum_of_integers(number: int) -> int:
    """Find the sum of the first n numbers"""
    sum: int = 0;
    i: int = 0

    while i <= number:
        sum += i
        i += 1
    
    return sum


if __name__ == "__main__":
    number: int = 3
    print(sum_of_integers(number))
