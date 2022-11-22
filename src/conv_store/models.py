"""
Convenience Store Models

"""

from typing import Iterator, List, Union


class Product:
    """Product model implementation

    :ivar name: product name
    :type name: str
    :ivar price: price for a single unit of a product
    :type price: float

    """

    def __init__(self, name: str, price: float) -> None:
        """Initialize instance"""

        self.name = name
        self.price = price

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"Product('{self.name}', {self.price})"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name

    def __eq__(self, other) -> bool:
        """Return equality comparison result"""

        if not isinstance(other, Product):
            err_message = (f"unsupported operation for ==: "
                           f"{self.__class__.__name__} and "
                           f"{other.__class__.__name__}")
            raise TypeError(err_message)

        return self.name == other.name and self.price == other.price

    def get_total(self, quantity: Union[int, float]) -> float:
        """Return price for a specified amount of a product

        :param quantity: amount to calculate price for
        :type quantity: int or float

        :return: calculated price for the specified amount of product
        :rtype: float

        """

        return round(self.price * quantity, 2)


class ShoppingCart:
    """Shopping cart model implementation

    :ivar products: list of products in cart
    :type products: list[:class: `Product`]
    :ivar quantities: corresponding quantity value for each product
    :type quantities: list[Union[int, float]]

    """

    def __init__(self) -> None:
        """Initialize instance"""

        self.products: List[Product] = []
        self.quantities: List[Union[int, float]] = []

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return "<ShoppingCart>"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return "\n".join(
            [
                f"{product} x {quantity}" for product, quantity in self
            ]
        )

    def __iter__(self) -> Iterator:
        """Return a shopping cart iterator object"""

        return zip(self.products, self.quantities)

    def add_product(
            self, product: Product, quantity: Union[int, float]
    ) -> None:
        """Add product to a shopping cart"""

        try:
            idx = self.products.index(product)
            self.quantities[idx] += quantity
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

    def get_total(self) -> float:
        """Return a total price for an instance"""

        total = 0.0
        for product, quantity in self:
            total += product.get_total(quantity)

        return total
