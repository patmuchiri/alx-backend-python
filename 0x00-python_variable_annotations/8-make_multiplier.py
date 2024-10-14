#!/usr/bin/env python3

"""
This module provides a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the productof the float and the multiplier.

    Example:
        >>> fun = make_multiplier(2.22)
        >>> fun(2.22)
        4.928400000000001
    """
    return lambda x: x * multiplier
