"""
a x b = LCM(a, b) * GCD (a, b)

LCM(a, b) = (a x b) / GCD(a, b)

Time Complexity: O(min(a,b))
Auxiliary Space: O(1)
"""

def gcd(a: int, b: int) -> int:
    return a if not b else gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


if __name__ == "__main__":
    print(lcm(5, 10))
