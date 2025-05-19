
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
    
