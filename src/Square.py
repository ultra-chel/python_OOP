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
circle = Circle(15)

print(square.area)
print(circle.area)
print(square.add_area(circle))
