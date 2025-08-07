"""
The iterative approach for printing a multiplication table involves using a loop to calculate and print the product of a given number and the numbers in range from 1 to 10.
In this method, you begin with the number whose table you want to print and use a loop to multiply it with increasing values.
"""

def print_multiplication_table(number: int) -> None:
    """Print the multiplication table of a number"""

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


if __name__ == "__main__":
    number: int = 5
    print_multiplication_table(number)
