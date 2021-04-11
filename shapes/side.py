class Side:
    def __init__(self, l: int = 0):
        self.length = l

    def __pow__(self, power, modulo=None):
        result = self.length ** power
        return result

    def __add__(self, other):
        return self.length + other.length
