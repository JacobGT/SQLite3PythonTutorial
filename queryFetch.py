import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Query the database (db)
c.execute("SELECT * FROM customers")

# .fetchone() == fetches the last item
# .fetchmany() == fetches how many you tell it on parameters
# .fetchall() == fetches all
print(c.fetchall())  # It is returned as a python list

# Commit changes to db
conn.commit()

# Close connection to db
conn.close()
