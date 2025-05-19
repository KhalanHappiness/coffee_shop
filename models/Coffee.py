
class Coffee:

    all = []
    

    def __init__(self, name):
    
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if  isinstance(value, str) and len(value.strip()) >=3:
           
           self._name =value

        else: 
             raise TypeError("Coffee name must be a string with at least 3 characters")
    
    def orders(self):
        from models.Order import Order
        return [orders for orders in Order.all if orders.coffee == self ]
    
    def customers(self):
        from models.Order import Order
        return [orders.customer for orders in Order.all if orders.coffee == self]
    
    def num_orders(self):
        return f"{self.name} has been ordered {len(self.orders())} times"
    
    def average_price(self):

        if not self.orders():
            return 0
        Average = sum ([order.price for order in self.orders()])/ len(self.orders())

        return f'The average price of {self.name} is {Average}'


        

    
