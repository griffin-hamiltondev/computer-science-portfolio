import sqlite3
from datetime import datetime as dt

class Database:
    # Connection, Creation and Close
    
    def __init__(self):
        self.db_name = "inventory.db"
        self.connection = None
        self.connect()
    
    # Open the connection
    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        # Ensure tables exist after establishing connection
        self.create_tables()
    
    # Create the database and its tables if it doesn't exist
    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_name TEXT NOT NULL UNIQUE,
            contact_number TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS inventory (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            category_id INTEGER NOT NULL,
            supplier_id INTEGER NOT NULL,
            last_updated TEXT NOT NULL,

            FOREIGN KEY (category_id)
                REFERENCES categories(category_id),

            FOREIGN KEY (supplier_id)
                REFERENCES suppliers(supplier_id)
        );
        """)
        self.connection.commit()
    
    # Close the connection
    def on_close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    # Query Execution
    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
    
    # Inventory Logic
    
    # Fetch Inventory Items
    def fetch_inventory_items(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT
                        i.item_id,
                        i.item_name,
                        i.quantity,
                        i.price,
                        c.category_name,
                        s.supplier_name,
                        i.last_updated
                        FROM inventory i
                        LEFT JOIN categories c
                            ON i.category_id = c.category_id
                        LEFT JOIN suppliers s
                            ON i.supplier_id = s.supplier_id
                        """)
        result = cursor.fetchall()
        return result
    
    # Add a New Inventory Item
    def add_inventory_item(self, item_name, quantity, price, category_id, supplier_id):
        last_updated = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_query = """INSERT INTO inventory 
                        (item_name, quantity, price, category_id, supplier_id, last_updated)
                        VALUES (?, ?, ?, ?, ?, ?)"""
        self.execute_query(insert_query, (item_name, quantity, price, category_id, supplier_id, last_updated))
    
    # Delete an Inventory Item
    def delete_inventory_item(self, item_id):
        delete_query = "DELETE FROM inventory WHERE item_id = ?"
        self.execute_query(delete_query, (item_id,))
    
    # Update an Inventory Item
    def update_inventory_item(self, item_id, new_item_name, new_quantity, new_price, new_category_id, new_supplier_id):
        last_updated = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        update_query = """UPDATE inventory 
                        SET item_name = ?,
                            quantity = ?,
                            price = ?,
                            category_id = ?,
                            supplier_id = ?,
                            last_updated = ?
                        WHERE item_id = ?"""
        self.execute_query(update_query, (new_item_name, new_quantity, new_price, new_category_id, new_supplier_id, last_updated, item_id))
    
    def calculate_stock_value(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT SUM(quantity * price) FROM inventory")
        result = cursor.fetchone()[0]
        return result if result else 0.0
    
    # Category Logic
    
    # Fetch Categories
    def fetch_categories(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM categories")
        result = cursor.fetchall()
        return result
    
    # Add a New Category
    def add_category(self, category_name):
        insert_query = "INSERT INTO categories (category_name) VALUES (?)"
        self.execute_query(insert_query, (category_name,))
    
    # Delete a Category
    def delete_category(self, category_id):
        delete_query = "DELETE FROM categories WHERE category_id = ?"
        self.execute_query(delete_query, (category_id,))
        delete_inventory_query = "DELETE FROM inventory WHERE category_id = ?"
        self.execute_query(delete_inventory_query, (category_id,))
    
    # Update a Category
    def update_category(self, category_id, new_category_name):
        update_query = "UPDATE categories SET category_name = ? WHERE category_id = ?"
        self.execute_query(update_query, (new_category_name, category_id))
        
    
    # Supplier Logic
    
    # Fetch Suppliers
    def fetch_suppliers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM suppliers")
        result = cursor.fetchall()
        return result
    
    # Add a New Supplier
    def add_supplier(self, supplier_name, contact_number, email, address):
        insert_query = """INSERT INTO suppliers 
                        (supplier_name, contact_number, email, address) 
                        VALUES (?, ?, ?, ?)"""
        self.execute_query(insert_query, (supplier_name, contact_number, email, address))
    
    # Delete a Supplier
    def delete_supplier(self, supplier_id):
        delete_query = "DELETE FROM suppliers WHERE supplier_id = ?"
        self.execute_query(delete_query, (supplier_id,))
        delete_inventory_query = "DELETE FROM inventory WHERE supplier_id = ?"
        self.execute_query(delete_inventory_query, (supplier_id,))

    # Update a Supplier
    def update_supplier(self, supplier_id, new_supplier_name, new_contact_number, new_email, new_address):
        update_query = """UPDATE suppliers 
                        SET supplier_name = ?, contact_number = ?, email = ?, address = ? 
                        WHERE supplier_id = ?"""
        self.execute_query(update_query, (new_supplier_name, new_contact_number, new_email, new_address, supplier_id))