"""
In this method, we pass i as an additional parameter with initial value as 1. We print n * i and then recursively call for i+1.
We stop the recursion when i becomes 11 as we need to print only 10 multiples of given number and i.
"""

def print_multiplication_table_recursive(number: int, i: int) -> None:
    """Print the multiplication table recursively"""

    if i == 11:
        return

    print(f"{number} x {i} = {number * i}")

    print_multiplication_table_recursive(number, i + 1)


if __name__ == "__main__":
    number: int = 5
    print_multiplication_table_recursive(5, 1)
