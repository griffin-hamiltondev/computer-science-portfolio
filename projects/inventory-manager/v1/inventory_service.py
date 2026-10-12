import database as db

class InventoryService:
    def __init__(self):
        self.db = db.Database()

    def add_item(self, item_name, quantity, price=0, category="General", supplier="Unknown"):
        self.db.insert_item(item_name, quantity, price, category, supplier)

    def update_item(self, item_name, quantity, price=None, category=None, supplier=None):
        self.db.update_item(item_name, quantity, price, category, supplier)

    def delete_item(self, item_name):
        self.db.delete_item(item_name)

    def fetch_item(self):
        return self.db.fetch_item("SELECT * FROM inventory")

    def calculate_stock_value(self):
        inventory = self.fetch_item()
        total_value = sum(item[2] * item[3] for item in inventory)
        return total_value