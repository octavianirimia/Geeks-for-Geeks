def factorial(number: int) -> bool:
    result = 1

    for i in range(2, number + 1):
        result *= i
    
    return result


if __name__ == "__main__":
    number = 5
    print(factorial(number))
