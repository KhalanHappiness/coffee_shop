

class Customer:

    all = []

    def __init__(self, name):
    
        self.name = name
        Customer.all.append(self)

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

        return order
    
    def total_spent_on_coffee(self, coffee):
        total =0
        for order in self.orders():
            if order.coffee == coffee:
                total += order.price
        return total

    @classmethod
    def most_aficionado(cls, coffee):
        most_spent = 0
        aficionado = None
#validate, make sure it is  an object of the coffee instance
        for customer in cls.all:
            spent = customer.total_spent_on_coffee(coffee)
            if spent > most_spent:
                most_spent = spent
                aficionado = customer
        return aficionado





        
