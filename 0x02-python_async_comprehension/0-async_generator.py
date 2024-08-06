#!/usr/bin/env python3
"Async Generator"
from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[int, any]:
    """_summary_

    Returns:
        AsyncGenerator[int, any]: _description_

    Yields:
        Iterator[AsyncGenerator[int, any]]: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
