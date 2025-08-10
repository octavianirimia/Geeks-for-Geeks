def sum_of_digits(number: int) -> int:
    """Return the sum of digits of a number"""
    s: int = 0

    while number:
        s += number 
