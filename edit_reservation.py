import tkinter as tk
from tkinter import messagebox
import sqlite3
import reservations   # go back after editing
import home           # for back to home button

def load_reservation(reservation_id):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_reservation(reservation_id):
    name = name_entry.get()
    flight_number = flight_entry.get()
    departure = departure_entry.get()
    destination = destination_entry.get()
    date = date_entry.get()
    seat_number = seat_entry.get()

    if not (name and flight_number and departure and destination and date and seat_number):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE reservations
                      SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
                      WHERE id=?""",
                   (name, flight_number, departure, destination, date, seat_number, reservation_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Reservation updated successfully!")
    root.destroy()
    reservations.create_reservations_window()

def delete_reservation(reservation_id):
    if not messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?"):
        return

    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Deleted", "Reservation deleted successfully!")
    root.destroy()
    reservations.create_reservations_window()

def create_edit_window(reservation_id):
    global root, name_entry, flight_entry, departure_entry, destination_entry, date_entry, seat_entry
    root = tk.Tk()
    root.title("Edit Reservation")
    root.geometry("800x500")
    root.configure(bg="white")

    row = load_reservation(reservation_id)
    if not row:
        messagebox.showerror("Error", "Reservation not found!")
        root.destroy()
        reservations.create_reservations_window()
        return

    # Unpack row
    _, name, flight_number, departure, destination, date, seat_number = row

    label_font = ("Arial", 14, "bold")
    entry_font = ("Arial", 14)

    # --- Form Frame ---
    form_frame = tk.Frame(root, bg="white")
    form_frame.pack(fill="both", expand=True)

    # Passenger Name
    tk.Label(form_frame, text="Passenger Name", font=label_font, bg="white", fg="navy").pack(pady=5)
    name_entry = tk.Entry(form_frame, font=entry_font, width=40)
    name_entry.insert(0, name)
    name_entry.pack(pady=5)

    # Flight Number
    tk.Label(form_frame, text="Flight Number", font=label_font, bg="white", fg="navy").pack(pady=5)
    flight_entry = tk.Entry(form_frame, font=entry_font, width=40)
    flight_entry.insert(0, flight_number)
    flight_entry.pack(pady=5)

    # Departure
    tk.Label(form_frame, text="Departure", font=label_font, bg="white", fg="navy").pack(pady=5)
    departure_entry = tk.Entry(form_frame, font=entry_font, width=40)
    departure_entry.insert(0, departure)
    departure_entry.pack(pady=5)

    # Destination
    tk.Label(form_frame, text="Destination", font=label_font, bg="white", fg="navy").pack(pady=5)
    destination_entry = tk.Entry(form_frame, font=entry_font, width=40)
    destination_entry.insert(0, destination)
    destination_entry.pack(pady=5)

    # Date
    tk.Label(form_frame, text="Date (YYYY-MM-DD)", font=label_font, bg="white", fg="navy").pack(pady=5)
    date_entry = tk.Entry(form_frame, font=entry_font, width=40)
    date_entry.insert(0, date)
    date_entry.pack(pady=5)

    # Seat Number
    tk.Label(form_frame, text="Seat Number", font=label_font, bg="white", fg="navy").pack(pady=5)
    seat_entry = tk.Entry(form_frame, font=entry_font, width=40)
    seat_entry.insert(0, seat_number)
    seat_entry.pack(pady=5)

    # Action Buttons (Update / Delete)
    tk.Button(form_frame, text="Update", font=("Arial", 12, "bold"),
              bg="green", fg="white", width=15,
              command=lambda: update_reservation(reservation_id)).pack(pady=10)

    tk.Button(form_frame, text="Delete", font=("Arial", 12, "bold"),
              bg="red", fg="white", width=15,
              command=lambda: delete_reservation(reservation_id)).pack(pady=10)

    # --- Navigation Frame (Bottom) ---
    nav_frame = tk.Frame(root, bg="white")
    nav_frame.pack(fill="x", side="bottom")

    tk.Button(nav_frame, text="Back to Home",
              font=("Arial", 12, "bold"),
              bg="gray", fg="white", width=15,
              command=lambda: [root.destroy(), home.create_home_window()]
              ).pack(pady=10)

    root.mainloop()
