import pytest


@pytest.mark.parametrize("a, b, c", [(3, 4, 5), (5, 12, 13), (21, 20, 29), (15, 8, 17)])
def test_magic_triangles(triangle_factory, a, b, c):
    triangle = triangle_factory(sides=(a, b, c))
    assert triangle.is_real


@pytest.mark.parametrize("a, b, c", [(3, 4, 25), (5, 12, 213), (21, 20, 229), (15, 8, 217)])
def test_imaginary_triangles(triangle_factory, a, b, c):
    triangle = triangle_factory(sides=(a, b, c))
    assert triangle.is_imaginary