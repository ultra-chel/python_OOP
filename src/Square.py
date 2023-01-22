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


# Недоработаный вариант наследования от прямоугольника:
# для работы с классом квадрата, логично в аргумент передавать только 1 сторону,
# но т.к. он наследуется от Rectangle он по умолчанию в аргумент принемает 2 стороны и на функцию __init__ ругается что есть в родительском классе, не понятно как это исправить и внутри класса работать с одним атрибутом
# внутри класса квадрат я бы переопределил расчет площади

from src.Rectangle import Rectangle

class Square(Rectangle):
    name = "Square"
    side =??
    @property
    def area(self):
        return self.side**2


square = Square(side=3)
print(square.area)
