#!/bin/python3
"""This script implements a function that finds the peak in a list"""
def find_peak(list_of_integers):
    """Finds the peak index in an array"""
    if len(list_of_integers) > 2:
        start = 0
        end = len(list_of_integers) - 1
        while start < end:
            middle = start + (end - start) // 2
            if list_of_integers[middle] > list_of_integers[middle + 1]:
                end = middle
            else:
                start = middle + 1
        return list_of_integers[start]
