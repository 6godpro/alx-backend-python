#!/usr/bin/env python3
"""
A function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
       Returns an anonymous function that multiplies the argument
       by multiplier.
    """
    return lambda x: multiplier * x
