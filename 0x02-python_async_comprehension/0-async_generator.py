#!/usr/bin/env python3
"""
    This module contains a coroutine called async_generator
    that takes no arguments, sleeps for one (1) second between
    each iteration and yields a random number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """Returns an asynchronous generator."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
