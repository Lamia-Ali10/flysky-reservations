import tkinter as tk
from tkinter import messagebox
import sqlite3
import home   # make sure home.py is in the same folder

def book_flight():
    # Get values from input fields
    name = name_entry.get()
    flight_number = flight_entry.get()
    departure = departure_entry.get()
    destination = destination_entry.get()
    date = date_entry.get()
    seat_number = seat_entry.get()

    # Validate (simple check)
    if not (name and flight_number and departure and destination and date and seat_number):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Save to database
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO reservations 
           (name, flight_number, departure, destination, date, seat_number) 
           VALUES (?, ?, ?, ?, ?, ?)""",
        (name, flight_number, departure, destination, date, seat_number)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Flight booked successfully!")

    # Clear fields after submission
    name_entry.delete(0, tk.END)
    flight_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    seat_entry.delete(0, tk.END)

def create_booking_window():
    global name_entry, flight_entry, departure_entry, destination_entry, date_entry, seat_entry, root
    root = tk.Tk()
    root.title("Book a Flight")
    root.geometry("800x500")   # Same size as home page
    root.configure(bg="white")

    label_font = ("Arial", 14, "bold")
    entry_font = ("Arial", 18)

    # --- Form Frame ---
    form_frame = tk.Frame(root, bg="white")
    form_frame.pack(fill="both", expand=True)

    tk.Label(form_frame, text="Book a Flight", font=("Arial", 20, "bold"),
             bg="white", fg="navy").pack(pady=10)

    # Labels + Entry fields
    tk.Label(form_frame, text="Passenger Name", font=label_font, bg="white", fg="navy").pack(pady=5)
    name_entry = tk.Entry(form_frame, width=40, font=entry_font)
    name_entry.pack(pady=5)

    tk.Label(form_frame, text="Flight Number", font=label_font, bg="white", fg="navy").pack(pady=5)
    flight_entry = tk.Entry(form_frame, width=40, font=entry_font)
    flight_entry.pack(pady=5)

    tk.Label(form_frame, text="Departure", font=label_font, bg="white", fg="navy").pack(pady=5)
    departure_entry = tk.Entry(form_frame, width=40, font=entry_font)
    departure_entry.pack(pady=5)

    tk.Label(form_frame, text="Destination", font=label_font, bg="white", fg="navy").pack(pady=5)
    destination_entry = tk.Entry(form_frame, width=40, font=entry_font)
    destination_entry.pack(pady=5)

    tk.Label(form_frame, text="Date (YYYY-MM-DD)", font=label_font, bg="white", fg="navy").pack(pady=5)
    date_entry = tk.Entry(form_frame, width=40, font=entry_font)
    date_entry.pack(pady=5)

    tk.Label(form_frame, text="Seat Number", font=label_font, bg="white", fg="navy").pack(pady=5)
    seat_entry = tk.Entry(form_frame, width=40, font=entry_font)
    seat_entry.pack(pady=5)

    # Submit button
    tk.Button(form_frame, text="Book Flight", width=20, height=2,
              font=("Arial", 14, "bold"),
              bg="navy", fg="white", command=book_flight).pack(pady=20)

    # --- Navigation Frame (Bottom) ---
    nav_frame = tk.Frame(root, bg="white")
    nav_frame.pack(fill="x", side="bottom")

    tk.Button(nav_frame, text="Back to Home",
              font=("Arial", 12, "bold"),
              bg="gray", fg="white",
              command=lambda: [root.destroy(), home.create_home_window()]
              ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_booking_window()
