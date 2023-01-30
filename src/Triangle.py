from src.GeometricFigure import GeometricFigure
import pytest


class Triangle(GeometricFigure):
    name = "Triangle"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a == 0 | b == 0 | c == 0:
            raise ValueError

    @property
    def area(self):
        return self.a * self.b * self.c

    @property
    def perimeter(self):
        return self.a + self.b + self.c
