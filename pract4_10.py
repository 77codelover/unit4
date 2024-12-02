import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user ="root",
        password="1234",
        database="SampleDB"
    )
    if mydb is None:
        print("Database not connected")
    else:
        print("Database connected")
    cursor = mydb.cursor()
    
    id = input("Enter Employee id: ")
    increment = int(input("Enter Increment Amount: "))
    query = "update emp5 set sal = sal +%s where id = %s"
    val =(increment,id)
    cursor.execute(query,val)
    print("Record Updated...")
    mydb.commit()
except mysql.connector.Error as e:
    print(e)