import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import edit_reservation   # import the edit reservation page
import home               # for back to home button

def load_reservations():
    # Clear table
    for row in tree.get_children():
        tree.delete(row)

    # Fetch all reservations
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)

def on_row_double_click(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    row_data = tree.item(selected_item)["values"]  # get row data
    reservation_id = row_data[0]  # ID is the first column
    root.destroy()
    edit_reservation.create_edit_window(reservation_id)

def create_reservations_window():
    global tree, root
    root = tk.Tk()
    root.title("Reservations")
    root.geometry("800x500")
    root.configure(bg="white")

    # --- Form Frame ---
    form_frame = tk.Frame(root, bg="white")
    form_frame.pack(fill="both", expand=True)

    # Title
    tk.Label(form_frame, text="All Reservations",
             font=("Arial", 18, "bold"),
             fg="navy", bg="white").pack(pady=10)

    # Table
    columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
    tree = ttk.Treeview(form_frame, columns=columns, show="headings", height=15)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=110, anchor="center")

    tree.pack(pady=10, fill="x")

    # Double-click event
    tree.bind("<Double-1>", on_row_double_click)

    # Refresh button
    tk.Button(form_frame, text="Refresh List",
              font=("Arial", 12, "bold"),
              bg="navy", fg="white",
              command=load_reservations).pack(pady=10)

    # --- Navigation Frame (Bottom) ---
    nav_frame = tk.Frame(root, bg="white")
    nav_frame.pack(fill="x", side="bottom")

    tk.Button(nav_frame, text="Back to Home",
              font=("Arial", 12, "bold"),
              bg="gray", fg="white",
              command=lambda: [root.destroy(), home.create_home_window()]
              ).pack(pady=10)

    load_reservations()

    root.mainloop()

if __name__ == "__main__":
    create_reservations_window()
