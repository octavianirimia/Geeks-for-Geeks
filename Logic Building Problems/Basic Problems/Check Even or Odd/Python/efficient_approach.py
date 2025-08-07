"""
[Efficient Approach] Using Bitwise AND Operator - O(1) Time and O(1) Space
The last bit of all odd numbers is always 1, while for even numbers it’s 0. So, when performing bitwise AND operation with 1, odd numbers give 1, and even numbers give 0.
"""

def  is_even(number: int) -> bool:
    """Return True if the number is even else False"""
    return (number & 1) == 0


if __name__ == "__main__":
    n: int = 15

    print("true" if is_even(n) else "false")
