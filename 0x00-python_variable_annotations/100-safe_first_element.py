#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from types import NoneType
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Returns the first element in the iterable"""
    if lst:
        return lst[0]
    else:
        return None
