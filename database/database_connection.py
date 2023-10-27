import sqlite3

conn = sqlite3.connect('customer.db')


c = conn.cursor()

#create a table


c.execute("""
    CREATE TABLE customers (
          first_name TEXT,
          last_name TEXT,
          email TEXT    
    )
""")

print("command run successfully")
conn.commit()
conn.close()