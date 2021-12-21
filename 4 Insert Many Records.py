import sqlite3
connection = sqlite3.connect('customer.db')
c = connection.cursor()
#===================================

many_customers = [
    ('Joe', 'Thomas', 'Joeboi@us.com'),
    ('Saad', 'Mohd', 'SaadMohd@outlook.com'),
    ('David', 'Joseph', 'Davidjo@gmail.com')
]

#we use executemany instead of execute
# '?' is the placeholder for SQL
# ?,?,? is basically first_name, last_name and email
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


#===================================
print('Command executed :D')
connection.commit()
connection.close()