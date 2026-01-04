#!/usr/bin/python3
"""mi"""


def pascal_triangle(n):
    """hm"""

    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        last = triangle[-1]
        left = [0] + last
        right = last + [0]

        new_row = []
        i = 0
        while i < len(left):
            new_row.append(left[i] + right[i])
            i += 1

        triangle.append(new_row)

    return triangle
