"""
Calculate the distance between two points.
"""

from math import sqrt

def distance(point_one: tuple[int, int], point_two: tuple[int, int]) -> float:
    return sqrt((point_two[0] - point_one[0]) ** 2 + (point_two[1] - point_one[1]) ** 2)

if __name__ == "__main__":
    point_one: tuple[int, int] = (3, 4)
    point_two: tuple[int, int] = (4, 3)

    print(distance(point_one, point_two))
