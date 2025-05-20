from models.Customer import Customer
from models.Coffee import Coffee
from models.Order import Order

def debug():
    """
    This function demonstrates how to use the Customer, Coffee, and Order classes
    and prints information to help with debugging.
    """
    print("--- Creating Coffee Objects ---")
    try:
        # Correct Coffee names
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        coffee3 = Coffee("Cappuccino")
        print(f"Created coffees: {coffee1.name}, {coffee2.name}, {coffee3.name}")
    except TypeError as e:
        print(f"Error creating coffee: {e}")
        return  # Stop if there's an error with Coffee

    print("\n--- Creating Customer Objects ---")
    try:
        # Correct Customer names
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        customer3 = Customer("Charlie")
        print(f"Created customers: {customer1.name}, {customer2.name}, {customer3.name}")
    except ValueError as e:
        print(f"Error creating customer: {e}")
        return  # Stop if there's an error with Customer

    print("\n--- Creating Order Objects ---")
    try:
        # Correct order prices
        order1 = Order(customer1, coffee1, 4.50)
        order2 = Order(customer1, coffee2, 3.00)
        order3 = Order(customer2, coffee1, 5.00)
        order4 = Order(customer3, coffee2, 3.50)
        order5 = Order(customer3, coffee3, 6.00)
        print(f"Created orders for {customer1.name}, {customer2.name}, and {customer3.name}")
    except TypeError as e:
        print(f"Error creating order: {e}")
        return  # Stop if there's an error with Order

    print("\n---  Testing Relationships and Methods ---")
    print("\n--- Customer Class ---")
    print(f"{customer1.name}'s orders: {[order.coffee.name for order in customer1.orders()]}")  # Use a list comprehension
    print(f"{customer1.name}'s coffees: {[coffee.name for coffee in customer1.coffees()]}") # Use a list comprehension
    print(f"Total spent by {customer1.name} on {coffee1.name}: {customer1.total_spent_on_coffee(coffee1)}")
    print(f"Most aficionado of {coffee1.name}: {Customer.most_aficionado(coffee1).name if Customer.most_aficionado(coffee1) else 'No one'}")

    print("\n--- Coffee Class ---")
    print(f"{coffee1.name}'s orders: {[order.customer.name for order in coffee1.orders()]}") # Use a list comprehension
    print(f"{coffee1.name}'s customers: {[customer.name for customer in coffee1.customers()]}") # Use a list comprehension
    print(coffee1.num_orders())
    print(coffee1.average_price())

    print("\n--- Order Class ---")
    print(f"Order 1 details - Customer: {order1.customer.name}, Coffee: {order1.coffee.name}, Price: {order1.price}")

    print("\n---Demonstrate edge cases ---")
    print("\n---Coffee with no orders---")
    coffee4 = Coffee("Mocha")
    print(coffee4.num_orders())
    print(coffee4.average_price())
    print(f"Most aficionado of {coffee4.name}: {Customer.most_aficionado(coffee4).name if Customer.most_aficionado(coffee4) else 'No one'}")

if __name__ == "__main__":
    debug()
