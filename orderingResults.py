import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Ordering results
# By default the database order the results by the rowid in ascending order
c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
# The keyword to ordering are:
# ASC == ascending
# DESC == descending
# and you can combine and mix them like: ex. ORDER BY last_name DESC

# Commit changes to db
conn.commit()

# Only to verify that changes have been done we will print it to screen
c.execute("SELECT * FROM customers")

print(c.fetchall())

# Close connection to db
conn.close()
