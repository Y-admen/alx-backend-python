#!/usr/bin/env python3
"Async Comprehensions"
from typing import Generator
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """_summary_

    Returns:
        AsyncGenerator[float, None]: _description_
    """
    return [_ async for _ in async_generator()]
