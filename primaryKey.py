import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Query the database (db)
# A primary key is a unique id number that each record from the database gets / in SQLite it is called row id
# In most databases you have to create the primary key yourself and an automatic increasing counter
# But this sqlite has it included all ready, and you can show it with the following code
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()


# Formatting the results
for item in items:
    print("Name: " + item[0] + "\tLast Name: " + item[1] + "\tEmail: " + item[2])
    # We also can just do: print(item)

# Commit changes to db
conn.commit()

# Close connection to db
conn.close()
