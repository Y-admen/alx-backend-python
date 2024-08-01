#!/usr/bin/env python3
"tuple with the squared value of v"
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the squared value of v."""
    return (k, v**2)
