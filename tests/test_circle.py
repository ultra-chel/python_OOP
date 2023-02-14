import random

from src.Square import Square
from src.Circle import Circle

radius = random.randint(1, 1000)
circle = Circle(radius)


def test_p_circle_calc_area():
    assert circle.area == 3.14 * (radius ** 2), "Circle area calculation is not correct"


def test_p_circle_calc_circumference():
    assert circle.circumference == 3.14 * radius * 2, "Circle circumference calculation is not correct"


def test_p_circle_calc_addarea():
    square = Square(random.randint(1, 1000))
    assert circle.add_area(
        square) == circle.area + square.area, "Sum areas of circle and square is not correct"
