"""
Naive Approach Using Third Variable
The idea is to use a third variable, say temp to store the original value of one of the variables during the swap.

Store the value of a in temp.
Assign the value of b to a.
Assign the value of temp to b.
"""

if __name__ == "__main__":
    a: int = 2
    b: int = 3
    print(f"{a=}; {b=}")

    temp: int = a
    a: int = b
    b: int = temp

    print(f"{a=}; {b=}")
