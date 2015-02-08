from nose.tools import *
from product.product_inv import Product, Inventory
import unittest

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.car = Product(3,3,'Audi',5)
        self.computer = Product(4,100,'Mac',1)
        self.inv = Inventory()
    def teardown(self):
        pass
    def test_car(self):
        self.assertEqual(self.car.ids, 3)
        self.assertEqual(self.car.price, 3)
        self.assertEqual(self.car.name, 'Audi')
        self.assertEqual(self.car.quantity, 5)
        self.car.price = 10
        self.car.quantity = 20
        self.assertEqual(self.car.price, 10)
        self.assertEqual(self.car.quantity, 20)
        self.assertRaises(TypeError, self.car.ids)
        self.assertRaises(TypeError, self.car.name)
        self.assertEqual(repr(self.car), "Product: 3")
        self.assertEqual(str(self.car), "Audi with 10 price and 20 quanitity")
    def test_inventory(self):
        self.inv.add_product(self.car)
        self.assertEqual(self.inv.products, {3:['Audi',3,5]})
        self.inv.add_product(self.computer)
        self.assertEqual(self.inv.products, {3:['Audi',3,5], 4:['Mac',100,1]})
        self.assertEqual(self.inv.sum_price(), 103)
        self.assertEqual(self.inv.sum_quantity(), 6)
        self.assertEqual(self.inv.sum_products(), 2)

