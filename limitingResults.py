import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Ordering results
# If there are too many records you can limit the results
c.execute("SELECT rowid, * FROM customers LIMIT 2")
# You can mix this with ordering results and other things
# Example: c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

# Commit changes to db
conn.commit()

# Only to verify that changes have been done we will print it to screen
c.execute("SELECT * FROM customers")

print(c.fetchall())

# Close connection to db
conn.close()
