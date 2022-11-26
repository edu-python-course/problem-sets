import unittest

from conv_store import models


class TestProductModel(unittest.TestCase):

    def setUp(self) -> None:
        self.product_name = "apple"
        self.product_price = 15.1
        self.instance = models.Product(self.product_name, self.product_price)

    def test_initializer(self):
        self.assertEqual(self.product_name, self.instance.name)
        self.assertEqual(self.product_price, self.instance.price)

    def test_str(self):
        self.assertEqual(self.product_name, str(self.instance))

    def test_equality_comparing(self):
        another = models.Product("apple", 15.1)
        self.assertEqual(another, self.instance)

    def test_equality_raises(self):
        self.assertRaises(TypeError, self.instance.__eq__, "apple")
        self.assertRaises(TypeError, self.instance.__eq__, 15.1)

    def test_get_total(self):
        self.assertEqual(10.57, self.instance.get_total(0.7))


class TestShoppingCartModel(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = models.ShoppingCart()
        apple = models.Product("apple", 10.59)
        juice = models.Product("juice", 36.55)
        self.products = [apple, juice]
        self.quantities = [0.7, 4]
        self.instance.add_product(apple, 0.7)
        self.instance.add_product(juice, 4)

    def test_products(self):
        self.assertListEqual(self.products, self.instance.products)
        self.assertListEqual(self.quantities, self.instance.quantities)

    def test_add_product(self):
        spice = models.Product("spice", 120.25)
        self.instance.add_product(spice, .100)
        self.assertListEqual(self.products + [spice], self.instance.products)
        self.assertListEqual(self.quantities + [.1], self.instance.quantities)

    def test_add_existing_product(self):
        # avoid existing objects usage
        apple = models.Product("apple", 10.59)
        juice = models.Product("juice", 36.55)
        self.quantities = [self.quantities[0] + 1.5, self.quantities[1] + 2]

        self.instance.add_product(apple, 1.5)
        self.instance.add_product(juice, 2)
        self.assertListEqual(self.products, self.instance.products)
        self.assertListEqual(self.quantities, self.instance.quantities)

    def test_get_total(self):
        self.assertEqual(153.61, self.instance.get_total())
