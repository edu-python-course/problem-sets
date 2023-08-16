"""
Convenience store models

"""

from typing import Iterator, List, Optional, Tuple, Union


class Product:
    """
    Product model implementation

    :ivar name: the name of a product
    :type name: str
    :ivar price: the price for a single product unit
    :type price: int
    :ivar unit: the size of a single product unit
    :type unit: int | float

    Instances of this class represent a product available for purchase.

    """

    def __init__(self,
                 name: str,
                 price: int,
                 unit: Union[int, float]
                 ) -> None:
        """
        Initialize instance

        :param name: product name
        :type name: str
        :param price: product price
        :type price: int
        :param unit: product unit size
        :type unit: int | float

        """

        self.name = name
        self.price = price
        self.unit = unit

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"Product('{self.name}', {self.price}, {self.unit})"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name

    def __int__(self) -> int:
        """Cast product instance to integer type"""

        return self.price

    def __float__(self) -> float:
        """Cast product instance to float type"""

        return self.price / 100

    def __eq__(self, other: object) -> bool:
        """Return equality comparing result (self == other)"""

        if not isinstance(other, Product):
            return False

        return (
            self.name == other.name and
            self.price == other.price and
            self.unit == other.unit
        )

    def get_total(self, quantity: Optional[Union[int, float]] = None) -> int:
        """
        Return the total price for a specified amount of a product

        :param quantity: a quantity to purchase, defaults to None
        :type quantity: int | float, optional

        :return: total price for a specified amount of a product
        :rtype: int

        If the quantity argument is omitted, unit attribute value should be
        used instead.

        """

        quantity = quantity or self.unit
        total_price = round(self.price * quantity / self.unit, 0)

        return int(total_price)

    def get_units(self, quantity: Union[int, float]) -> int:
        """Return the number of units for a specified amount of a product"""

        return int(round(quantity / self.unit))


class ShoppingCart:
    """Shopping cart model implementation

    :ivar products: product appended to the shopping cart instance
    :type products: list
    :ivar quantities: corresponding quantities for each product in cart
    :type quantities: list

    In general shopping cart is a container for products. Instances of this
    class handle product and corresponding quantity for each item inside
    a shopping cart instance.

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

    def __float__(self) -> float:
        """Cast to float type"""

        return self.get_total() / 100

    def __len__(self) -> int:
        """Return a number of products in the shopping cart"""

        return len(self.products)

    size_of = __len__

    def __getitem__(self, idx: int) -> Tuple[Product, Union[int, float]]:
        """Return a product - quantity pair"""

        return self.products[idx], self.quantities[idx]

    def __contains__(self, item: object) -> bool:
        """Return True if item is present in the shopping cart"""

        return item in self.products

    def __iter__(self) -> Iterator[Tuple[Product, Union[int, float]]]:
        """Return shopping cart iterator"""

        return zip(self.products, self.quantities)

    def remove_product(self,
                       product: Product
                       ) -> Tuple[Product, Union[int, float]]:
        """
        Remove product from a cart instance

        :param product: a product instance to add to cart
        :type product: :class: `Product`

        :return: a shopping cart product/quantity entry
        :rtype: tuple

        :raise ValueError: if the project isn't present in the shopping cart

        """

        idx = self.products.index(product)
        product = self.products.pop(idx)
        quantity = self.quantities.pop(idx)

        return product, quantity

    pop = remove_product

    def add_product(self,
                    product: Product,
                    quantity: Optional[Union[int, float]] = None
                    ) -> None:
        """
        Add product to the shopping cart

        :param product: a product instance to add to cart
        :type product: :class: `Product`
        :param quantity: a quantity of a product to add. Defaults to the
            product unit value.
        :type quantity: int | float, optional

        This method adds a product instance and corresponding quantity value
        to the cart.

        """

        quantity = quantity or product.unit

        try:
            idx = self.products.index(product)
            self.quantities[idx] += quantity
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

        idx = self.products.index(product)
        if self.quantities[idx] <= 0:
            self.remove_product(product)

    add = add_product

    def sub_product(self,
                    product: Product,
                    quantity: Union[int, float]
                    ) -> None:
        """
        Subtract product from the shopping cart

        :param product: a product instance to add to cart
        :type product: :class: `Product`
        :param quantity: a quantity of a product to add
        :type quantity: int | float

        If quantity value is less or equal to 0 the product is to be
        removed from the shopping cart

        """

        quantity = - abs(quantity)
        return self.add_product(product, quantity)

    def get_total(self) -> int:
        """
        Return the total price for all the product in the cart

        :return: total cart price
        :rtype: int

        """

        total = 0
        for product, quantity in self:
            total += product.get_total(quantity)

        return total
