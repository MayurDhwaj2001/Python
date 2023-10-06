import mysql.connector

mysql = mysql.connector.connect(host="localhost", user="root", passwd="", database="test")

mycursor = mysql.cursor()

mycursor.execute("select * from students")

result = mycursor.fetchall()
# result2 = mycursor.fetchone()

for i in result:
    print(i)

