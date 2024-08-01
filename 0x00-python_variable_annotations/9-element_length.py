#!/usr/bin/env python3
"list of tuples containing the element and its length"
from typing import Tuple, List, Sequence


def element_length(lst) -> List[Tuple[Sequence, int]]:
	"""
	Return a list of tuples containing the element and its length
	"""
	return [(i, len(i)) for i in lst]
