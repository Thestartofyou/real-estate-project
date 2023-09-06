import sqlite3
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Create SQLite database and tables
conn = sqlite3.connect("commercial_real_estate.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY,
                name TEXT,
                type TEXT,
                price REAL,
                rent_income REAL,
                expenses REAL
            )''')
conn.commit()

# Function to add a new property listing
def add_property():
    name = name_entry.get()
    property_type = type_entry.get()
    price = float(price_entry.get())
    rent_income = float(rent_entry.get())
    expenses = float(expenses_entry.get())

    c.execute("INSERT INTO properties (name, type, price, rent_income, expenses) VALUES (?, ?, ?, ?, ?)",
              (name, property_type, price, rent_income, expenses))
    conn.commit()
    clear_entries()
    messagebox.showinfo("Success", "Property added successfully!")

# Function to view property details
def view_properties():
    c.execute("SELECT * FROM properties")
    rows = c.fetchall()
    if rows:
        property_df = pd.DataFrame(rows, columns=["ID", "Name", "Type", "Price", "Rent Income", "Expenses"])
        property_df.set_index("ID", inplace=True)
        messagebox.showinfo("Property Listings", property_df.to_string())
    else:
        messagebox.showinfo("Property Listings", "No properties found.")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    rent_entry.delete(0, tk.END)
    expenses_entry.delete(0, tk.END)

# Create a tkinter GUI
root = tk.Tk()
root.title("Commercial Real Estate Management")

# Label and Entry widgets for property details
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Type:").grid(row=1, column=0)
type_entry = tk.Entry(root)
type_entry.grid(row=1, column=1)

tk.Label(root, text="Price:").grid(row=2, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1)

tk.Label(root, text="Rent Income:").grid(row=3, column=0)
rent_entry = tk.Entry(root)
rent_entry.grid(row=3, column=1)

tk.Label(root, text="Expenses:").grid(row=4, column=0)
expenses_entry = tk.Entry(root)
expenses_entry.grid(row=4, column=1)

# Buttons for actions
add_button = tk.Button(root, text="Add Property", command=add_property)
add_button.grid(row=5, column=0)

view_button = tk.Button(root, text="View Properties", command=view_properties)
view_button.grid(row=5, column=1)

# Start the tkinter main loop
root.mainloop()
