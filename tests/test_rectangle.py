import pytest
from src.Rectangle import Rectangle


def test_p_calc_area():
    rectangle = Rectangle(15, 15)
    assert rectangle.area == 15*15, "Rectangle area calculation is not correct"
