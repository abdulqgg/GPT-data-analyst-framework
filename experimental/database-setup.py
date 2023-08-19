import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('northwind.db')

# Create a cursor object
cur = con.cursor()

# Get the list of all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()

# Loop through all tables and print their names and headers
for table in tables[:-1]:
    with open('northwind-info.txt', 'a') as f:
        f.write(f"{table[0]}:")
        cur.execute(f'PRAGMA table_info("{table[0]}")')  # Quote the table name

        # Fetch all column details
        columns = cur.fetchall()

        # Print column names
        for column in columns:
            f.write(f"\n- {column[1]}")
        f.write("\n\n")

# Close the connection
con.close()
