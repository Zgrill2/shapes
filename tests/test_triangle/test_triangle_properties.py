import pytest


@pytest.mark.parametrize("a, b, c", [(3, 4, 5), (5, 12, 13), (21, 20, 29), (15, 8, 17)])
def test_height(triangle_factory, a, b, c):
    triangle = triangle_factory(sides=(a, b, c))
    h = triangle.height
    pass


def test_area():
    pass
