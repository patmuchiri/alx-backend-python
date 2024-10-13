#!/usr/bin/env python3

"""
Provides a function to compute the floor of a floating-point number.

It includes a function named 'floor' that takes a float as input and
returns the largest integer less than or equal to that float.
"""
import math


def floor(n: float) -> int:
    """
    Computes the floor of a given floating-point number.

    This function takes a float n and returns the largest integer
    less than or equal to n.

    Args:
        n (float): The floating-point number to be floored.

    Returns:
        int: The floor of the floating-point number n.

    Example:
        >>> floor(3.14)
        3
    """
    return math.floor(n)
