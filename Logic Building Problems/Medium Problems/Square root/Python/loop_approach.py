def floor_sqrt(number: int):

    result: int = 1

    while result ** 2 <= number:
        result += 1
    
    return result - 1


if __name__ == "__main__":
    print(floor_sqrt(10453))