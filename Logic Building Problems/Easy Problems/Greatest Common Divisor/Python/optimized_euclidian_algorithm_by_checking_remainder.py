"""
Instead of the Euclidean algorithm by subtraction, a better approach can be used.
We don't perform subtraction here. we continuously divide the bigger number by the smaller number.

Time Complexity: O(log(min(a,b)))




How it works?
a = 20; b = 28
b is not 0

a = 28; b = 8
b is not 0

a = 8; b = 4
b is not 0

a = 4; b = 0
b is 0 so the greatest common divisor is 4
"""


def greatest_common_divisor(a: int, b : int) -> int:
    return a if not b else greatest_common_divisor(b, a % b)


if __name__ == "__main__":
    print(greatest_common_divisor(20, 28))
