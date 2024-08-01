#!/usr/bin/env python3
"concat str1/str2"
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "multiplier"
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
