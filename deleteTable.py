import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Delete table
c.execute("DROP TABLE customers")  # Once dropped (deleted) the table is gone

# Commit changes to db
conn.commit()

# Close connection to db
conn.close()
