import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Record (Name, Age) VALUES ( ?, ? )', 
    ( 'James', 20 ) )
cur.execute('INSERT INTO Record (Name, Age) VALUES ( ?, ? )', 
    ( 'Mary', 15 ) )
conn.commit()

print 'Records:'
cur.execute('SELECT Name, Age FROM Record')
for row in cur :
   print row

cur.execute('DELETE FROM Record WHERE Age < 100')

cur.close()

