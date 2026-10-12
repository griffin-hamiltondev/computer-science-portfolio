class SupplierService:
    def __init__(self, db):
        self.db = db

    def fetch_suppliers(self):
        return self.db.fetch_suppliers()
    
    def add_supplier(self, supplier_name, contact_info, email, address):
        self.db.add_supplier(supplier_name, contact_info, email, address)
    
    def delete_supplier(self, supplier_id):
        self.db.delete_supplier(supplier_id)
    
    def update_supplier(self, supplier_id, new_supplier_name, new_contact_info, new_email, new_address):
        self.db.update_supplier(supplier_id, new_supplier_name, new_contact_info, new_email, new_address)
    
    def on_close(self):
        self.db.on_close()