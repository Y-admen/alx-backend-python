#!/usr/bin/env python3
"""concurrent_coroutines"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    wait = [await wait_random(max_delay) for _ in range(n)]
    results = wait.sort()
    return wait
