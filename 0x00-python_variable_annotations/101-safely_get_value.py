#!/usr/bin/env python3
"""
Given the parameters and the return values, add type
annotations to the function

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
       Returns a value in the dct if the key passed
       exists else it returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
