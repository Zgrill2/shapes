import typing

import pytest

from shapes.side import Side
from shapes.triangle import Triangle


@pytest.fixture(scope='session')
def triangle_factory():
    def generator(sides: typing.Tuple[int, ...] = ()):
        assert len(sides) == 3
        side_set = [Side(s) for s in sides]
        side_set = (*side_set, )
        return Triangle(side_set)

    return generator


@pytest.fixture(scope='session')
def side_factory():
    def generator(length: int = 0):
        return Side(length)
    return generator
