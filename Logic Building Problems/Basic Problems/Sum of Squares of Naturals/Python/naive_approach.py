"""
Naive Approach - Adding One By One - O(n) Time and O(1) Space
The idea for this naive approach is to run a loop from 1 to n and sum up all the squares.
"""

def sum_of_squares(number: int) -> int:
    """Return the sum of the squared numbers from 1 to n"""
    return sum([i ** 2 for i in range(1, number + 1)])


if __name__ == "__main__":
    number: int = 2
    print(sum_of_squares(number))
