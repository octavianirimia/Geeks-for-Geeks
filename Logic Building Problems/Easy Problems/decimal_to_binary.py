def dec2bin(n: int) -> str:
    bin = ''
    while n > 0:
        bit = n & 1
        bin += str(bit)

        n = n >> 1
    
    return bin[::-1]

print(dec2bin(10))
