import _sqlite3
class Coffee:

    all = []
    DB_PATH = "coffee_shop.db"
    

    def __init__(self, name, id = None):
    
        self.name = name
        self.id = id
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if  isinstance(value, str) and len(value.strip()) >=3:
           
           self._name =value

        else: 
             raise ValueError("Coffee name must be a string with at least 3 characters")
    
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

#Database methods

@classmethod
def create_table(cls):
    #connection reference
    conn = _sqlite3.connect(cls.DB_PATH)
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS coffees(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL)  """)
    conn.commit()
    conn.close()

def save(self):
    conn = _sqlite3.connect(self.DB_PATH)
    cursor = conn.cursor()
    if self.id is None:
        #research
        cursor.execute("INSERT INTO coffees (name) VALUES(?)", (self.name,))
        self.id = cursor.lastrowid
    else:
        cursor.execute(f"UPDATE coffes SET name = ? WHERE id = ?", (self.name, self.id))
    conn.commit()
    conn.close()


        

    
