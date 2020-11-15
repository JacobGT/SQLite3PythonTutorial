import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Delete record
# Like updating a record, we can use the rowid or any other method
c.execute("DELETE from customers WHERE rowid = 3")  # Do not forget to use the WHERE with the DELETE
# Once dropped (deleted) the thing is gone

# Commit changes to db
conn.commit()

# Only to verify that changes have been done we will print it to screen
c.execute("SELECT * FROM customers")

print(c.fetchall())

# Close connection to db
conn.close()
