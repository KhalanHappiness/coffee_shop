from models.Customer import Customer
from models.Coffee import Coffee
from models.Order import Order

# Create some Coffee objects
latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")

# Create some Customer objects
alice = Customer("Alice")
bob = Customer("Bob")
charlie = Customer("Charlie")

# Create some orders
alice.create_order(latte, 4.50)
alice.create_order(espresso, 3.00)
bob.create_order(latte, 5.00) # Bob ordered Latte at a different price
bob.create_order(latte, 5.50)
charlie.create_order(espresso, 3.50)
charlie.create_order(latte, 6.00)

# Print results
print([c.name for c in latte.customers()])  # ['Alice', 'Bob']
print([cf.name for cf in alice.coffees()])
print(latte.num_orders())
print(latte.average_price())
print(Customer.most_aficionado(cappuccino).name)