#!/usr/bin/env python3
"""
A measure_time function with integers parameters
n and max_delay that measures the total execution
time for wait_n(n, max_delay), and returns total_time / n.
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
       Returns total time taken for the operation
       divided by total operations perfomed.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
