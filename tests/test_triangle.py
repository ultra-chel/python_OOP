import random
import pytest

from src.Rectangle import Rectangle
from src.Triangle import Triangle

side_a = random.randint(1, 1000)
side_b = random.randint(1, 1000)
side_c = random.randint(1, 1000)
triangle = Triangle(side_a, side_b, side_c)


def test_p_triangle_calc_area():
    assert triangle.area == side_a * side_b * side_c, "Triangle area calculation is not correct"


def test_p_triangle_calc_perimeter():
    assert triangle.perimeter == side_a + side_b + side_c, "Triangle perimeter calculation is not correct"


def test_p_triangle_calc_addarea():
    rectangle = Rectangle(random.randint(1, 1000), random.randint(1, 1000))
    assert triangle.add_area(
        rectangle) == rectangle.area + triangle.area, "Sum areas of triangle and rectangle is not correct"


def test_n_triangle_addarea_not_geometricfigure():
    with pytest.raises(ValueError):
        triangle.add_area("gogi")


def test_p_triangle_incorrect_init():
    with pytest.raises(ValueError):
        Triangle(random.randint(1, 1000), random.randint(1, 1000), 0)
