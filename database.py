import sqlite3

def create_database():
    # Connect to SQLite (this will create flights.db if it doesn’t exist yet)
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()

    # Create a table called reservations (if it doesn’t exist already)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)

    # Save changes and close connection
    conn.commit()
    conn.close()
    print("Database and table created successfully!")

# Run the function when you execute database.py
if __name__ == "__main__":
    create_database()

