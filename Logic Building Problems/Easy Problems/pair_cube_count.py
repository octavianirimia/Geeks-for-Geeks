def count_pairs(number: int) -> int:
    count = 0
    for i in range(1, int(number ** (1/3)) + 1):
        cb = i ** 3

        diff = number - cb

        cbrt_diff = round(diff ** (1/3))

        if cbrt_diff ** 3 == diff:
            count +=1
            print(i, cbrt_diff)
    print(count)


if __name__ == "__main__":
    count_pairs(9)