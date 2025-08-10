from math import sqrt


def is_prime(number: int) -> bool:
    if number == 2 or number == 3:
        return True
    
    if number <= 1 or number % 2 == 0 or number %  3 == 0:
        return False
    
    for i in range (5, int(sqrt(number)) + 1, 6):
        if number % i == 0 or (number + 2) % i == 0:
            return False
    
    return True


def _3_divisors_numbers(number: int) -> None:

    i: int = 2

    while i ** 2 <= number:
        if is_prime(i):
            print(i ** 2)
        
        i += 1


if __name__ == "__main__":
    n = 12209

    print(_3_divisors_numbers(n))
