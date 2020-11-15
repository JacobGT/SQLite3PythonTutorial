import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Ordering results
# AND & OR add more conditions to your WHERE cause
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'custumer%' AND rowid = 2")
# This works like any logical condition

# Commit changes to db
conn.commit()

# Only to verify that changes have been done we will print it to screen
c.execute("SELECT * FROM customers")

print(c.fetchall())

# Close connection to db
conn.close()
