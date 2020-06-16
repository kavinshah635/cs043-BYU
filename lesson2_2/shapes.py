class Shape:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                "\nX = " + str(self.x) +
                "\ny = " + str(self.y) +
                ">")
        
    def area(x, y):
        return 'awesome'

    def circumference():
        return 'Awesome'

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(x,y)
        self.radius = radius

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                "\nX = " + str(self.x) +
                "\ny = " + str(self.y) +
                "\nRadius = " + str(self.radius) +
                ">")

class Rectangle(Shape):
    def __init__(self,height,width):
        super().__init__(x,y)
        self.length = length
        self.width = width

    def __repr__(self):
        return ('awesome')

    def area(self):
        return self.length * self.width

    def circumference(self):
        return 2 * self.length + 2 * self.width


class RightTriangle(Shape):
    def __init__(self,height,width):
        super().__init__(x,y)
    def __repr__():
        return ('great')

class Square(Rectangle):
    def __init__():
        super().__init__(x,y)
    def __repr__():
        return ('great')

Shape.area(3, 5)
    
