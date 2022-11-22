import unittest

from conv_store import models


class TestProductModel(unittest.TestCase):
    PRODUCT_NAME = "cheese"
    PRODUCT_PRICE = 128.45

    def setUp(self) -> None:
        self.instance = models.Product(
            TestProductModel.PRODUCT_NAME, TestProductModel.PRODUCT_PRICE
        )

    def test_initializer(self):
        self.assertEqual(self.instance.name, TestProductModel.PRODUCT_NAME)
        self.assertEqual(self.instance.price, TestProductModel.PRODUCT_PRICE)

    def test_str(self):
        self.assertEqual(str(self.instance), TestProductModel.PRODUCT_NAME)

    def test_get_total(self):
        quantity = 0.500
        test_value = round(TestProductModel.PRODUCT_PRICE * quantity, 2)
        self.assertEqual(self.instance.get_total(quantity), test_value)

    def test_equal(self):
        another = models.Product(
            TestProductModel.PRODUCT_NAME, TestProductModel.PRODUCT_PRICE
        )
        self.assertEqual(self.instance, another)

    def test_equal_raises(self):
        self.assertRaises(
            TypeError, self.instance.__eq__, TestProductModel.PRODUCT_NAME
        )


class TestShoppingCartModel(unittest.TestCase):
    APPLE = models.Product("apple", 24.5), 1.5
    BEER = models.Product("beer", 32.0), 2
    CHEESE = models.Product("cheese", 128.45), 0.500

    def setUp(self) -> None:
        self.instance = models.ShoppingCart()
        self.instance.add_product(*TestShoppingCartModel.APPLE)
        self.instance.add_product(*TestShoppingCartModel.BEER)
        self.instance.add_product(*TestShoppingCartModel.CHEESE)

    def test_str(self):
        test_value = "apple x 1.5\nbeer x 2\ncheese x 0.5"
        self.assertEqual(str(self.instance), test_value)

    def test_add_product(self):
        product = models.Product("foobar", 42)
        quantity = 4.2
        self.instance.add_product(product, quantity)
        self.assertEqual(len(self.instance.products), 4)
        self.assertEqual(len(self.instance.quantities), 4)
        self.assertEqual(self.instance.products[-1], product)
        self.assertEqual(self.instance.quantities[-1], quantity)

    def test_add_product_existing(self):
        product = models.Product("apple", 24.5)
        quantity = 1.5
        self.instance.add_product(product, quantity)
        self.assertEqual(len(self.instance.products), 3)
        self.assertEqual(len(self.instance.quantities), 3)
        self.assertEqual(self.instance.quantities[0], 3)

    def test_get_total(self):
        test_value = 164.97
        self.assertEqual(self.instance.get_total(), test_value)
