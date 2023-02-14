import random

from src.Square import Square
from src.Triangle import Triangle

side = random.randint(1, 1000)
square = Square(side)


def test_p_square_calc_area():
    assert square.area == side ** 2, "Square area calculation is not correct"


def test_p_square_calc_perimeter():
    assert square.perimeter == side * 4, "Square perimeter calculation is not correct"


def test_p_square_calc_addarea():
    triangle = Triangle(random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000))
    assert square.add_area(
        triangle) == square.area + triangle.area, "Sum areas of triangle and square is not correct"
