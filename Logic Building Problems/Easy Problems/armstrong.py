"""
Given a number x, determine whether the given number is Armstrong's number or not.
A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

Here a, b, c and d are digits of input number abcd.....

Examples

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153

Input: n = 9474
Output: true
Explanation: 9**4 + 4**4 + 7**4 + 4**4 = 6561 + 256 + 2401 + 256 = 9474

Input: n = 123
Output: false
Explanation: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36
"""

def armstrong(number: int) -> bool:
    string_number = str(number)
    digits = len(string_number)

    result = 0

    for digit in string_number:
        result += int(digit) ** digits
    
    return number == result


if __name__ == "__main__":
    print(armstrong(153))
