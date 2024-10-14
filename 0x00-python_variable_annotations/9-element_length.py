#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple

"""
This module contains a function to compute the lengths of elements
in an iterable of sequences.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from the input
    iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (like strings,
        lists, or tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence and its length.

    Example:
        >>> element_length(["abc", "de", "f"])
        [('abc', 3), ('de', 2), ('f', 1)]
    """
    return [(i, len(i)) for i in lst]
