class GeometricFigure:

    def __init__(self):
        self.area = None

    def add_area(self, figure):
        if isinstance(figure, GeometricFigure) == "false":
            raise ValueError
        sum_area = self.area + figure.area
        return sum_area
