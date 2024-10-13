#!/usr/bin/env python3

"""
This module provides a function to convert a floating-point number
to its string representation.

It includes a function named 'to_str' that takes a float as input
and returns the string representation of that float.
"""


def to_str(n: float) -> str:
    """
    Converts a floating-point number to its string representation.

    This function takes a float n and returns a string that represents
    the float.

    Args:
        n (float): The floating-point number to convert.

    Returns:
        str: The string representation of the float n.

    Example:
        >>> to_str(3.14)
        '3.14'
    """
    return str(n)
