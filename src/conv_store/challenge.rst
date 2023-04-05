###############################################################################
                          Convenience Store Challenge
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
    * ``price`` - a price for a single product unit (e.g. 3655, 500, 12999)
    * ``unit`` - a size of a single product's unit (e.g. 1, 0.500, 12)

#.  ``Product`` class should implement ``get_total`` method to calculate
    a total price for a specified quantity of a product. Desired quantity
    will be passed as an optional argument of a numeric type (``int`` or
    ``float``). The returned value is the multiplication result for
    price and quantity values. In case quantity argument is omitted -
    just use ``unit`` attribute instead.

.. rubric:: Test Cases

.. code-block:: python

    product_obj = Product()
    product_obj.name = "candy"
    product_obj.price = 1059
    product_obj.unit = 0.1

    assert product_obj.get_total(0.7) == 7413
    assert product_obj.get_total() == 1059

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

.. rubric:: Test Cases

.. code-block:: python

    product_obj = Product()
    product_obj.name = "juice"
    product_obj.price = 3655
    product_obj.unit = 1
    cart_obj = ShoppingCart()
    cart_obj.add_product(product_obj, 3)  # put 3 packs of juice to cart
    cart_obj.add_product(product_obj)     # add one more (unit = 1)

    assert cart_obj.get_total() == 14620  # 3655 x 4

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
#.  While casting shopping cart instance to ``float`` type it should be equal
    to its total price value.
#.  While casting shopping cart instance to ``bool`` consider it ``True`` if
    at least one product is attach to current cart.

#.  Implement equality operator support for your objects:

    * consider products equal if all their properties are the same
    * consider carts equal if products and corresponding quantities are
      the same

.. rubric:: Test Cases

.. code-block:: python

    candy = Product("candy", 1059, 0.1)
    sweet = Product("candy", 1059, 0.1)
    juice = Product("juice", 3655, 1)
    cart_1 = ShoppingCart()
    cart_2 = ShoppingCart()
    cart_1.add_product(candy, 1)
    cart_1.add_product(sweet, 0.5)
    cart_2.add_product(juice)

    assert cart_1.get_total() == 15885
    assert str(candy) == "candy"
    assert float(candy) == 10.59
    assert float(cart_2) == 36.55
    assert candy == sweet
    assert sweet != juice
    assert cart

******************
Payment Processors
******************

The owner asked you to implement a flexible payment system.
Purchasing the shopping card consists of several steps:

- cart validation - it should not be empty or already purchased
- payment validation - various payment types requires various validations
- purchasing the cart

For now there are two payment types available in the store: cash and credit
card, but they maybe extended at any time.

#.  Update the ``ShoppingCart`` class to handle ``purchased`` state. Make this
    property *protected*, since it should not be accessed outside the card
    instance.
#.  Implement ``PaymentValidator`` class with ``is_valid`` that takes
    no arguments and return a value of a boolean type. This is an abstract
    class for the future usage.
#.  Implement ``PaymentProcessor`` class with ``purchase`` method that takes
    a ``ShoppingCart`` object and returns nothing. This is an abstract class
    for the future usage.
#.  Inherit ``CashPaymentValidator`` from the base validator.
    The instances of this class are considered to be always valid.
#.  Inherit ``CodeValidator`` from the base validator.

    - The instances of this class are created with ``security_code`` argument.
    - ``is_valid`` method should ask a customer for a security code and check
      it against the stored value. In case codes are equal payment considered
      to be valid.

#.  Create ``CashPaymentProcessor`` that combines ``CashValidator`` and
    ``PaymentProcessor`` behaviors. While purchasing the cart the messages
    "Processing cash payment..." and "Cart bill: {float total}" should be
    printed out.

#.  Create ``CardPaymentProcessor`` that combines ``CodeValidator`` and
    ``PaymentProcessor`` behaviors. While purchasing the cart the messages
    "Processing card payment..." and "Security code: {code}" should be
    printed out.

.. rubric:: Test Cases

.. code-block:: python

    cart = ShoppingCart()
    cart.add_product(Product("juice", 3655, 1), 1)

    cash_processor = CashPaymentProcessor()
    cash_processor.purchase(cart)  # Cart bill: 36.55

    card_processor = CardPaymentProcessor("1234")
    card_processor.purchase(cart)  # Security code: 1234

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

.. rubric:: Test Cases

.. code-block:: python

    candy = Product("candy", 1059, 0.1)
    sweet = Product("candy", 1059, 0.1)
    juice = Product("juice", 3655, 1)
    cart = ShoppingCart()
    cart.add_product(candy, 0.75)
    cart.add_product(sweet, 0.75)
    cart.add_product(juice, 3)

    assert len(cart) == 2
    assert cart[0] == candy, 1.5  # this may use other value as key
    for cart_item, purchase in zip(cart, ((candy, 1.5), (juice, 3))):
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
