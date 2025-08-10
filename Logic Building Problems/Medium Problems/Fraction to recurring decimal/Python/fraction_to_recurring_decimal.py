"""
Given two integers a and b(b != 0), the task is to return the fraction a/b in string format. If the fractional part is repeating, enclose the repeating part in parentheses.

Examples: 

Input: a = 1, b = 2
Output: "0.5"
Explanation: 1/2 = 0.5 with no repeating part.

Input: a = 50, b = 22
Output: "2.(27)"
Explanation: 50/22 = 2.27272727... Since fractional part (27) is repeating, it is enclosed in parentheses.

Approach:
The idea is to first calculate the integral quotient (absolute part before decimal point) and then calculate the fractional part.
To check if the fractional part is repeating, insert the remainder (a % b) in a hash map with key as remainder and value as the index position at which this remainder occurs.
If at any point of time, the remainder becomes zero, then there doesn't exist a repeating fraction otherwise if the remainder is already found in the map, then there exists a repeating fraction.
"""


def fraction_to_recurring_decimal(a: int, b: int) -> str:
    if a == 0:
        return '0'

    result: str = '-' if a < 0 or b < 0 else ''

    a, b = abs(a), abs(b)

    result += str(a // b)

    remainder: float = a % b

    if not remainder:
        return result
    
    result += '.'
    seen = {}

    while remainder > 0:
        if remainder in seen:
            result = result[:seen[remainder]] + "(" + result[seen[remainder]:] + ")"
            break
            
        seen[remainder] = len(result)

        remainder *= 10

        result += str(remainder // b)

        remainder = remainder % b

    return result


if __name__ == "__main__":
    a: int = 50
    b: int = 22

    print(fraction_to_recurring_decimal(a, b))
