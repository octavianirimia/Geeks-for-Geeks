def is_divisible_by_11(number: int) -> bool:

    even_digits_sum: int = 0
    odd_digits_sum: int = 0

    string_number: str = str(number)

    for i in range(len(string_number)):
        if i % 2 == 0:
            even_digits_sum += int(string_number[i])
        else:
            odd_digits_sum += int(string_number[i])
    
    return (even_digits_sum - odd_digits_sum) % 11 == 0


if __name__ == "__main__":
    print(is_divisible_by_11(76945))
