import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import inventory_service as ia

class InventoryUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inventory Management")
        self.service = ia.InventoryService()

        self.create_widgets()
        self.refresh_inventory()

    def create_widgets(self):
        # Inventory List
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Item Name', 'Quantity', 'Price', 'Category', 'Supplier', 'Last Updated'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Item Name', text='Item Name')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Supplier', text='Supplier')
        self.tree.heading('Last Updated', text='Last Updated')
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)
        self.tree.grid(row=0, column=0, columnspan=2, sticky='nsew')

        # Add Form Frame
        form_frame = tk.Frame(self.root)
        form_frame.grid(row=1, column=0, pady=10, padx=10)

        tk.Label(form_frame, text="Item Name:").grid(row=0, column=0)
        self.item_name_entry = tk.Entry(form_frame)
        self.item_name_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Quantity:").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(form_frame)
        self.quantity_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Price:").grid(row=2, column=0)
        self.price_entry = tk.Entry(form_frame)
        self.price_entry.grid(row=2, column=1)

        tk.Label(form_frame, text="Category:").grid(row=3, column=0)
        self.category_entry = tk.Entry(form_frame)
        self.category_entry.grid(row=3, column=1)

        tk.Label(form_frame, text="Supplier:").grid(row=4, column=0)
        self.supplier_entry = tk.Entry(form_frame)
        self.supplier_entry.grid(row=4, column=1)
        
        # Button Frame
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=1, pady=10, padx=10)

        add_button = tk.Button(button_frame, text="Add Item", command=self.add_item)
        add_button.grid(row=0, column=0, columnspan=2)
        
        update_button = tk.Button(button_frame, text="Update Item", command=self.update_item)
        update_button.grid(row=1, column=0, columnspan=2)
        
        delete_button = tk.Button(button_frame, text="Delete Item", command=self.delete_item)
        delete_button.grid(row=2, column=0, columnspan=2)
        
        clear_button = tk.Button(button_frame, text="Clear Fields", command=self.clear_fields)
        clear_button.grid(row=3, column=0, columnspan=2)
        
        stock_value_button = tk.Button(button_frame, text="Calculate Stock Value", command=self.calculate_stock_value)
        stock_value_button.grid(row=4, column=0, columnspan=2)
    
    def on_item_select(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            self.item_name_entry.delete(0, tk.END)
            self.item_name_entry.insert(0, item_values[1])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, item_values[2])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, item_values[3])
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, item_values[4])
            self.supplier_entry.delete(0, tk.END)
            self.supplier_entry.insert(0, item_values[5])

    def add_item(self):
        item_name = self.item_name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        category = self.category_entry.get()
        supplier = self.supplier_entry.get()
        self.service.add_item(item_name, quantity, price, category, supplier)
        self.refresh_inventory()
    
    def update_item(self):
        item_name = self.item_name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        category = self.category_entry.get()
        supplier = self.supplier_entry.get()
        self.service.update_item(item_name, quantity, price, category, supplier)
        self.refresh_inventory()
    
    def delete_item(self):
        item_name = self.item_name_entry.get()
        self.service.delete_item(item_name)
        self.refresh_inventory()
    
    def calculate_stock_value(self):
        total_value = self.service.calculate_stock_value()
        messagebox.showinfo("Total Stock Value", f"Total Stock Value: R{total_value:.2f}")
    
    def clear_fields(self):
        self.item_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.supplier_entry.delete(0, tk.END)

    def refresh_inventory(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        inventory = self.service.fetch_item()
        for item in inventory:
            self.tree.insert('', 'end', values=(item))
        
    def run(self):
        self.root.mainloop()