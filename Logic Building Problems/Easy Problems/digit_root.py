"""
The digital root of a positive integer is found by summing the digits of the integer.
If the resulting value is a single digit then that digit is the digital root.
If the resulting value contains two or more digits, those digits are summed and the process is repeated.
This is continued as long as necessary to obtain a single digit.
Given a number, the task is to find its digital root.
The input number may be large and it may not be possible to store even if we use long long int.
"""

def digital_root(number: int) -> int:
    if number == 0:
        return 0
    
    if number % 9 == 0:
        return 9
    
    return number % 9


if __name__ == "__main__":
    print(digital_root(5739))
