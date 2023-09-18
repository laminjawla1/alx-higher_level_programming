#!/usr/bin/python3
"""This model implements the the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The blueprint for the square instances

    It inherits from the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer"""
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """The string representation of the current object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Size getter"""
        return super(Square, self).width

    @size.setter
    def size(self, size):
        """Size setter"""
        self.width = self.height = size

    def update(self, *args, **kwargs):
        """Update"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            for attr_name in ['size', 'x', 'y']:
                if attr_name in kwargs:
                    setattr(self, attr_name, kwargs[attr_name])

    def to_dictionary(self):
        """To dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
