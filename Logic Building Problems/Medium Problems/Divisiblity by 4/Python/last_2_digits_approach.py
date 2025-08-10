def is_divisible_by_4(number: int) -> bool:
    if not number:
        return False
    
    if number <= 9:
        return number % 4 == 0
    
    last_2_digits = int(str(number)[-2:])

    return last_2_digits % 4 == 0


if __name__ == "__main__":
    print(is_divisible_by_4(76952))
