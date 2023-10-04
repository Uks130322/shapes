"""Module shape: contains classes Shape, Circle, RightTriangle, Rectangle and Square"""


class Shape:
    """Contains coordinates of shape and const pi"""
    pi = 3.14159

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class Circle(Shape):
    """Class Circle"""
    all_circles = []

    def __init__(self, radius=1, x=0, y=0):
        """Create new instance of class Circle with radius"""
        super().__init__(x, y)
        self.__radius = radius
        self.__class__.all_circles.append(self)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius >= 0:
            self.__radius = new_radius

    def area(self):
        """Calculate the area of circle for instance of Circle"""
        return self.__class__.pi * self.__radius * self.__radius

    @classmethod
    def total_area(cls):
        total = 0
        for item in cls.all_circles:
            total += item.area()
        return total

    def circuit(self):
        """Calculate the perimetr of rectangle for instance of Rectangle"""
        return self.__radius * 2 * self.__class__.pi

    @classmethod
    def total_circuit(cls):
        total = 0
        for item in cls.all_circles:
            total += item.circuit()
        return total


class RightTriangle(Shape):
    """Class RightTriangle"""
    all_triangles = []

    def __init__(self, side=1, x=0, y=0):
        """Create new instance of class Circle with radius"""
        super().__init__(x, y)
        self.__side = side
        self.__class__.all_triangles.append(self)

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        if new_side >= 0:
            self.__side = new_side

    def area(self):
        """Calculate the area of triangle for instance of RightTriangle"""
        return self.__side * self.__side * 3 ** 0.5

    @classmethod
    def total_area(cls):
        total = 0
        for item in cls.all_triangles:
            total += item.area()
        return total

    def perimeter(self):
        """Calculate the perimetr of rectangle for instance of Rectangle"""
        return self.__side * 3

    @classmethod
    def total_circuit(cls):
        total = 0
        for item in cls.all_triangles:
            total += item.circuit()
        return total


class Rectangle(Shape):
    """class Rectangle"""
    all_rectangles = []

    def __init__(self, length=2, wight=1, x=0, y=0):
        """Create new instance of class Rectangle with length and wight"""
        super().__init__(x, y)
        self.__length = length
        self.__wight = wight
        self.__class__.all_rectangles.append(self)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        if new_length >= 0:
            self.__length = new_length

    @property
    def wight(self):
        return self.__wight

    @wight.setter
    def wight(self, new_wight):
        if new_wight >= 0:
            self.__wight = new_wight

    def area(self):
        """Calculate the area of rectangle for instance of Rectangle"""
        return self.__length * self.__wight

    @classmethod
    def total_area(cls):
        total = 0
        for item in cls.all_rectangles:
            total += item.area()
        return total

    def perimeter(self):
        """Calculate the perimeter of rectangle for instance of Rectangle"""
        return (self.__length + self.__wight) * 2

    @classmethod
    def total_perimeter(cls):
        total = 0
        for item in cls.all_rectangles:
            total += item.perimeter()
        return total


class Square(Rectangle):
    """class Square"""
    all_squares = []

    def __init__(self, side=1):
        """Create new instance of class Square with length of side"""
        super().__init__(side, side)
        self.__side = side
        self.__class__.all_squares.append(self)

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        if new_side >= 0:
            self.__side = new_side
            super().__init__(self.__side, self.__side)

    @classmethod
    def total_area(cls):
        total = 0
        for item in cls.all_squares:
            total += item.area()
        return total

    @classmethod
    def total_perimeter(cls):
        total = 0
        for item in cls.all_squares:
            total += item.perimeter()
        return total
