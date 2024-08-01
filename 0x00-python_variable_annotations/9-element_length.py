#!/usr/bin/env python3
"concat str1/str2"
from typing import Tuple, List, Sequence


def element_length(lst) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
