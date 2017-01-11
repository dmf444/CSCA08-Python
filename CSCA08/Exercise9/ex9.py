import math


class Shape():
    '''Defines the basic parameters for a shape and allows for most functions to be put into a higher class'''

    def __init__(self, base, side, theta, shape):
        """
        (Shape) -> NoneType
        :param side: float value, cannot be null
        :param theta: float value, cannot be null, must be between 0 -> 360
        :param base: float value, cannot be null
        :param shape: string, represents the shape, cannot be null.
        """
        self._base = base
        self._side = side
        self._theta = theta
        self._shape = shape

    def area(self):
        """ (Shape) -> Float area
        Returns the area of given shape, defaults to the shape of a parallelogram.
        REQ: Shape must be instantiated.
        """
        # Convert degrees to rads
        radians = math.radians(self.get_theta())
        # Sine of given rads
        sine = math.sin(radians)
        # Find area of shape and return
        area = self.get_base() * self.get_side() * sine
        return area

    def bst(self):
        """ (Shape) -> [list of floats]
        Returns a list of floats formatted into [base, side, theta].
        REQ: Shape must be instantiated.
        """
        # Format the list and return it
        return [self.get_base(), self.get_side(), self.get_theta()]

    def __str__(self):
        """ (Shape) -> str
        Returns the string of the of shape in the format: I am a SHAPE with area AREA
        REQ: Shape must be instantiated.
        """
        # Format the string and return it
        return "I am a " + self.get_shape() + " with area " + str(self.area())

    def get_theta(self):
        """ (Shape) -> float
        Returns the instance of shape's angle
        REQ: Shape must be instantiated.
        """
        return self._theta

    def get_side(self):
        """ (Shape) -> float
        Returns the instance of shape's side
        REQ: Shape must be instantiated.
        """
        return self._side

    def get_base(self):
        """ (Shape) -> float
        Returns the instance of shape's base
        REQ: Shape must be instantiated.
        """
        return self._base

    def get_shape(self):
        """ (Shape) -> str
        Returns the instance of shape's shape
        REQ: Shape must be instantiated.
        """
        return self._shape

    def set_shape(self, new_shape):
        """  (Shape, str) -> NoneType
        :param new_shape: string, represents the new shape
        :return: NoneType
        """
        self._shape = new_shape


class Parallelogram(Shape):
    '''Class that represents a parallelogram'''

    def __init__(self, base, side, theta):
        """
        (Parallelogram) -> NoneType
        :param side: float value, cannot be null
        :param theta: float value, cannot be null, must be between 0 -> 360
        :param base: float value, cannot be null
        """
        Shape.__init__(self, base, side, theta, "Parallelogram")


class Rhombus(Parallelogram):
    '''Class that represents a rhombus'''

    def __init__(self, base, theta):
        """
        (Rhombus) -> NoneType
        :param theta: float value, cannot be null, must be between 0 -> 360
        :param base: float value, cannot be null
        """
        Shape.__init__(self, base, base, theta, "Rhombus")


class Rectangle(Shape):
    '''Class that represents a rectangle'''

    def __init__(self, base, side):
        """
        (Rectangle) -> NoneType
        :param side: float value, cannot be null
        :param base: float value, cannot be null
        """
        Shape.__init__(self, base, side, 90.0, "Rectangle")


class Square(Rectangle):
    '''Class that represents a square'''

    def __init__(self, base):
        """
        (Square) -> NoneType
        :param base: float value, cannot be null
        """
        Rectangle.__init__(self, base, base)
        # Extra call to properly set the shape
        self.set_shape("Square")
