from database.database import Database

class InventoryService():
    def __init__(self, database):
        self.db = database
    
    def fetch_inventory_items(self):
        return self.db.fetch_inventory_items()
    
    def add_inventory_item(self, item_name, quantity, price, category_id, supplier_id):
        self.db.add_inventory_item(item_name, quantity, price, category_id, supplier_id)
    
    def delete_inventory_item(self, item_id):
        self.db.delete_inventory_item(item_id)
    
    def update_inventory_item(self, item_id, new_item_name, new_quantity, new_price, new_category_id, new_supplier_id):
        self.db.update_inventory_item(item_id, new_item_name, new_quantity, new_price, new_category_id, new_supplier_id)
    
    def fetch_categories(self):
        return self.db.fetch_categories()
    
    def fetch_suppliers(self):
        return self.db.fetch_suppliers()
    
    def calculate_total_value(self):
        return self.db.calculate_stock_value()
    
    def on_close(self):
        self.db.on_close()