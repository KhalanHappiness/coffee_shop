from Models.Customer import Customer
from Models.Coffee import Coffee


class Order:

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        self.customer =customer
        pass
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        self.coffee = coffee
        pass
        if not isinstance(price, float) and (price >= 1.0 and price <= 10.0):
            raise TypeError("price must be a float bwtween 1.0 and 10.0")
        self.price = price
       
    pass