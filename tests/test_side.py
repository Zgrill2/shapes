import pytest
from shapes.side import Side


def test_generate_side(side_factory):
    side_a = side_factory(1)
    assert side_a.length == 1
    assert isinstance(side_a, Side)


def test_side_addition(side_factory):
    side_a = side_factory(3)
    side_b = side_factory(4)
    assert side_a + side_b == 7


def test_side_added_by_int(side_factory):
    side_a = side_factory(3)
    int_b = 4
    assert side_a + int_b == 7


def test_side_squared(side_factory):
    side_a = side_factory(3)
    assert side_a ** 2 == 9


def test_side_multiplication(side_factory):
    side_a = side_factory(3)
    assert side_a * side_a == 9


def test_side_multiplied_by_int(side_factory):
    side_a = side_factory(3)
    int_a = 3
    assert side_a * int_a == 9
