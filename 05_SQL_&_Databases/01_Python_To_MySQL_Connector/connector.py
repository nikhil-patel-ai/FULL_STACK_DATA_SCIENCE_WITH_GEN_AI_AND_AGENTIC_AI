import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  
    user="root",
    password="Nikhil@2005",
    #database="your_database"
)

if conn.is_connected():
    print("Connected to MySQL database")   
print(conn)
print(conn.is_connected)
