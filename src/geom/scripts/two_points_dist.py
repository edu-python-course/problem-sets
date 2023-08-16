# Distance between two points #91
# https://github.com/edu-python-course/problem-sets/issues/91
# pylint: disable=C0114

import math

if __name__ == "__main__":
    point_a = input("Enter 1st point coordinates (x, y): ")
    point_b = input("Enter 2nd point coordinates (x, y): ")

    xa, ya = map(float, point_a.replace(",", "").split())
    xb, yb = map(float, point_b.replace(",", "").split())

    print(f"{math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2) = }")
