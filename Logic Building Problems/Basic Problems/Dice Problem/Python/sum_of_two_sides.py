"""
Using Sum of Two Sides
The idea is based on the observation that the sum of two opposite sides of a cubical dice is equal to 7. So, just subtract the given n from 7 and print the answer.
"""

def opposite_face_of_dice(n: int) -> int:
    """Get the opposite face of the dice"""
    return 7 - n


if __name__ == "__main__":
    n: int = 2
    print(f"The opposite face of {n} is {opposite_face_of_dice(n)}")

