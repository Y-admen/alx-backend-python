#!/usr/bin/env python3
"Run time for four parallel comprehensions"
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    start = time.time()
    await async_comprehension()
    end = time.time()
    return end - start
