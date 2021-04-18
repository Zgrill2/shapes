from typing import Union


class Side:
    def __init__(self, l: int = 0):
        self.length = l

    def __pow__(self, power: int, modulo=None) -> int:
        result = self.length ** power
        assert isinstance(power, int)
        return result

    def __add__(self, other):
        if isinstance(other, Side):
            return self.length + other.length
        elif isinstance(other, float) or isinstance(other, int):
            return self.length + other

    def __int__(self) -> int:
        return self.length

    def __mul__(self, other):
        if isinstance(other, Side):
            return self.length * other.length
        elif isinstance(other, float) or isinstance(other, int):
            return self.length * other
