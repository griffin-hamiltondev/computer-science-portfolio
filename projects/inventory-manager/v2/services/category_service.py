class CategoryService:
    def __init__(self, db):
        self.db = db

    def fetch_categories(self):
        return self.db.fetch_categories()
    
    def add_category(self, category_name):
        self.db.add_category(category_name)
    
    def delete_category(self, category_id):
        self.db.delete_category(category_id)
    
    def update_category(self, category_id, new_category_name):
        self.db.update_category(category_id, new_category_name)
    
    def on_close(self):
        self.db.on_close()