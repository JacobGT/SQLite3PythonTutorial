import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Query the database (db)
# We want to fetch only certain things from the db, so we use the where function
c.execute("SELECT * FROM customers WHERE first_name LIKE 'customer%' ")
# A comparison operator used a lot is: LIKE / which compares to similar results and have to end with % or start with %
# Example: WHERE email LIKE '%customer'
# We can also use all of the other comparison operators like: >, <, ==, >=, etc.

items = c.fetchall()

# Formatting the results
for item in items:
    print("Name: " + item[0] + "\tLast Name: " + item[1] + "\tEmail: " + item[2])
    # We also can just do: print(item)

# Commit changes to db
conn.commit()

# Close connection to db
conn.close()
