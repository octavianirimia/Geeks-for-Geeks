"""
Iterative Checking - O(m) Time and O(1) Space
The basic idea is to start checking from n - m to n + m one by one and take the closest number.
"""

def closest_number(n: int, m: int) -> int:

    minimum_differnce = float("inf")
    closest = 0

    for i in range(n - abs(m), n + abs(m) + 1):
        if not i % m:
            difference = abs(n - i)

            if difference < minimum_differnce or (difference == minimum_differnce and abs(i) > abs(closest)):
                closest = i
                minimum_differnce = difference
    
    return closest


if __name__ == "__main__":
    n: int = -15
    m: int = 6

    print(closest_number(n, m))
