import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM [Table Name]')
count = 0
for row in cur :
   print row
   count = count + 1
print count, 'rows.'
cur.close()