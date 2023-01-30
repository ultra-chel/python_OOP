from src.GeometricFigure import GeometricFigure

#
# class Square(GeometricFigure):
#     name = "Square"
#
#     def __init__(self, side):
#         self.side = side
#
#     @property
#     def area(self):
#         return self.side ** 2
#
#     @property
#     def perimeter(self):
#         return self.side * 4


from src.Rectangle import Rectangle
from src.Circle import Circle


class Square(Rectangle):
    name = "Square"

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side**2


square = Square(side=3)
print(square.area)

print(Square.area)
print(Circle.area)
print(square.add_area(Circle.area))
