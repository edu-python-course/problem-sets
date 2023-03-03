import unittest

from conv_store import models


class TestProductModel(unittest.TestCase):

    def setUp(self) -> None:
        self.product_name = "candy"
        self.product_price = 1059
        self.product_unit = 0.1
        self.instance = models.Product(
            self.product_name, self.product_price, self.product_unit
        )

    def test_initializer(self):
        self.assertEqual(self.product_name, self.instance.name)
        self.assertEqual(self.product_price, self.instance.price)
        self.assertEqual(self.product_unit, self.instance.unit)

    def test_str(self):
        self.assertEqual(self.product_name, str(self.instance))

    def test_repr(self):
        values = self.product_name, self.product_price, self.product_unit
        test_value = "Product('%s', %d, %s)" % values
        self.assertEqual(repr(self.instance), test_value)

    def test_float(self):
        self.assertEqual(self.product_price / 100, float(self.instance))

    def test_equal(self):
        another = models.Product("candy", 1059, 0.1)
        self.assertEqual(self.instance, another)

    def test_not_equal(self):
        another = models.Product("juice", 3655, 1)
        self.assertNotEqual(self.instance, another)
        another = models.Product("candy", 3655, 1)
        self.assertNotEqual(self.instance, another)
        another = models.Product("candy", 1059, 1)
        self.assertNotEqual(self.instance, another)
        self.assertNotEqual(self.instance, "candy")
        self.assertNotEqual(self.instance, 10.59)

    def test_get_total(self):
        self.assertEqual(7413, self.instance.get_total(0.7))

    def test_get_units(self):
        self.assertEqual(7, self.instance.get_units(0.7))


class TestShoppingCartModel(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = models.ShoppingCart()
        candy = models.Product("candy", 1059, 0.1)
        juice = models.Product("juice", 3655, 1)
        self.products = [candy, juice]
        self.quantities = [0.7, 4]
        self.instance.add_product(candy, 0.7)
        self.instance.add_product(juice, 4)

    def test_products(self):
        self.assertListEqual(self.products, self.instance.products)
        self.assertListEqual(self.quantities, self.instance.quantities)

    def test_remove_product(self):
        candy = models.Product("candy", 1059, 0.1)
        returned_value = self.instance.remove_product(candy)
        self.assertEqual((candy, 0.7), returned_value)
        self.assertNotIn(candy, self.instance.products)
        self.assertEqual(len(self.instance.products), 1)
        self.assertEqual(len(self.instance.quantities), 1)

    def test_remove_product_raises(self):
        spice = models.Product("spice", 12025, 0.1)
        self.assertRaises(ValueError, self.instance.remove_product, spice)
        self.assertEqual(2, len(self.instance.products))
        self.assertEqual(2, len(self.instance.quantities))

    def test_add_product(self):
        spice = models.Product("spice", 12025, 0.1)
        self.instance.add_product(spice)
        self.assertListEqual(self.products + [spice], self.instance.products)
        self.assertListEqual(self.quantities + [.1], self.instance.quantities)

    def test_add_existing_product(self):
        # avoid existing objects usage
        candy = models.Product("candy", 1059, 0.1)
        juice = models.Product("juice", 3655, 1)
        quantities = [self.quantities[0] + 1.5, self.quantities[1] + 2]

        self.instance.add_product(candy, 1.5)
        self.instance.add_product(juice, 2)
        self.assertListEqual(self.products, self.instance.products)
        self.assertListEqual(quantities, self.instance.quantities)

    def test_sub_product(self):
        juice = models.Product("juice", 3655, 1)
        self.instance.sub_product(juice, 2)
        self.assertEqual(self.instance.quantities[1], 2)

    def test_sub_product_removes(self):
        juice = models.Product("juice", 3655, 1)
        self.instance.sub_product(juice, 5)
        self.assertNotIn(juice, self.instance.products)
        self.assertEqual(len(self.instance.products), 1)
        self.assertEqual(len(self.instance.quantities), 1)

    def test_get_total(self):
        self.assertEqual(22033, self.instance.get_total())

    def test_empty(self):
        self.assertTrue(self.instance)
        self.assertFalse(models.ShoppingCart())

    def test_len(self):
        self.assertEqual(len(self.instance), 2)

    def test_get_item(self):
        test_value = models.Product("juice", 3655, 1), 4
        self.assertTupleEqual(self.instance[1], test_value)

    def test_contains(self):
        juice = models.Product("juice", 3655, 1)
        eggs = models.Product("eggs", 6500, 10)
        self.assertIn(juice, self.instance)
        self.assertNotIn(eggs, self.instance)

    def test_iteration(self):
        test_values = zip(self.products, self.quantities)
        for test_value, cart_item in zip(test_values, self.instance):
            self.assertTupleEqual(test_value, cart_item)
