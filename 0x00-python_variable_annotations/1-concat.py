#!/usr/bin/env python3

"""
This module provides a function to perform basic arithmetic operations.
Specifically, it includes a function to add two floating-point numbers
and return their sum.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    This function takes two string arguments, combines them into one
    single string by joining them, and returns the concatenated string.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string formed by joining str1 and str2.

    Example:
        >>> concat("hello", "world")
        'helloworld'
    """
    return str1 + str2
