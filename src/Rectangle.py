from src.GeometricFigure import GeometricFigure


class Rectangle(GeometricFigure):
    name = "Rectangle"

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b)*2
