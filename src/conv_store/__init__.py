"""
Convenience Store Challenge
===========================

As a software developer you're asked to create a simple goods and purchase
register for a small convenience store in your local area.

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

__all__ = ["Product", "ShoppingCart"]

from conv_store.models import Product, ShoppingCart
