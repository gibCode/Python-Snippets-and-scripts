import sys

conn = ogr.Open("PG:host='108.163.190.66' dbname='world' user ='user1' password='123'")

#test the connection
if conn is None:
    print 'Coul not open database'
    sys,exit(1)
    
#query to obtain layers
layer = conn.ExecuteSQL("SELECT * FROM countries ")

print "Number: %d" %(layer.GetFeatureCount())
