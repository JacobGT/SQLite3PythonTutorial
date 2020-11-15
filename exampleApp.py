import databaseAppFunc

# We will need the other .py file to use the functions defined there / here we will only run the functions
# The try excepts in this code are REALLY basic, try editing it if you wish.

leave = False
while leave != True:
    print("\nWelcome to our example app.")
    print("""Options:
    1. Create database (for first runs)
    2. Add one record to database
    3. Add many (3) records to database
    4. Show records in database
    5. Search a record in database with email
    6. Delete one record from database
    0. Exit
    -----------------------------------------------------
    """)
    option = int(input("Enter option: "))

    if option == 1:
        # Create DB
        try:
            databaseAppFunc.create_database()
        except:  # This except is in case the database is all ready created / try adding try excepts in the rest of code
            print("Database all ready created or other error.")

    elif option == 2:
        # Add a record to database
        try:
            first = input("Enter the first name of the user: ")
            last = input("Enter the last name of the user: ")
            email = input("Enter the email of the user: ")
            databaseAppFunc.add_one(first, last, email)
        except:
            print("Database has not been created or any other Unknown Error.")

    elif option == 3:
        # Add many records
        try:
            first1 = input("Enter the first name of the user: ")
            last1 = input("Enter the last name of the user: ")
            email1 = input("Enter the email of the user: ")

            first2 = input("Enter the first name of the user: ")
            last2 = input("Enter the last name of the user: ")
            email2 = input("Enter the email of the user: ")

            first3 = input("Enter the first name of the user: ")
            last3 = input("Enter the last name of the user: ")
            email3 = input("Enter the email of the user: ")

            stuff = [
                (first1, last1, email1),
                (first2, last2, email2),
                (first3, last3, email3)
            ]
            databaseAppFunc.add_many(stuff)
        except:
            print("Database has not been created or any other Unknown Error.")

    elif option == 4:
        # Show all records from db
        try:
            databaseAppFunc.show_all()
        except:
            print("Database has not been created or any other Unknown Error.")

    elif option == 5:
        # Lookup email in our database
        try:
            email_look = str(input("Enter email you wish to look up: "))
            databaseAppFunc.email_lookup(email_look)
        except:
            print("No user registered with that email, database has not been created or any other Unknown Error.")

    elif option == 6:
        # Delete record / we need to pass rowid as String to avoid error
        try:
            id_delete = str(input("Enter the id of the record you wish to delete: "))
            databaseAppFunc.delete_one(id_delete)
        except:
            print("Database has not been created or any other Unknown Error.")

    else:
        print("It is sad to see you go so soon. :(")
        print("I hope you enjoyed this program, and hope to see you soon. Bye! :)")
        leave = True
