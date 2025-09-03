import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import edit_reservation   # import the edit reservation page
import home               # for back to home button

def load_reservations(name):
    # Clear table
    for row in tree.get_children():
        tree.delete(row)

    # Fetch reservations only for this name
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations WHERE name = ?", (name,))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            tree.insert("", tk.END, values=row)
    else:
        messagebox.showinfo("No Reservations", "No reservations found for this name.")

def search_reservations():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name!")
        return
    load_reservations(name)

def on_row_double_click(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    row_data = tree.item(selected_item)["values"]  # get row data
    reservation_id = row_data[0]  # ID is the first column
    root.destroy()
    edit_reservation.create_edit_window(reservation_id)

def create_reservations_window():
    global tree, root, name_entry
    root = tk.Tk()
    root.title("Your Reservations")
    root.geometry("800x500")
    root.configure(bg="white")

    # --- Search Section ---
    tk.Label(root, text="Enter Your Name:", font=("Arial", 14, "bold"),
             bg="white", fg="black").pack(pady=5)
    name_entry = tk.Entry(root, font=("Arial", 14), width=30)
    name_entry.pack(pady=5)

    tk.Button(root, text="Search Reservations",
              font=("Arial", 12, "bold"),
              bg="navy", fg="white",
              command=search_reservations).pack(pady=10)

    # --- Table ---
    columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=110, anchor="center")

    tree.pack(pady=10, fill="x")

    # Double-click event (to edit/delete)
    tree.bind("<Double-1>", on_row_double_click)

    # --- Navigation ---
    tk.Button(root, text="Back to Home",
              font=("Arial", 12, "bold"),
              bg="gray", fg="white",
              command=lambda: [root.destroy(), home.create_home_window()]
              ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_reservations_window()
