"""
Digit Extraction - O(log10n) Time and O(1) Space
We can sum the digits of a number by repeatedly extracting the last digit using n % 10, adding it to the sum, and then removing it by dividing n by 10 using integer division.
"""

def sum_of_digits(number: int) -> int:
    
