#!/usr/bin/env python3
""""
This module provides a function to return a tuple with a string and the square
of an int or float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string 'k', and the second
    element is the square of the value 'v', as a float.


    Args:
        k (str): A string.
        v (Union[int, float]): An integer or float whose square is be returned

    Returns:
         Tuple[str, float]: A tuple with the string 'k' and the square of 'v'

        Example:
        >>> to_kv("eggs", 3)
        ('eggs', 9.0)

        >>> to_kv("school", 0.02)
        ('school', 0.0004)
    """

    return (k, float(v ** 2))
