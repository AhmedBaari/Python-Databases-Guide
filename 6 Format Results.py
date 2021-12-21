import sqlite3
connection = sqlite3.connect('customer.db')
c = connection.cursor()
#===================================
#Query the Database: Display 
c.execute("SELECT * FROM customers")

#Access elements inside the tuple
print(c.fetchone()[0])

#Now let's try to 


#===================================
print('Command executed :D')
connection.commit()
connection.close()