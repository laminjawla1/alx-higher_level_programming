#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """ "Generate a pascal triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        current = [1]
        if i > 0:
            prev = triangle[i - 1]
        for j in range(1, i):
            current.append(prev[j - 1] + prev[j])
        if i > 0:
            current.append(1)
        triangle.append(current)
    return triangle
