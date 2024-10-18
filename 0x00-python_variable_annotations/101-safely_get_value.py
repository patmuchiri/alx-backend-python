#!/usr/bin/env python3

from typing import Mapping, TypeVar, Any, Union

# Define a generic type variable 'T'
T = TypeVar('T')

def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on the key, with a fallback to a default value.

    Parameters:
    ----------
    dct : Mapping
        The dictionary containing keys and values. The keys can be of any type, and the values are of type 'T'.
    
    key : Any
        The key used to retrieve the value from the dictionary.
    
    default : Union[T, None], optional
        The default value to return if the key does not exist in the dictionary. Defaults to None.

    Returns:
    -------
    Union[Any, T]
        The value from the dictionary corresponding to the given key, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
