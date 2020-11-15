import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a curso
c = conn.cursor()

# Insert one record to table
c.execute("INSERT INTO customers VALUES ('customerName', 'customerLastName', 'customer@email.com')")

# Commit changes to db
conn.commit()

# Close connection to db
conn.close()
