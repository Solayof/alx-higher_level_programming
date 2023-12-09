#!/usr/bin/python3
"""
Rectanlge Class

"""
from models.base import Base


class Rectanlge(Base):
    """
    declare  class Rectangle
    Class Attributes:
        __init__(self, width, height, x=0, y=0, id=None)
    Methods:
    Inherited method:

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        args:
            width (int): the width of the new Rectangle
            height (int): the height of the new Rectangle
            x (int): the x coordinate
            y (int): the y coordinate
        Raises:
            TypeError: if either width, height, x, y, is/are not int
            ValueError: if either width, height, x, y, is/are less than or equal to zero
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    def width(self):
        """Get the width"""
        return self.__width
    
    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Get Class height"""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        "Get the x coordinate"
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an intger")
        if val <= 0:
            raise ValueError("x must be > 0")
        self.__x = val

    @property
    def y(self):
        """Get y coordinate"""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val <= 0:
            raise ValueError("y must be > 0")
        self.__y = val

    def area(self):
        """Calculate the area of rectangle"""
        return self.height * self.width
    
    def display(self):
        """Display Rectangular # of height by width"""
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """redefine __str__ representation of the object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """updates Rectangle Class attributes"""
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                if k == 1:
                    self.width = v
                if k == 2:
                    self.height = v
                if k == 3:
                    self.x = v
                if k == 4:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id == kwargs["id"]
            if "width" in kwargs:
                self.width == kwargs["width"]
            if "height" in kwargs:
                self.height == kwargs["height"]
            if "x" in kwargs:
                self.x == kwargs["x"]
            if "y" in kwargs:
                self.y == kwargs["y"]

        def to_dictionary(self):
            """Retruns the dictionary representation"""
            dic_ = {}
            dic_["id"] = self.id
            dic_["width"] = self.width
            dic_["height"] = self.height
            dic_["x"] = self.x
            dic_["y"] = self.y
            return dic_