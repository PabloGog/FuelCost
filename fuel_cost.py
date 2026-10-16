"""Standalone fuel-cost calculator."""

import tkinter as tk
from tkinter import messagebox, ttk


def calculate_cost():
    try:
        price_per_liter = float(price_var.get().strip().replace(",", "."))
        liters_per_100_km = float(consumption_var.get().strip().replace(",", "."))
        distance_km = float(distance_var.get().strip().replace(",", "."))
    except ValueError:
        messagebox.showerror("Invalid values", "Enter a number in all three fields.")
        return

    if price_per_liter < 0 or liters_per_100_km < 0 or distance_km < 0:
        messagebox.showerror("Invalid values", "Values cannot be negative.")
        return

    liters_used = liters_per_100_km * distance_km / 100
    total_cost = price_per_liter * liters_used
    result_var.set(f"Estimated fuel cost: {total_cost:,.2f}\nFuel used: {liters_used:,.2f} L")


root = tk.Tk()
root.title("Fuel Cost Calculator")
root.resizable(False, False)
root.configure(padx=20, pady=20)

price_var = tk.StringVar()
consumption_var = tk.StringVar()
distance_var = tk.StringVar()
result_var = tk.StringVar(value="Enter the trip details to calculate the cost.")

form = ttk.Frame(root, padding=4)
form.grid(sticky="nsew")

fields = (
    ("Fuel cost per liter", price_var),
    ("Average consumption (L / 100 km)", consumption_var),
    ("Distance covered (km)", distance_var),
)

for row, (label, variable) in enumerate(fields):
    ttk.Label(form, text=label).grid(row=row, column=0, sticky="w", pady=(0, 6))
    entry = ttk.Entry(form, textvariable=variable, width=20)
    entry.grid(row=row, column=1, sticky="ew", padx=(14, 0), pady=(0, 6))
    if row == 0:
        entry.focus()

ttk.Button(form, text="Calculate", command=calculate_cost).grid(
    row=len(fields), column=0, columnspan=2, sticky="ew", pady=(8, 14)
)
ttk.Label(form, textvariable=result_var, justify="left").grid(
    row=len(fields) + 1, column=0, columnspan=2, sticky="w"
)

root.bind("<Return>", lambda event: calculate_cost())
root.mainloop()