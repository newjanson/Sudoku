from quicksort import quicksort
from hypothesis import given
from hypothesis.strategies import lists, integers
from typing import List


@given(lst = lists(integers(), 0, 30))
def test_quicksort(lst: List[int]):
    quicksort(lst, 0, len(lst)-1)
    for i in range(1, len(lst)):
        assert(lst[i-1] <= lst[i])
