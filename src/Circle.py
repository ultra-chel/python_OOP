from src.GeometricFigure import GeometricFigure


class Circle(GeometricFigure):
    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * (self.radius ** 2)

    @property
    def circumference(self):
        return 3.14 * self.radius * 2
