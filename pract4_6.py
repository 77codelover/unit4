import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
)
print(mydb)
try:
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE Sample_DB1")
    cursor.execute("show databases")
    my = cursor.fetchall()
    print("Databade created \n")
    for i in my:
        print(i)
except error as e:
    print(e)
