import sqlite3


conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS [TableName1] 
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS [TableName1] 
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')
