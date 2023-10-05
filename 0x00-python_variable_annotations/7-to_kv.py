#!/usr/bin/env python3
"""
A function to_kv that takes a string k and an int OR float v as arguments and
returns a tuple. The first element of the tuple is the string k. The second
element is the square of the int/float v and should be annotated as a float.
"""
from math import sqrt
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of k and v."""
    return (k, v ** 2)