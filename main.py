from models.Customer import Customer
from models.Coffee import Coffee
from models.Order import Order

# Create instances
cust1 = Customer("Alice")
cust2 = Customer("Bob")
coffee1 = Coffee("Latte")

# Create orders
order1 = Order(cust1, coffee1, 4.5)
order2 = Order(cust2, coffee1, 5.0)

# Print results
print([c.name for c in coffee1.customers()])  # ['Alice', 'Bob']