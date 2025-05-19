# Coffee Shop System

This is a Python-based system for managing a coffee shop's operations, including customers, coffee products, and orders.

## Features

* **Customer Management:**
    * Customers have a name (string, 1-15 characters).
    * The system keeps track of all customers.
    * Provides functionality to retrieve a customer's order history.
    * Calculates the coffees a customer has ordered.
    * Calculates how much a customer has spent on a specific coffee.
    * Determines the "most aficionado" customer for a given coffee (the customer who has spent the most on it).
* **Coffee Management:**
    * Coffees have a name (string, at least 3 characters).
    * The system keeps track of all coffee types.
    * Provides functionality to retrieve the orders for a specific coffee.
    * Calculates the customers who ordered a specific coffee.
    * Calculates how many times a coffee has been ordered.
    * Calculates the average price of a coffee.
* **Order Management:**
    * Orders link a customer to a coffee and include the price.
    * Order prices must be a float between 1.0 and 10.0.
    * The system keeps track of all orders.

## Classes

### `Customer`

Represents a customer.

* **Attributes:**
    * `name` (string): The customer's name.

* **Methods:**
    * `__init__(self, name)`: Initializes a new customer with a name.
    * `orders(self)`: Returns a list of `Order` objects for this customer.
    * `coffees(self)`: Returns a list of `Coffee` objects for this customer.
    * `create_order(self, coffee, price)`: Creates a new `Order` for the customer.
    * `total_spent_on_coffee(self, coffee)`: Calculates the total amount spent by the customer on a specific `Coffee`.
    * `most_aficionado(cls, coffee)` (class method): Returns the `Customer` who has spent the most on a given `Coffee`.

### `Coffee`

Represents a type of coffee.

* **Attributes:**
    * `name` (string): The name of the coffee.

* **Methods:**
    - __init__(self, name): Initializes a new coffee type with a name.
    - orders(self): Returns a list of `Order` objects for this coffee type.
    - customers(self): Returns a list of `Customer` objects who have ordered this coffee type.
    - `num_orders(self)`: Returns a string indicating the number of times this coffee has been ordered.
    - `average_price(self)`: Returns a string indicating the average price of this coffee.

### `Order`

Represents an order placed by a customer for a coffee.

* **Attributes:**
    -customer (`Customer`): The customer who placed the order.
    * `coffee` (`Coffee`): The coffee ordered.
    * `price` (float): The price of the order.

* **Methods:**
    * `__init__(self, customer, coffee, price)`: Initializes a new order.

## How to Use

1.  **Define Coffee Types:** Create `Coffee` objects for each type of coffee you offer (e.g., "Latte", "Espresso").
2.  **Create Customers:** Create `Customer` objects for each customer.
3.  **Place Orders:** Use the `create_order` method of a `Customer` object to create orders, linking them to `Coffee` objects and specifying the price.
4.  **Query Data:** Use the methods of the `Customer` and `Coffee` classes to retrieve information about orders, customers, and spending.

