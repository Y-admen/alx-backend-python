#!/usr/bin/env python3
"list of tuples containing the element and its length"
from typing import List, Tuple, Sequence


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing the element and its length.
    """
    return [(i, len(i)) for i in lst]
