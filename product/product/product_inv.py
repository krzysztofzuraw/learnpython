"""An application which manages an inventory of products. """

class Product(object):
    """Store information about products."""
    def __init__(self, ids, price, name, quantity):
        """
        Args:
          ids(int): identification number
          price(int): how much does products cost
          name(str): name of product
          quantity(int): how much products you have
        """
        self._ids = ids
        self._price = price
        self._name = name
        self._quantity = quantity
        
    @property
    def ids(self):
        return self._ids
    @property
    def price(self):
        return self._price
    @property
    def name(self):
        return self._name
    @property
    def quanitity(self):
        return self._quantity
    @price.setter
    def price(self, other):
        self._price = other
    @quanitity.setter
    def quantity(self, other):
        self._quantity = other
        
    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self._ids)
        
    def __str__(self):
        return "{name} with {price} price and {quantity} quanitity".format(
                name=self._name, price=self._price, quantity=self._quantity)
                

class Inventory(object):
    """Keeps track of products"""
    def __init__(self):
        self._products = {}
    
    @property
    def products(self):
        return self._products
                
    def add_product(self, prod):
        """Adding product to inventory
        Args:
          prod(class): product class to be added
        """
        self._products[prod.ids] = [prod.name]
        self._products[prod.ids].append(prod.price)
        self._products[prod.ids].append(prod.quantity)

    def sum_price(self):
        """Returns:
        Sum price of all products in inventory"""
        return sum([x[1] for x in list(self._products.values())])
        
    def sum_quantity(self):
        """Returns:
        Sum of products quantity in inventory"""
        return sum([x[2] for x in list(self._products.values())])
       
    def sum_products(self):
        """Returns: 
        Number of products in inventory """
        return len(self._products.keys())

                                
