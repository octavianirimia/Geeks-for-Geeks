"""
Using Binary Search

The square of a number increases as the number increases, so the square root of n must lie in a sorted (monotonic) range.
If a number's square is more than n, the square root must be smaller.
If it's less than or equal to n, the square root could be that number or greater.
Because of this pattern, we can apply binary search in the range 1 to n to efficiently find the square root.

Time Complexity: O(log(n))
Space Complexity: O(1)
"""

def floor_sqrt(number: int) -> int:

    low: int = 0
    high: int = number
    result: int = 1

    while low <= high:
        middle = low + (high - low) // 2

        if middle * middle <= number:
            result = middle
            low = middle + 1
        else:
            high = middle - 1

    return result


if __name__ == "__main__":
    print(floor_sqrt(10453))
