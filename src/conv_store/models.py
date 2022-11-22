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
            err_message = (f"unsupported operand types for ==: "
                           f"'{self.__class__.__name__}' and "
                           f"'{other.__class__.__name__}'")
            raise TypeError(err_message)

        return self.name == other.name and self.price == other.price

    def get_total(self, quantity: Union[int, float]) -> float:
        """Return price for a specified amount of a product

        .. note:: the floating numbers are not very precision, consider
                  two decimal digits quite enough.

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

    def __add__(self, other):
        """Return a combined shopping cart"""

        if not isinstance(other, ShoppingCart):
            err_message = (f"unsupported operand types for +: "
                           f"{self.__class__.__name__} and "
                           f"{other.__class__.__name__}")
            raise TypeError(err_message)

        products = self.products + other.products
        quantities = self.quantities + other.quantities

        return self.create_from_lists(products, quantities)

    @classmethod
    def create_from_lists(
            cls, products: List[Product], quantities: List[Union[int, float]]
    ):
        """Return a shopping cart instance

        :param products: products list
        :type products: list[:class: `Product`]
        :param quantities: corresponding quantities list
        :type quantities: list[Union[int, float]]

        :return: a shopping cart instance
        :rtype: :class: `ShoppingCart`

        """

        instance = cls()
        for product, quantity in zip(products, quantities):
            instance.add_product(product, quantity)

        return instance

    def add_product(
            self, product: Product, quantity: Union[int, float]
    ) -> None:
        """Add product to a shopping cart

        In case the product instance is already in the shopping cart,
        this method just updates the quantity value without adjusting
        products list itself.

        :param product: a product instance to add
        :type product: :class: `Product`
        :param quantity: a quantity of a product instance to add
        :type quantity: int or float

        """

        try:
            idx = self.products.index(product)
            self.quantities[idx] += quantity
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

    def get_total(self) -> float:
        """Return a total price for an instance

        :return: calculated price for all the cart's content
        :rtype: float

        """

        total = 0.0
        for product, quantity in self:
            total += product.get_total(quantity)

        return total
