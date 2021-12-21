import sqlite3
connection = sqlite3.connect('customer.db') #makes file if it doesn't exist

#To do anything, we need a cursor to do it. Let's make a cursor instance.
#Create Cursor
c = connection.cursor()

#Creating a Table 
# #docstrings, multiple lines of code
c.execute(""" CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
)""")

#We can use this too
#c.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")

# NULL = Doesn't exist
# INTEGER = 100, 374
# REAL = 10.3, 382.94
# TEXT = Hello
# BLOB = Stored as it is (Images, mp3, etc.)

#Now let's commit the connection to the database
connection.commit()

#Close the connection (it closes by itself but we'll do it for best practices)
connection.close()