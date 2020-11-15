import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Query the database (db)
c.execute("SELECT * FROM customers")

# The fetch command brings out the results as a tuple inside a python list, so you can access it like that ex. ()[#]
items = c.fetchall()

# Formatting the results
for item in items:
    print("Name: " + item[0] + "\tLast Name: " + item[1] + "\tEmail: " + item[2])
    # We also can just do: print(item)

# Commit changes to db
conn.commit()

# Close connection to db
conn.close()
