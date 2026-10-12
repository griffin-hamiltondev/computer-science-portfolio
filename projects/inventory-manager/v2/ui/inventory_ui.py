import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from services.inventory_service import InventoryService as Service
from database.database import Database
from ui.category_ui import CategoryUI
from ui.supplier_ui import SupplierUI

class InventoryUI:
    # Innitiation and Close
    
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("Inventory Management")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.service = Service(self.db)
        self.create_widgets()
        self.refresh_inventory()
        self.refresh_categories()
        self.refresh_suppliers()
    
    def run(self):
        self.root.mainloop()
    
    def on_close(self):
        self.service.on_close()
        self.root.destroy()
    
    # Create Widgets
    
    def create_widgets(self):
        # Inventory List
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Item Name', 'Quantity', 'Price', 'Category','Supplier', 'Last Updated'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Item Name', text='Item Name')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Supplier', text='Supplier')
        self.tree.heading('Last Updated', text='Last Updated')
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)
        self.tree.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        # Form Frame
        form_frame = tk.Frame(self.root)
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        
        tk.Label(form_frame, text="Item Name:").grid(row=0, column=0)
        self.item_name_entry = tk.Entry(form_frame)
        self.item_name_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(form_frame, text="Quantity:").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(form_frame)
        self.quantity_entry.grid(row=1, column=1, sticky="ew")

        tk.Label(form_frame, text="Price:").grid(row=2, column=0)
        self.price_entry = tk.Entry(form_frame)
        self.price_entry.grid(row=2, column=1, sticky="ew")

        tk.Label(form_frame, text="Category:").grid(row=3, column=0)
        self.category_combobox = ttk.Combobox(form_frame, state="readonly")
        self.category_combobox.grid(row=3, column=1, sticky="ew")

        tk.Label(form_frame, text="Supplier:").grid(row=4, column=0)
        self.supplier_combobox = ttk.Combobox(form_frame, state="readonly")
        self.supplier_combobox.grid(row=4, column=1, sticky="ew")
        
        # Button Form
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

        add_button = tk.Button(button_frame, text="Add Item", command=self.add_item)
        add_button.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        update_button = tk.Button(button_frame, text="Update Item", command=self.update_item)
        update_button.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
        delete_button = tk.Button(button_frame, text="Delete Item", command=self.delete_item)
        delete_button.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
        clear_button = tk.Button(button_frame, text="Clear Fields", command=self.clear_fields)
        clear_button.grid(row=3, column=0, columnspan=2, sticky="nsew")
        
        stock_value_button = tk.Button(button_frame, text="Calculate Stock Value", command=self.calculate_stock_value)
        stock_value_button.grid(row=4, column=0, columnspan=2, sticky="nsew")
        
        category_button = tk.Button(button_frame, text="Category Table", command=self.category_table)
        category_button.grid(row=5, column=0, columnspan=2, sticky="nsew")
        
        supplier_button = tk.Button(button_frame, text="Supplier Table", command=self.supplier_table)
        supplier_button.grid(row=6, column=0, columnspan=2, sticky="nsew")
    
    # Treeview Item Selection
    def on_item_select(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            self.selected_id = item_values[0]
            self.item_name_entry.delete(0, tk.END)
            self.item_name_entry.insert(0, item_values[1])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, item_values[2])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, item_values[3])
            # item_values layout: id, name, quantity, price, category_id, category_name, supplier_id, supplier_name, last_updated
            cat_id = item_values[4]
            cat_name = item_values[5] if len(item_values) > 5 else ''
            sup_id = item_values[6] if len(item_values) > 6 else None
            sup_name = item_values[7] if len(item_values) > 7 else ''

            # Set combobox selection to "id: name" if present in values
            target_cat = f"{cat_id}: {cat_name}" if cat_id is not None else cat_name
            if target_cat in self.category_combobox['values']:
                self.category_combobox.set(target_cat)
            else:
                self.category_combobox.set(cat_name)

            target_sup = f"{sup_id}: {sup_name}" if sup_id is not None else sup_name
            if target_sup in self.supplier_combobox['values']:
                self.supplier_combobox.set(target_sup)
            else:
                self.supplier_combobox.set(sup_name)
    
    # Treeview Populate and Refresh
    def refresh_inventory(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        inventory = self.service.fetch_inventory_items()
        for item in inventory:
            # ensure we pass the tuple directly as values
            self.tree.insert('', 'end', values=item)
    
    # Category Combobox Populate and Refresh
    def refresh_categories(self):
        self.category_combobox.set('')
        self.category_combobox['values'] = [f"{cat[0]}: {cat[1]}" for cat in self.service.fetch_categories()]
    
    # Supplier Combobox Populate and Refresh
    def refresh_suppliers(self):
        self.supplier_combobox.set('')
        self.supplier_combobox['values'] = [f"{sup[0]}: {sup[1]}" for sup in self.service.fetch_suppliers()]
    
    # Button Commands
    
    def add_item(self):
        item_name = self.item_name_entry.get()
        # Validate inputs
        if not item_name.strip():
            messagebox.showerror("Input Error", "Item name is required.")
            return
        try:
            quantity = int(self.quantity_entry.get())
            if quantity < 0:
                raise ValueError()
        except Exception:
            messagebox.showerror("Input Error", "Quantity must be a non-negative integer.")
            return
        try:
            price = float(self.price_entry.get())
            if price < 0:
                raise ValueError()
        except Exception:
            messagebox.showerror("Input Error", "Price must be a non-negative number.")
            return

        try:
            category_id = int(self.category_combobox.get().split(':', 1)[0])
        except Exception:
            messagebox.showerror("Input Error", "Please select a valid category from the dropdown.")
            return
        try:
            supplier_id = int(self.supplier_combobox.get().split(':', 1)[0])
        except Exception:
            messagebox.showerror("Input Error", "Please select a valid supplier from the dropdown.")
            return

        try:
            self.service.add_inventory_item(item_name, quantity, price, category_id, supplier_id)
            self.refresh_inventory()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
    
    def update_item(self):
        item_name = self.item_name_entry.get()
        if not hasattr(self, 'selected_id'):
            messagebox.showerror("Selection Error", "No item selected to update.")
            return
        if not item_name.strip():
            messagebox.showerror("Input Error", "Item name is required.")
            return
        try:
            quantity = int(self.quantity_entry.get())
            if quantity < 0:
                raise ValueError()
        except Exception:
            messagebox.showerror("Input Error", "Quantity must be a non-negative integer.")
            return
        try:
            price = float(self.price_entry.get())
            if price < 0:
                raise ValueError()
        except Exception:
            messagebox.showerror("Input Error", "Price must be a non-negative number.")
            return
        try:
            category_id = int(self.category_combobox.get().split(':', 1)[0])
        except Exception:
            messagebox.showerror("Input Error", "Please select a valid category from the dropdown.")
            return
        try:
            supplier_id = int(self.supplier_combobox.get().split(':', 1)[0])
        except Exception:
            messagebox.showerror("Input Error", "Please select a valid supplier from the dropdown.")
            return

        try:
            self.service.update_inventory_item(self.selected_id, item_name, quantity, price, category_id, supplier_id)
            self.refresh_inventory()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
    
    def delete_item(self):
        if messagebox.askyesno("Confirm Delete", f"Delete '{self.selected_id}'?"):
            self.service.delete_inventory_item(self.selected_id)
            self.refresh_inventory()
    
    def clear_fields(self):
        self.item_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.category_combobox.set('')
        self.supplier_combobox.set('')
    
    def calculate_stock_value(self):
        total_value = self.service.calculate_stock_value()
        messagebox.showinfo("Total Stock Value", f"Total Stock Value: R{total_value:.2f}")
    
    def category_table(self):
        category_ui = CategoryUI(database=self.db)
        category_ui.run()
        self.refresh_categories()
        self.refresh_inventory()
    
    def supplier_table(self):
        supplier_ui = SupplierUI(database=self.db)
        supplier_ui.run()
        self.refresh_suppliers()
        self.refresh_inventory()
