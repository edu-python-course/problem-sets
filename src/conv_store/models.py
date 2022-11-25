"""
Convenience store models

"""

from typing import Union


class Product:
    """Product model implementation

    Instances of this class represent a product available for purchase.

    :ivar name: the name of a product
    :type name: str
    :ivar price: the price for a single product unit
    :type price: float

    """

    def __init__(self, name: str, price: float) -> None:
        """Initialize instance

        :param name: product name
        :type name: str
        :param price: product price
        :type price: float

        """

        ...

    def get_total(self, quantity: Union[int, float]) -> float:
        """Return the total price for a specified amount of product"""

        ...


class ShoppingCart:
    """Shopping cart model implementation

    In general shopping cart is a container for products. Instances of this
    class handle product and corresponding quantity for each item inside
    a shopping cart instance.

    :ivar products: product appended to the shopping cart instance
    :type products: list[product]
    :ivar quantities: corresponding quantities for each product in cart
    :type quantities: list[int or float]

    """

    def add_product(
        self, product: Product, quantity: Union[int, float]
    ) -> None:
        """Add product to the shopping cart

        :param product: a product instance to add to cart
        :type product: :class: `Product`
        :param quantity: a quantity of a product to add
        :type quantity: int or float

        """

        ...

    def get_total(self) -> float:
        """Return the total price for all the product in the cart

        :return: total cart price
        :rtype: float

        """

        ...
