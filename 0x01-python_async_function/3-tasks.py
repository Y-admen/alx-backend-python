#!/usr/bin/env python3
"""tasks"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delayL: int) -> asyncio.Task:
    """_summary_

    Args:
        max_delayL (int): _description_

    Returns:
        _type_: _description_
    """
    task = asyncio.create_task(wait_random())
    return task
