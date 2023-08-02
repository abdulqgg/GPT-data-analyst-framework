import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('chinook.db')

# Create a cursor object
cur = con.cursor()

# Get the list of all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()

# Loop through all tables and print their names and headers
for table in tables[:-1]:
    with open('database-info.txt', 'a') as f:
        f.write(f"{table[0]}:")
        cur.execute('PRAGMA table_info({})'.format(table[0]))

        # Fetch all column details
        columns = cur.fetchall()
        
        # Print column names
        for column in columns:
            f.write(f"\n- {column[1]}")
        f.write("\n\n")

# Close the connection
con.close()
