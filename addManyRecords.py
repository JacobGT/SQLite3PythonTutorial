import sqlite3

# Connect to database
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Create python list with customer info
many_customers = [
                 ('customerName1', 'customerLastName1', 'customer1@email.com'),
                 ('customerName2', 'customerLastName2', 'customer2@email.com'),
                 ('customerName3', 'customerLastName3', 'customer3@email.com'),
               ]

# Insert many records to table
# In sqlite the "?" question mark is the place holder
c.executemany("INSERT INTO customers VALUES (?,?, ?)", many_customers)

# Commit changes to db
conn.commit()

# Close connection to db
conn.close()
