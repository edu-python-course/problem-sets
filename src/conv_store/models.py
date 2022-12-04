"""
Convenience store models

"""

from typing import Iterator, List, Optional, Tuple, Union


class Product:
    """Product model implementation

    Instances of this class represent a product available for purchase.

    :ivar name: the name of a product
    :type name: str
    :ivar price: the price for a single product unit
    :type price: float
    :ivar unit: the size of a single product unit
    :type unit: int or float

    """

    def __init__(
        self, name: str, price: float, unit: Union[int, float]
    ) -> None:
        """Initialize instance

        :param name: product name
        :type name: str
        :param price: product price
        :type price: float
        :param unit: product unit size
        :type unit: int or float

        """

        self.name = name
        self.price = price
        self.unit = unit

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"Product('{self.name}', {self.price:.2f}, {self.unit})"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name

    def __float__(self) -> float:
        """Cast product instance to float type"""

        return self.price

    def __eq__(self, other: object) -> bool:
        """Return equality comparing result (self == other)"""

        if not isinstance(other, Product):
            return False

        return (
            self.name == other.name and
            self.price == other.price and
            self.unit == other.unit
        )

    def get_total(self, quantity: Union[int, float]) -> float:
        """Return the total price for a specified amount of product"""

        return round(self.price * quantity / self.unit, 2)


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

    def __init__(self) -> None:
        """Initialize instance"""

        self.products: List[Product] = []
        self.quantities: List[Union[int, float]] = []

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return "<ShoppingCart>"

    def __bool__(self) -> bool:
        """Cast to bool type"""

        return bool(self.products)

    def __len__(self) -> int:
        """Return a number of products in the shopping cart"""

        return len(self.products)

    def __getitem__(self, idx: int) -> Tuple[Product, Union[int, float]]:
        """Return a product - quantity pair"""

        return self.products[idx], self.quantities[idx]

    def __contains__(self, item) -> bool:
        """Return True if item is present in the shopping cart"""

        return item in self.products

    def __iter__(self) -> Iterator:
        """Return shopping cart iterator"""

        return zip(self.products, self.quantities)

    def remove_product(self, product: Product) -> None:
        """Remove product from a cart instance


        :param product: a product instance to add to cart
        :type product: :class: `Product`

        """

        if product in self.products:
            idx = self.products.index(product)
            self.products.pop(idx)
            self.quantities.pop(idx)

    def add_product(
        self, product: Product,
        quantity: Optional[Union[int, float]] = None
    ) -> None:
        """Add product to the shopping cart

        :param product: a product instance to add to cart
        :type product: :class: `Product`
        :param quantity: a quantity of a product to add
        :type quantity: int or float

        """

        quantity = quantity or product.unit

        if product in self.products:
            idx = self.products.index(product)
            self.quantities[idx] += quantity

        else:
            self.products.append(product)
            self.quantities.append(quantity)

        idx = self.products.index(product)
        if self.quantities[idx] <= 0:
            self.remove_product(product)

    def sub_product(
        self, product: Product, quantity: Union[int, float]
    ) -> None:
        """Subtract product from the shopping cart

        If quantity value is less or equal to 0 the product is to be
        removed from the shopping cart


        :param product: a product instance to add to cart
        :type product: :class: `Product`
        :param quantity: a quantity of a product to add
        :type quantity: int or float

        """

        quantity = - abs(quantity)
        return self.add_product(product, quantity)

    def get_total(self) -> float:
        """Return the total price for all the product in the cart

        :return: total cart price
        :rtype: float

        """

        total = 0.0
        for product, quantity in zip(self.products, self.quantities):
            total += product.get_total(quantity)

        return round(total, 2)
