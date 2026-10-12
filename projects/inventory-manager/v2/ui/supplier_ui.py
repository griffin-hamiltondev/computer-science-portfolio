import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from services.supplier_service import SupplierService as Service

class SupplierUI:
    def __init__(self, database):
        self.service = Service(database)
        self.supplier_window = tk.Toplevel()
        self.supplier_window.title("Supplier Management")
        self.supplier_window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()
        self.refresh_suppliers()
    
    def create_widgets(self):
        # Supplier List
        self.tree = ttk.Treeview(self.supplier_window, columns=('ID', 'Supplier Name', 'Contact Number', 'Email', 'Address'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Supplier Name', text='Supplier Name')
        self.tree.heading('Contact Number', text='Contact Number')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Address', text='Address')
        self.tree.bind('<<TreeviewSelect>>', self.on_supplier_select)
        self.tree.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        # Form Frame
        form_frame = tk.Frame(self.supplier_window)
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        
        tk.Label(form_frame, text="Supplier Name:").grid(row=0, column=0)
        self.supplier_name_entry = tk.Entry(form_frame)
        self.supplier_name_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(form_frame, text="Contact Number:").grid(row=1, column=0)
        self.contact_number_entry = tk.Entry(form_frame)
        self.contact_number_entry.grid(row=1, column=1, sticky="ew")

        tk.Label(form_frame, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=2, column=1, sticky="ew")

        tk.Label(form_frame, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Entry(form_frame)
        self.address_entry.grid(row=3, column=1, sticky="ew")
        
        # Buttons Frame
        button_frame = tk.Frame(self.supplier_window)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.add_button = tk.Button(button_frame, text="Add Supplier", command=self.add_supplier)
        self.add_button.grid(row=0, column=0, padx=5)
        
        self.update_button = tk.Button(button_frame, text="Update Supplier", command=self.update_supplier)
        self.update_button.grid(row=0, column=1, padx=5)
        
        self.delete_button = tk.Button(button_frame, text="Delete Supplier", command=self.delete_supplier)
        self.delete_button.grid(row=0, column=2, padx=5)
        
        self.back_button = tk.Button(button_frame, text="Back", command=self.supplier_window.destroy)
        self.back_button.grid(row=0, column=3, padx=5)
    
    def refresh_suppliers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        suppliers = self.service.fetch_suppliers()
        for supplier in suppliers:
            self.tree.insert('', 'end', values=supplier)
    
    def on_supplier_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            supplier_data = self.tree.item(selected_item)['values']
            self.supplier_name_entry.delete(0, tk.END)
            self.supplier_name_entry.insert(0, supplier_data[1])
            self.contact_number_entry.delete(0, tk.END)
            self.contact_number_entry.insert(0, supplier_data[2])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, supplier_data[3])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, supplier_data[4])
    
    def add_supplier(self):
        supplier_name = self.supplier_name_entry.get()
        contact_number = self.contact_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.service.add_supplier(supplier_name, contact_number, email, address)
        self.refresh_suppliers()
        
    def update_supplier(self):
        selected_item = self.tree.selection()
        if selected_item:
            supplier_id = self.tree.item(selected_item)['values'][0]
            new_supplier_name = self.supplier_name_entry.get()
            new_contact_number = self.contact_number_entry.get()
            new_email = self.email_entry.get()
            new_address = self.address_entry.get()
            self.service.update_supplier(supplier_id, new_supplier_name, new_contact_number, new_email, new_address)
            self.refresh_suppliers()
        else:
            messagebox.showwarning("No Selection", "Please select a supplier to update.")
    
    def delete_supplier(self):
        selected_item = self.tree.selection()
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this supplier?"):
            if selected_item:
                supplier_id = self.tree.item(selected_item)['values'][0]
                self.service.delete_supplier(supplier_id)
                self.refresh_suppliers()
            else:
                messagebox.showwarning("No Selection", "Please select a supplier to delete.")
    
    def run(self):
        self.supplier_window.mainloop()
    
    def on_close(self):
        self.service.on_close()
        self.supplier_window.destroy()