#!/usr/bin/python3
"""The My Int module"""


class MyInt(int):
    """My int class"""

    def __eq__(self, other):
        return super(MyInt, self).__ne__(other)

    def __ne__(self, other):
        return super(MyInt, self).__eq__(other)
