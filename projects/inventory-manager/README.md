# Inventory Manager

A desktop inventory management application built with Python, Tkinter, and SQLite. This project explores graphical user interfaces, database operations, and the gradual improvement of application structure across two versions.

## Versions

### Version 1 — Basic Inventory Management

V1 provides the initial inventory management functionality using a Tkinter interface and a SQLite database.

**Features**

* Add, update, and delete inventory items
* Store item names, quantities, prices, categories, suppliers, and last-updated timestamps
* Display inventory records in a table
* Calculate the total value of current stock

**Structure**

* `main.py` — application entry point
* `ui.py` — graphical user interface
* `inventory_service.py` — inventory operations
* `database.py` — SQLite database operations

### Version 2 — Expanded Inventory Management

V2 expands the application to manage inventory alongside separate category and supplier records.

**Features**

* Add, update, and delete inventory items
* Manage categories independently
* Manage supplier details, including contact number, email, and address
* Associate inventory items with categories and suppliers
* Display inventory records in a table
* Calculate the total value of current stock
* Store data in SQLite tables with category and supplier identifiers

**Structure**

* `main.py` — application entry point
* `ui/` — inventory, category, and supplier interfaces
* `services/` — service classes for inventory, categories, and suppliers
* `database/database.py` — SQLite schema and database operations

V2 introduces a more modular structure than V1 by separating the interface, service classes, and database operations into different modules.

## Technologies

* **Python** — application logic
* **Tkinter and ttk** — desktop graphical interface
* **SQLite** — persistent local data storage
* **Git and GitHub** — version control and project portfolio

## Requirements

* Python 3
* Tkinter support for Python
* SQLite support, included with standard Python installations in typical environments

On Debian-based Linux distributions, Tkinter may need to be installed separately:

```bash
sudo apt install python3-tk
```

## Running the Application

Run each version from its own directory so its relative SQLite database path behaves as expected.

### V1

From the repository root:

```bash
cd projects/inventory-manager/v1
python3 main.py
```

### V2

From the repository root:

```bash
cd projects/inventory-manager/v2
python3 main.py
```

Each version creates or opens an `inventory.db` file in its current working directory when its database code runs. The database files are generated locally and are not included in the repository.

## Learning Objectives

This project provides practical experience with:

* Building desktop interfaces with Tkinter
* Performing CRUD operations with SQLite
* Separating interface code from application services and database operations
* Working with related database tables
* Calculating inventory stock value
* Refactoring and expanding an existing application across versions

## Current Status and Future Work

V2 is the more feature-rich iteration. Further improvements, including fixes and refinements identified during development, are planned for a future V3.

The project is a learning and portfolio project, not a production-ready inventory system. The versions have passed a Python syntax compilation check, but that check does not verify runtime behaviour or all application workflows.
