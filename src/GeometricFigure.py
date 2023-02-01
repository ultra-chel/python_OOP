from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square


class GeometricFigure:

    def __init__(self):
        self.area = None

    def add_area(self, figure):
        if isinstance(figure, (Rectangle, Circle, Triangle, Square, GeometricFigure)) == "false":
            raise ValueError
        sum_area = self.area + figure.area
        return sum_area
