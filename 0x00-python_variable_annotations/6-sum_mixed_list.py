#!/usr/bin/env python3

"""
This module provides a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]):list containing integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.

    Example:
        >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
        679.13
    """
    return sum(mxd_lst)
