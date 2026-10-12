import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from services.category_service import CategoryService as Service

class CategoryUI:
    def __init__(self, database):
        self.service = Service(database)
        self.category_window = tk.Toplevel()
        self.category_window.title("Category Management")
        self.category_window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()
        self.refresh_categories()
    
    def create_widgets(self):
        # Category List
        self.tree = ttk.Treeview(self.category_window, columns=('ID', 'Category Name'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Category Name', text='Category Name')
        self.tree.bind('<<TreeviewSelect>>', self.on_category_select)
        self.tree.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        # Form Frame
        form_frame = tk.Frame(self.category_window)
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        
        tk.Label(form_frame, text="Category Name:").grid(row=0, column=0)
        self.category_name_entry = tk.Entry(form_frame)
        self.category_name_entry.grid(row=0, column=1, sticky="ew")
        
        # Buttons Frame
        button_frame = tk.Frame(self.category_window)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.add_button = tk.Button(button_frame, text="Add Category", command=self.add_category)
        self.add_button.grid(row=0, column=0, padx=5)
        
        self.update_button = tk.Button(button_frame, text="Update Category", command=self.update_category)
        self.update_button.grid(row=0, column=1, padx=5)
        
        self.delete_button = tk.Button(button_frame, text="Delete Category", command=self.delete_category)
        self.delete_button.grid(row=0, column=2, padx=5)
        
        self.back_button = tk.Button(button_frame, text="Back", command=self.category_window.destroy)
        self.back_button.grid(row=0, column=3, padx=5)
    
    def refresh_categories(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        categories = self.service.fetch_categories()
        for category in categories:
            self.tree.insert('', 'end', values=category)
    
    def on_category_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            category_id, category_name = self.tree.item(selected_item[0])['values']
            self.category_name_entry.delete(0, tk.END)
            self.category_name_entry.insert(0, category_name)
    
    def add_category(self):
        category_name = self.category_name_entry.get()
        if category_name:
            self.service.add_category(category_name)
            self.refresh_categories()
            self.category_name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a category name.")
    
    def update_category(self):
        selected_item = self.tree.selection()
        if selected_item:
            category_id = self.tree.item(selected_item[0])['values'][0]
            new_category_name = self.category_name_entry.get()
            if new_category_name:
                self.service.update_category(category_id, new_category_name)
                self.refresh_categories()
                self.category_name_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a category name.")
        else:
            messagebox.showwarning("Selection Error", "Please select a category to update.")
    
    def delete_category(self):
        selected_item = self.tree.selection()
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this category? This will also delete all associated inventory items."):
            if selected_item:
                category_id = self.tree.item(selected_item[0])['values'][0]
                self.service.delete_category(category_id)
                self.refresh_categories()
                self.category_name_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Selection Error", "Please select a category to delete.")
    
    def run(self):
        self.category_window.mainloop()
    
    def on_close(self):
        self.service.on_close()
        self.category_window.quit()