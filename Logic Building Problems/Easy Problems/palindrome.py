def palindrome(number: int) -> int:

    result = 0
    number_copy = number

    while number_copy:
        result = result * 10 + number_copy % 10

        number_copy //= 10
    
    return number == result


if __name__ == "__main__":
    print(palindrome(1234321))
