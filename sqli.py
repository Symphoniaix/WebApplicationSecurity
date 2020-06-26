import sqlite3
# Relevent xkcd: https://xkcd.com/327/
conn = sqlite3.connect('example.db')

conn.execute("CREATE TABLE IF NOT EXISTS users (name text, surname text)")
cursor = conn.cursor()
name = input("name:")
surname = input("surname:")

# Unsecure database interaction
cursor.executescript("INSERT INTO users VALUES('" + name + "', '" + surname + "')")
# if user input surname is "'); DROP TABLE users; --" table is dropped

# Secure database interaction
cursor.execute("INSERT INTO users VALUES(?,?)", (name, surname))
# Even if the user input is "'); DROP TABLE users; --"
# input is not executed and only stored as string 

conn.commit()
conn.close()