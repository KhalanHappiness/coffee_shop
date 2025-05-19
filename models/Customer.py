

class Customer:

    def __init__(self, name):
    
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1<= len(value) <= 15:
            
           self._name =value

        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters")
        
    
    def orders(self):
        from models.Order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        from models.Order import Order
        return [order.coffee for order in Order.all if order.customer == self]
    
    def create_order(self, coffee, price):
        from models.Order import Order

        order = Order(customer=self, coffee= coffee, price = price)
        self.orders.append(order)

        return order

        
