import sqlite3
from datetime import datetime as dt

class Database:
    def __init__(self):
        self.db_name = "inventory.db"
        self.connection = None
        self.connect()
        self.create_tables()
        self.disconnect()
    
    def execute_query(self, query, params=None):
        self.connect()
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        self.disconnect()

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        if not self.connection:
            self.create_tables()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            supplier TEXT NOT NULL,
            last_updated TEXT NOT NULL
        )
        """)
        self.connection.commit()
        self.disconnect()

    
    def insert_item(self, item_name, quantity, price, category="General", supplier="Unknown"):
        self.connect()
        insert_query = "INSERT INTO inventory (item_name, quantity, price, category, supplier, last_updated) VALUES (?, ?, ?, ?, ?, ?)"
        time_stamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.execute_query(insert_query, (item_name, quantity, price, category, supplier, time_stamp))
        self.disconnect()

    def fetch_item(self, query, params=None):
        self.connect()
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        result = cursor.fetchall()
        self.disconnect()
        return result

    def update_item(self, item_name, quantity, price=None, category=None, supplier=None):
        self.connect()
        update_query = "UPDATE inventory SET quantity = ?"
        params = [quantity]

        if price is not None:
            update_query += ", price = ?"
            params.append(price)

        if category is not None:
            update_query += ", category = ?"
            params.append(category)

        if supplier is not None:
            update_query += ", supplier = ?"
            params.append(supplier)

        time_stamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        update_query += ", last_updated = ?"
        params.append(time_stamp)
        
        update_query += " WHERE item_name = ?"
        params.append(item_name)

        self.execute_query(update_query, tuple(params))
        self.disconnect()

    def delete_item(self, item_name):
        self.connect()
        delete_query = "DELETE FROM inventory WHERE item_name = ?"
        self.execute_query(delete_query, (item_name,))
        self.disconnect()