import sqlite3
connection = sqlite3.connect('customer.db')
c = connection.cursor()
#===================================

#Query the Database: Display 
c.execute("SELECT * FROM customers")

#Methods to fetch
#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

#Get first element
print(c.fetchone())

#Get first 3 elements
print(c.fetchmany(3))

#Fetch all elements
print(c.fetchall())


#===================================
print('Command executed :D')
connection.commit()
connection.close()