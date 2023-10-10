#!/usr/bin/env python3
"""
    This module contains a coroutine measure_runtime
    that will execute async_comprehension four times
    in parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns the run time of all four tasks."""
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(5)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start
