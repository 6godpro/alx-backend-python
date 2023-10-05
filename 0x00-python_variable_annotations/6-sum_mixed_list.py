#!/usr/bin/env python3
"""
A function sum_mixed_list which takes a list arguments containing integers
and floats and return their sum.
 """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of values in mxd_lst."""
    return sum(mxd_lst)
