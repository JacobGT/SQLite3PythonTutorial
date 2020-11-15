# Sqlite all ready come included with python
import sqlite3  # We import sqlite3

# Connect to database if existent or creates a new database if nonexistent
conn = sqlite3.connect("customers.db")

# Create a cursor
c = conn.cursor()

# Create a table
# In this case 'customers' is the name of the database / a database is LIKE a spreadsheet
# then you enter the name of variable in table and the datatype
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
)""")
# Sqlite only has 5 datatype (although other databases like MySql have dozens more)
# SQLite DataTypes are:
# NULL (does it exist or doesnt),
# INTEGER (any whole number)
# REAL (any decimal number)
# TEXT (any text)
# BLOB (it is stored exactly like it is) (an image, mp3, etc. are some examples of blobs)

# 'Commits' (saves) the things we just made to the db (database)
conn.commit()

# Close connection to avoid mistakes & errors / it is a good practice to make it manually
conn.close()
