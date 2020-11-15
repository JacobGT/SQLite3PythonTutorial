import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Update record
# c.execute(""" UPDATE customers SET first_name = 'Jimmy'
#               WHERE first_name = 'customerName3'
#         """)
# The code in the lines above works, but it is not ideally and/or correct because there may be different records with
# similar parts; like in this case there may be a lot of customers with the name of 'customerName3'
# the best thing to do is to search it with the row id like this:
# First we search for the rowid
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

# Formatting the results
for item in items:
    print(item)

# Now that we know the rowid, we can use it with the WHERE
c.execute(""" UPDATE customers SET first_name = 'Jimmy'
              WHERE rowid = 2
        """)

# Commit changes to db
conn.commit()

# Only to verify that changes have been done we will print it to screen
c.execute("SELECT * FROM customers")

print(c.fetchall())

# Close connection to db
conn.close()
