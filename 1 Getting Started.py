import sqlite3

#Permanent database saved in directory
connection = sqlite3.connect('customer.db')

#Temporary database in memory
#conn = sqlite3.connect(':memory:')

# Running the code creates the Database