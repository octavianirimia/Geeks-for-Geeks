"""
Naive Approach] By Finding the Remainder - O(1) Time and O(1) Space
We can check the remainder when divided by 2. If the remainder is 0, the number is even, otherwise it is odd.
"""

def is_even(number: int) -> bool:
    """Return True if the number is even else False"""
    return number % 2 == 0


if __name__ == "__main__":
    n: int = 15

    print("true" if is_even(n) else "false")
