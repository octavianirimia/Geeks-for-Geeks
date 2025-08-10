def is_divisible_by_13(number: int) -> bool:
    n = abs(number)
    while n > 99:
        last_digit = n % 10
        n = n // 10 - 9 * last_digit
        n = abs(n)
    # Now n is at most 2 digits, check if it's 0 or 13 or 26 or ... 91
    return n in {0, 13, 26, 39, 52, 65, 78, 91}

if __name__ == "__main__":
    print(is_divisible_by_13(6159452))
