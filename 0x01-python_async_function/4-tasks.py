#!/usr/bin/env python3
"""concurrent_coroutines"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    wait = sorted([await task_wait_random(max_delay) for _ in range(n)])
    return wait
