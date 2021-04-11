import pytest
from shapes.side import Side


def test_generate_side(side_factory):
    side_a = side_factory(1)
    assert side_a.length == 1
    assert isinstance(side_a, Side)


def test_side_addition(side_factory):
    side_a = side_factory(3)
    side_b = side_factory(4)

    assert (side_a + side_b) == 7


def test_side_squared(side_factory):
    side_a = side_factory(3)
    assert (side_a ** 2) == 9
