def prime_factor(number: int) -> list[int]:

    factors = set()

    divisor = 2

    # Check for 2
    while number % divisor == 0:
        factors.add(divisor)
        number //= divisor
    
    divisor += 1

    while divisor ** 2 <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        
        divisor += 2
    
    if number > 1:
        factors.add(number)
    
    return sorted(factors)


if __name__ == "__main__":
    print(prime_factor(60))
