import pytest

def test_1_method():

    x, y = 5, 6
    assert x+1 == y, "test failed"
    assert x == y, "test failed"


def test_2_method():
    x, y = 5, 6
    assert x+1 == y,"test failed"
