"""
An efficient Solution is to go through numbers till square root of n. If a number 'i' divides n, then add both 'i' and 'n/i' .

Time Complexity: O(sqrt n)
Space Complexity: O(1)

How it works?

number = 6
sum = 1

The for loop is from 2 to 3 (not inclusive)

6 % 2 == 0 and 2 ** 2 != 6 => sum = 1 + 2 + 3

sum == number and number != 1 so the number is perfect
"""

from math import sqrt


def is_perfect(number: int) -> bool:

    sum: int = 1

    for i in range(2, int(sqrt(number)) + 1):
        if not number % i:
            if i ** 2 != number:
                sum += i + number // i
            else:
                sum += i
        print(sum)
    
    return sum == number and number != 1


if __name__ == "__main__":
    print(is_perfect(15))
    print(is_perfect(6))
