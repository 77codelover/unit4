##CREATE TABLE...


# import mysql.connector
# # from mysql.connector import Error
# try:
#     mydb = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "1234",
#         database = "SampleDB"
#     )
#     if mydb is None:
#         print("Your Database is not connected.....")
#     else:
#         print("Your Database is connected.....")

#     cursor = mydb.cursor()
#     cursor.execute("create table emp5(id varchar(10) primary key,name varchar(10),sal numeric(15))")
#     print("Employee table created")
# except mysql.connector.Error as e:
#         print(e)


##INSERT TABLE...


# import mysql.connector
# try:
#     mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "1234",
#     database = "SampleDB"
#     )
#     if mydb is None:
#         print("Database not connectivity....")
#     else:
#         print("Database connectivity....")

#     cursor = mydb.cursor()
#     cursor.execute("insert into emp5 values('E001','Rahul','50000')")
#     cursor.execute("insert into emp5 values('E002','Raj','60000')")
#     cursor.execute("insert into emp5 values('E003','Ram','70000')")
#     cursor.execute("insert into emp5 values('E004','Raghu','20000')")
#     print("New Table created")
#     mydb.commit()
# except mysql.connector.Error as e:
#     print(e)
    

                   
    
##RETRIVE DATA....
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = "root",
        password = "1234",
        database = "SampleDB"
    )
    if mydb is None:
        print("Database not connected....")
    else:
        print("Database is connected...")
    cursor = mydb.cursor()
    cursor.execute("select * from emp5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    mydb.commit()
except mysql.connector.Error as e:
    print(e)