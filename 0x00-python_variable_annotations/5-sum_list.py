#!/usr/bin/env python3

"""
This module contains a function to sum a list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the floating-point numbers in the input list.

    Example:
        >>> sum_list([3.14, 1.11, 2.22])
        6.470000000000001
    """
    return sum(input_list)
