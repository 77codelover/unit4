import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "SampleDB"
    )

#check database is connected or not?
    if mydb is None:
        print ("Database not connected...")
    else:
        print("Database is connected..")
        cursor = mydb.cursor()
    cursor.execute("create table new_employee_tbl(eno int,ename char(30),gender char(1),salary float)")
    print("New table created")
    mydb.commit()
except mysql.connector.Error as e:
    print(e)
    