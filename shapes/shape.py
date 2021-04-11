import typing

from shapes.side import Side


class Shape:
    def __init__(self, sides: typing.Tuple[Side, ...] = ()):
        self.sides = len(sides)
        self.side = sides

    @property
    def area(self):
        return 0

    @property
    def perimeter(self):
        return 0
