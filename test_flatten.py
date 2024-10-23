import pytest
from main import flatten

def test_flatten_simple():
    assert flatten(lst=[1, 2, 3]) == [1, 2, 3]

def test_flatten_nested():
    assert flatten(lst=[1, 2, [4, 5], [6, [7]], 8]) == [1, 2, 4, 5, 6, 7, 8]

def test_flatten_deeply_nested():
    assert flatten(lst=[[[1], 2], [[3], [4, [5]]]]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    assert flatten(lst=[]) == []

def test_flatten_with_empty_nested_list():
    assert flatten(lst=[1, [], [2, []], 3]) == [1, 2, 3]

def test_flatten_nested_depth_1():
    assert flatten(lst=[1, [2, [3, 4], 5], 6], depth=1) == [1, 2, [3, 4], 5, 6]

def test_flatten_nested_depth_2():
    assert flatten(lst=[1, [2, [3, 4], 5], 6], depth=2) == [1, 2, 3, 4, 5, 6]

def test_flatten_nested_depth_3():
    assert flatten(lst=[1, [2, [3, [4, 5]]]], depth=3) == [1, 2, 3, 4, 5]


