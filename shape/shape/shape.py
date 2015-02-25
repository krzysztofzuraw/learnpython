import abc
import math
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='shape.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class Shape(object):
    """Shape abstract class"""
    __metaclass__ = abc.ABCMeta


    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    """Triangle class"""

    def get_sides(self):
        return [self.a, self.b, self.c]

    def __init__(self, a, b, c):
        """
        Create new triangle with given:
        :param a: side a
        :param b: side b
        :param c: side c
        """
        logger.info('Creating a triangle')
        self.a = a
        self.b = b
        self.c = c
        if any(i < 0 for i in self.get_sides()):
            logger.error("Triangle can't be created with negative values")
            raise ValueError("You can't make triangle")

    def is_possible(self):
        """
        Check if it's possible to make triangle
        :return: True when it possible otherwise False
        """
        logger.info('Checking if triangle is possible')
        sides = self.get_sides()
        maxium = sides.pop(sides.index(max(sides)))
        if maxium >= sum(sides):
            return False
        else:
            return True

    def area(self):
        """
        Compute area of triangle using Heron's equation
        :return: area of triangle
        """
        logger.info('Calculating area of triangle')
        p = sum(self.get_sides()) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        """
        Compute perimeter of triangle by summing up its sides
        :return: perimeter
        """
        logger.info('Calculating perimeter of triangle')
        return sum(self.get_sides())


class Circle(Shape):
    """Circle class"""


    def __init__(self, r):
        """
        Create new circle with given :
        :param r: radius
        """
        logger.info('Creating a circle')
        self.r = r
        if self.r <= 0:
            logger.error("Circle can't be created with negative values")
            raise ValueError("You can't make Circle")


    def area(self):
        """
        Compute approx area of circle
        :return: area
        """
        logger.info('Calculating area of circle')
        return math.pi * self.r ** 2

    def perimeter(self):
        """
        Compute approx perimeter of circle
        :return: perimeter
        """
        logger.info('Calculating perimeter of circle')
        return 2 * math.pi * self.r


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, a, b):
        """
        Create new rectangle with
        :param a: side a (shorter)
        :param b: side b (longer)
        """
        logger.info('Creating a circle')
        self.a = a
        self.b = b
        if any(i < 0 for i in (self.a, self.b)):
            logger.error("Rectangle can't be created with negative values")
            raise ValueError("You can't make Rectangle")


    def perimeter(self):
        """
        Compute the perimeter of rectangle
        :return: perimeter
        """
        logger.info('Calculating perimeter of rectangle')
        return 2 * self.a + 2 * self.b

    def area(self):
        """
        Compute the area of rectangle
        :return: area
        """
        logger.info('Calculating area of rectangle')
        return self.a * self.b


class Trapeze(Shape):
    """Trapeze class"""

    def __init__(self, a, b, c, d):
        """
        Create new trapeze
        :param a: top side
        :param b: bottom side
        :param c: left side
        :param d: right side
        """
        logger.info('Creating a trapeze')
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        if any(i < 0 for i in (self.a, self.b, self.c, self.d)):
            logger.error("Trapeze can't be created with negative values")
            raise ValueError("You can't make Trapeze")

    def perimeter(self):
        """
        Compute the perimeter of Trapeze
        :return: perimeter
        """
        logger.info('Calculating perimeter of trapeze')
        return self.a + self.b + self.c + self.d

    def area(self):
        """
        Compute the area of Trapeze
        :return: area
        """
        logger.info('Calculating area of trapeze')
        if self.a > self.b:
            return 0.25 * (((self.a + self.b) / (self.a - self.b))
                           * math.sqrt(self.a - self.b + self.c + self.d)
                           * math.sqrt(self.a - self.b - self.c + self.d)
                           * math.sqrt(self.a - self.b + self.c - self.d)
                           * math.sqrt(-self.a + self.b + self.c + self.d))
        elif self.b == 0:
            p = sum(self.a + self.c + self.d) / 2
            return math.sqrt(p * (p - self.a) * (p - self.c) * (p - self.d))
