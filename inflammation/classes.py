import math

"""
Class examples
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2*math.pi*self.radius
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
class Rectangle:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def circumference(self):
        return 2*(self.a + self.b)
    def __repr__(self):
        return f"Square(side_a={self.a}, side_b={self.b})"
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)
    def __repr__(self):
        return f"Square(side={self.a})"
    

if __name__ == "__main__":
    my_circle = Circle(10)
    my_square = Square(5)

    for shape in [my_circle, my_square]:
        print(type(shape))
        print(my_circle.circumference)
