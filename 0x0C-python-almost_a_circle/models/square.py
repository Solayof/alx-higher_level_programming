#!/usr/bin /python3
"""
Square Class

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Dedclare Square Class
    Attributes:
        __init__(self, size, x=0, y=0, id=None)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        args:
            width (int): the width of the new Rectangle
            height (int): the height of the new Rectangle
            x (int): the x coordinate
            y (int): the y coordinate
        Raises:
            TypeError: if either width, height, x, y, is/are not int
            ValueError: if either width, height, x, y, is/are <= 0
        """

        super().__init__(size, size, x, y, id)

        @property
        def size(self):
            """Get the size of a Square class"""
            return self.height

        @size.setter
        def size(self, val):
            self.width = val
            self.height = val

        def __str__(self):
            """define the string representation"""
            return f"[square] ({self.id}) {self.x}/{self.y} - {self.size}"

        def update(self, *args, **kwargs):
            """updates Rectangle Class attributes"""
            if args:
                for k, v in enumerate(args):
                    if k == 0:
                        self.id = v
                    if k == 1:
                        self.size = v
                    if k == 2:
                        self.x = v
                    if k == 3:
                        self.y = v
            else:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.width = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

        def to_dictionary(self):
            """Return dictionary representation"""
            dic_ = {}
            dic_["id"] = self.id
            dic_["size"] = self.size
            dic_["x"] = self.x
            dic_["y"] = self.y
            return dic_
