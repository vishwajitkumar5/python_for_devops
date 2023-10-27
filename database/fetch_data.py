import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("SELECT * FROM customers")

print(c.fetchall())

print("command run successfully")
conn.commit()
conn.close()