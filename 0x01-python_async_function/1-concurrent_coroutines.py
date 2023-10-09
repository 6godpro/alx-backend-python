#!/usr/bin/env python3
"""
An  async routine called wait_n that takes in two (2)
integer arguments. wait_random is spawned n times
with the specified max_delay.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a sorted list of all the delays."""
    routines = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*routines))
