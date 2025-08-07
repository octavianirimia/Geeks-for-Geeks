"""
Expected Approach Without using Third Variable
The idea is to swap two numbers using Arithmetic operators or Bitwise operators.
"""

if __name__ == "__main__":
    a: int = 2
    b: int = 3
    print(f"{a=}; {b=}")

    a, b = b, a

    print(f"{a=}; {b=}")
