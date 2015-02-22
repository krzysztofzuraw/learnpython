import abc
import math


class Shape(object):

    """docstring for Shape"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_possible():
        pass

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):

    """docstring for Triangle"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_sides(self):
        return [self.a, self.b, self.c if self.a and
                self.b and self.c > 0 else None]

    def is_possible(self):
        sides = self.get_sides()
        maxium = sides.pop(sides.index(max(sides)))
        if maxium >= sum(sides):
            return False
        else:
            return True

    def area(self):
        """Using Heron's 'wzór'"""
        p = sum(self.get_sides()) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return sum(self.get_sides())


class Cicle(object):

    """docstring for Cicle"""

    def __init__(self, r):
        self.r = r

    def is_possible(self):
        return True

    def area(self):
        return math.pi() * self.r

    def perimeter(self):
        return 2 * math.pi() * self.r


class Rectangle(object):

    """docstring for Rectangle"""

    def __init__(self, a, b):
        self.a = a
        self.b = b
