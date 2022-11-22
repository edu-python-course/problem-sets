"""
Convenience Store Challenge
===========================

Product
-------

The ``Product`` instance represents a single product anyone can purchase
in the convenience store (e.g. apple, banana etc.). This contains all
required information, such as product's name and price.

.. autoclass:: Product
    :members: __init__, __str__, get_total

Shopping Cart
-------------

In general, this is a container for products.

.. autoclass:: ShoppingCart
    :members: add_product, get_total

"""

from .models import Product, ShoppingCart

__all__ = ["Product", "ShoppingCart"]
