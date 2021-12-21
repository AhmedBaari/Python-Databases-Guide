import sqlite3
connection = sqlite3.connect('customer.db')
c = connection.cursor()

c.execute("INSERT INTO customers VALUES('Ahmed', 'Baari', 'ahmed4baari@gmail.com')")
c.execute("INSERT INTO customers VALUES('Tejas', 'Ranju', 'thejuice123@gmail.com')")
print('Command executed :D')

#Commit and Close
connection.commit()
connection.close()