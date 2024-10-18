#!/usr/bin/env python3
"""
Project Title: Safe First Element Extractor
Description: This project provides a function to safely extract the first
element from a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function returns the first element of a given sequence if it exists,
    otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence (e.g., list, tuple) that contains elements
    of any type.

    Returns:
    Union[Any, None]: The first element of the sequence if the sequence
    is not empty; otherwise, None.
    """
    if lst:
        return lst[0]
    else:
        return None
