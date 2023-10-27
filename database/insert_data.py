import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("INSERT INTO customers VALUES('vishu','kumar','vishu@gmail.com')")

c.execute("INSERT INTO customers VALUES('happy','kumar','happy@gmail.com')")

print("command run successfully")

conn.commit()
conn.close()