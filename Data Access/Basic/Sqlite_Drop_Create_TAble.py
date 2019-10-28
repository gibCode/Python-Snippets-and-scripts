import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Record ')
cur.execute('CREATE TABLE Record (Name TEXT, Age INTEGER)')

conn.close()

