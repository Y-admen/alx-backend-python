#!/usr/bin/env python3
"Async Generator"
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """_summary_

    Returns:
        AsyncGenerator[int, any]: _description_

    Yields:
        Iterator[AsyncGenerator[int, any]]: _description_
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
