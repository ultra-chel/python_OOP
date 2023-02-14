import random

from src.Rectangle import Rectangle
from src.Circle import Circle

side_a = random.randint(1, 1000)
side_b = random.randint(1, 1000)
rectangle = Rectangle(side_a, side_b)


def test_p_rectangle_calc_area():
    assert rectangle.area == side_a * side_b, "Rectangle area calculation is not correct"


def test_p_rectangle_calc_perimeter():
    assert rectangle.perimeter == (side_a + side_b) * 2, "Rectangle perimeter calculation is not correct"


def test_p_rectangle_calc_addarea():
    circle = Circle(random.randint(1, 1000))
    assert rectangle.add_area(
        circle) == circle.area + rectangle.area, "Sum areas of circle and rectangle is not correct"
