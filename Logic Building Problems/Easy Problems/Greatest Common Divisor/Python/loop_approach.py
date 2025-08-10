"""
The idea is to find the minimum of the two numbers and find its highest factor which is also a factor of the other number.

Time Complexity: O(min(a, b))
Space Complexity: O(1)
"""

from math import gcd

def greatest_common_divisor(a: int, b: int) -> int:
    gcd = min(a, b)

    while gcd > 0:
        if not a % gcd and not b % gcd:
            break
        gcd -= 1
    
    return gcd

if __name__ == "__main__":
    print(greatest_common_divisor(20, 28))
