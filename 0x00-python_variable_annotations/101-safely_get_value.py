from typing import Mapping, TypeVar, Any, Union

# Define a type variable that can be any type
T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
) -> Union[T, None]:
    """
    Safely retrieve a value from a dictionary.

    Parameters:
    dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
    key (Any): The key whose value needs to be retrieved.
    default (Union[T, None]): The default value to return if the key is not
    found.

    Returns:
    Union[T, None]: The value associated with the key if found,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
