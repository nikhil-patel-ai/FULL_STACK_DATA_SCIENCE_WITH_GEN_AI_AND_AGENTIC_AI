import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  
    user="root",
    password="Nikhil@2005",
    #database="your_database"
)

mycursor = conn.cursor()
mycursor.execute("show databases")

for db in mycursor:
    print(db)