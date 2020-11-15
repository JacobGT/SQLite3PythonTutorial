import sqlite3


# Query the DB and returning ALL records
def show_all():
    # Connect to database
    conn = sqlite3.connect("customers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT * FROM customers")
    items = c.fetchall()

    # Show results
    for item in items:
        print(item)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Add ONE new record to the table
def add_one(first, last, email):
    # Connect to database
    conn = sqlite3.connect("customers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Delete record from table
def delete_one(id):
    # Connect to database
    conn = sqlite3.connect("customers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("DELETE from customers WHERE ROWID = (?)", id)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Add MANY records to DB
def add_many(list_customers):
    # Connect to database
    conn = sqlite3.connect("customers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", list_customers)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Lookup with WHERE
# There are a zillion ways to lookup records with where, name, lastname, email, rowid, etc.
# so for learning/teaching purposes we will only do an email lookup0
def email_lookup(email):
    # Connect to database
    conn = sqlite3.connect("customers.db")

    # Create a cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT * FROM customers WHERE email = (?)", email)
    items = c.fetchall()

    # Show results
    for item in items:
        print(item)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create database
def create_database():
    import sqlite3

    # Connect to database
    conn = sqlite3.connect("customers.db")

    # Create a cursor
    c = conn.cursor()

    # Create a table
    c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

    # 'Commits' (saves) the things we just made to the db (database)
    conn.commit()

    # Close connection to avoid mistakes & errors / it is a good practice to make it manually
    conn.close()

# Please feel free to play with this code. Try adding and changing stuff. Enjoy ;) -JacobGT
