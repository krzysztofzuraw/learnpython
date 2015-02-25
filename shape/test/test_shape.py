import pytest
from shape.shape import Circle, Triangle, Rectangle, Trapeze


class TestTriangle:
    @classmethod
    def setup_class(cls):
        cls.triangle_1 = Triangle(1, 2, 3)
        cls.triangle_2 = Triangle(2, 3, 4)

    def test_triangle_1(cls):
        assert cls.triangle_1.is_possible() == False

    def test_triangle_2(cls):
        assert cls.triangle_2.is_possible() == True
        assert cls.triangle_2.area() == 2.9047375096555625
        assert cls.triangle_2.perimeter() == 9

    @pytest.mark.xfail(raises=ValueError)
    def test_fail_triangle(cls):
        cls.triangle_3 = Triangle(-1, -2, -3)
        cls.triangle_4 = Triangle(-1, 2, 3)


class TestCircle:

    def setup_class(self):
        self.circle = Circle(4)

    def test_circle(self):
        assert round(self.circle.area() - 50.27, 2) == 0
        assert round(self.circle.perimeter() - 25.13, 2) == 0

    @pytest.mark.xfail(raises=ValueError)
    def test_fail_circle(self):
        self.circle_2 = Circle(-10)


class TestRectangle:
    def setup_class(self):
        self.rectangle_1 = Rectangle(2, 3)

    def test_rectangle(self):
        assert self.rectangle_1.area() == 6
        assert self.rectangle_1.perimeter() == 10

    @pytest.mark.xfail(raises=ValueError)
    def test_fail_rectangle(self):
        self.rectangle_2 = Rectangle(-1, -2)


class TestTrapeze:
    def setup_class(self):
        self.trapeze_1 = Trapeze(5, 3, 2, 2)
        self.trapeze_2 = Trapeze(2, 0, 8, 9)

    def test_trapeze_1(self):
        assert round(self.trapeze_1.area() - 6.92) == 0
        assert self.trapeze_1.perimeter() == 12
        
    def test_trapeze_2(self):
        assert round(self.trapeze_2.area() - 7.31) == 0
        assert self.trapeze_2.perimeter() == 19

    @pytest.mark.xfail(raises=ValueError)
    def test_fail_trapeze(self):
        self.trapeze_3 = Trapeze(-1, 2, 3, 4)