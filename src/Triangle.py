from src.GeometricFigure import GeometricFigure


class Triangle(GeometricFigure):
    name = "Triangle"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        return self.a * self.b * self.c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

