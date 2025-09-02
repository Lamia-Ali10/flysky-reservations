import tkinter as tk   # Import Tkinter
import booking         # Import booking file
import reservations    # Import reservations file

def open_booking_page():
    root.destroy()  # close Home before opening new window
    booking.create_booking_window()

def open_reservations_page():
    root.destroy()  # close Home before opening new window
    reservations.create_reservations_window()

def create_home_window():
    global root
    # Create the main window
    root = tk.Tk()
    root.title("FlySky Reservations")   # Window title
    root.geometry("800x500")            # Window size (width x height)

    # Title label
    title_label = tk.Label(root, text="Welcome to FlySky Reservations",
                           font=("Arial", 24, "bold"),
                           fg="navy")
    title_label.pack(pady=20)  # pady = padding (space around)

    # Book Flight button
    book_button = tk.Button(root, text="Book a Flight",
                            width=25, height=3,
                            font=("Arial", 12, "bold"),
                            fg="white", bg="navy",
                            command=open_booking_page)
    book_button.pack(pady=20, ipadx=10, ipady=10)

    # View Reservations button
    view_button = tk.Button(root, text="View Reservations",
                            width=25, height=3,
                            font=("Arial", 12, "bold"),
                            fg="white", bg="navy",
                            command=open_reservations_page)
    view_button.pack(pady=20, ipadx=10, ipady=10)

    # Run the Tkinter event loop
    root.mainloop()

# Run the window if this file is executed directly
if __name__ == "__main__":
    create_home_window()
