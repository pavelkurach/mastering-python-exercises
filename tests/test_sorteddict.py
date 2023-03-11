import pytest

from pythonic_design_patterns.sorteddict import SortedDict


def test_init():
    sd = SortedDict(keyfunc=lambda x: x[1], c=3, d=4, a=1, b=2)
    assert sd.to_dict() == {"a": 1, "b": 2, "c": 3, "d": 4}
