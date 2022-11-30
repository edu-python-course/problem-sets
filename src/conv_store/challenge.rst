###############################################################################
                          CONVENIENCE STORE CHALLENGE
###############################################################################

The local store is struggling with their payment registry system. The owner
asked you to take a look at it and to propose some ideas about the upgrade.
While looking on a wooden frames with rows of beads you think that this will
be a challenging task to bring a modern approach into this place and reorganize
the processes. Fortunately, you are a Python developer who knows how to work
with various data incomes and outcomes. After some time the scope of works and
timelines were discussed and wrote some notes to split the entire project into
individual pieces to implement step-by-step.

Your notes are here,

******************
Products and Carts
******************

It's a good idea to with basics - the objects you're going to work with. At
stage one the main goal is to implement data models - classes to work around
data in the future.

Product
=======

This class represents goods available to purchase in the store.

#.  Each product instance should have next attributes:

    * ``name`` - a product title (e.g. "apple", "juice")
    * ``price`` - a price for a single product unit (e.g. 36.55)
    * ``unit`` - a size of a single product's unit (e.g. 1, 0.500, 12)

#.  ``Product`` class should implement ``get_total`` method to calculate
    price for a specified quantity of a product. Quantity arguments is
    something you can think about as "total number of product's units".
    It is of a numeric type (``int`` or ``float``) and it may be omitted.
    In case argument hasn't been passed just consider it is equal to unit
    attribute value.

**Test cases**

.. code-block:: python

    product_obj = Product()
    product_obj.name = "candy"
    product_obj.price = 10.59
    product_obj.unit = 0.1

    assert product_obj.get_total(0.7) == 74.13

Shopping Cart
=============

This class represents the container for the products. It's main responsibility
is to store information about the purchases and their amount (quantities).

#.  Each cart instance should store data about ``Product`` objects in it and
    corresponding quantity value for each individual product.
#.  ``ShoppingCart`` should implement ``add_product`` method to put a specified
    quantity into a cart. ``quantity`` argument is optional, if omitted just
    uses ``Product.unit`` value instead.
#.  ``ShoppingCart`` should implement ``get_total`` method to calculate the
    total price for the entire cart contents.

**Test cases**

.. code-block:: python

    product_obj = Product()
    product_obj.name = "juice"
    product_obj.price = 36.55
    product_obj.unit = 1
    cart_obj = ShoppingCart()
    cart_obj.add_product(product_obj, 3)  # put 3 packs of juice to cart
    cart_obj.add_product(product_obj)     # add one more (unit = 1)

    assert cart_obj.get_total() == 146.2  # 36.55 x 4

***********************************************
Initialization, Representation and Type Casting
***********************************************

It's difficult to set properties one-by-one, also it's not informative to get
default objects string representations. It's time to fix this.

#.  ``Product`` should be initialized with all required data, no defaults.
#.  Apply ``ShoppingCart.__init__`` to separate products and quantities
    between different carts.
#.  Provide a human readable representations. For example:

    * ``Product('juice', 35.66, 1)``
    * ``<ShoppingCart>``

#.  While casting product instance to ``str`` type it should be equal to its
    ``name`` attribute value.
#.  While casting product instance to ``float`` type it should be equal to its
    ``price`` attribute value.
#.  While casting product instance to ``float`` type it should be equal to its
    total price value.
#.  While casting shopping cart instance to ``bool`` consider it ``True`` if
    at least one product is attach to current cart.

#.  Implement equality operator support for your objects

    * consider products equal if all their properties are the same
    * consider carts equal if products and corresponding quantities are
      the same

**Test cases**

.. code-block:: python

    candy = Product("candy", 10.59, 0.1)
    sweet = Product("candy", 10.59, 0.1)
    juice = Product("juice", 36.55, 1)
    cart_1 = ShoppingCart()
    cart_2 = ShoppingCart()
    cart_1.add_product(candy, 1)
    cart_1.add_product(sweet, 0.5)
    cart_2.add_product(juice)

    assert cart_1.get_total() == 158.85
    assert str(candy) == "candy"
    assert float(candy) == 10.59
    assert float(cart_2) == 36.55
    assert candy == sweet
    assert sweet != juice
    assert cart

************************************
More Enhancements for Shopping Carts
************************************

#.  Make your ``ShoppingCart`` an actual container

    * Implement ``len(cart_obj)`` and make it return the number of products
      in the cart.
    * Implement ``cart[...]`` behavior to take a ``tuple`` containing product
      and corresponding quantity
      (type hint: ``Tuple[Product, Union[int, float]]``).

#.  Make your ``ShoppingCart`` iterable - let it provide the product instance
    and corresponding quantity for each iteration.
#.  Avoid products duplication. In case someone tries to put the product into
    a cart and this product already is present there, do not it for the second
    time - adjust corresponding quantity value instead.
#.  Implement ``remove_product`` method to completely remove some product from
    the cart.
#.  Implement ``sub_product`` to decrease some product quantity. If quantity
    is equal to 0 (zero) or less - remove product from the cart.

**Test cases**

.. code-block:: python

    candy = Product("candy", 10.59, 0.1)
    sweet = Product("candy", 10.59, 0.1)
    juice = Product("juice", 36.55, 1)
    cart = ShoppingCart()
    cart.add_product(candy, 0.75)
    cart.add_product(sweet, 0.75)
    cart.add_product(juice, 3)

    assert len(cart) == 2
    assert cart[0] == candy, 0.7  # this may use other value as key
    for cart_item, purchase in zip(cart, ((candy, 0.7), (juice, 3))):
        assert cart_item == purchase

    cart.remove_product(candy)
    assert len(cart) == 1
    cart.sub_product(juice, 2)
    assert cart[0][1] == 2
    cart.sub_product(juice, 2)
    assert not cart

****************
Testing Software
****************

Add autotests for ``ShoppingCart`` and ``Product`` models.

#.  Tests should be located inside of "tests" directory.
#.  ``pytest`` and ``coverage`` libraries will be used for testing.
#.  At least 50% coverage.
#.  Project dependencies are to be updated.