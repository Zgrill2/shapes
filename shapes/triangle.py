import math

from shapes.shape import Shape


class Triangle(Shape):

    def __init__(self, sides):

        super().__init__(sides)
        assert self.sides == 3

    @property
    def height(self):
        return self.sides[0] * math.sin(self.sides[2])

    @property
    def area(self):
        return 0.5 * self.side[0] * self.side[1] * math.sin(self.side[2])

    @property
    def is_imaginary(self):
        try:
            self.pythagorean_theorem()
        except AssertionError:
            return True
        return False

    @property
    def is_real(self):
        return not self.is_imaginary

    def pythagorean_theorem(self, order=(0, 1, 2)):
        assert (self.side[order[0]] ** 2) + (self.side[order[1]] ** 2) == self.side[order[2]] ** 2
        return True


if __name__ == '__main__':
    from shapes.side import Side

    s = (Side(3), Side(4), Side(5))
    t = Triangle(s)
    assert t.is_imaginary is True
    s = (Side(3), Side(4), Side(8))
    t = Triangle(s)
    assert t.is_imaginary is False
