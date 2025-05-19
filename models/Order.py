from models.Customer import Customer
from models.Coffee import Coffee


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
       
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):

        if not isinstance(value, Customer):
            raise TypeError("customer must be an instance of Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):

        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        self._coffee = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):

        if not isinstance(value,  float )or not (1.0<= value <= 10.0):
            raise TypeError("price must be a float between 1.0 and 10.0")
        self._price = value