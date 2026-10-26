import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  
    user="root",
    password="Nikhil@2005",
    database="pythondb"
)

mycursor = conn.cursor()

sql = "insert into student(name, branch, id) values(%s, %s, %s)"

val = [("rohit", "cse", "56"), ("rohan", "ece", "57"), ("ritik", "mech", "58")]
mycursor.executemany(sql, val)
conn.commit()
print(mycursor.rowcount, "record inserted.")    
