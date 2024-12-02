import mysql.connector
try:
    # Establish a connection to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database = "SampleDB"
    )
    if mydb is None:
        print("Connection failed")
    else:
        print("Connected to the database")
    cursor = mydb.cursor()
    # insert data dynamically...
    while('True'):
        choice = input("Would you like to enter record: ")
        if choice == 'Yes' or choice == 'yes':
            id = input("Enter Employee id: ")
            name = input("Enter Employee name: ")
            sal = int(input("Enter Employee salary: "))
            query = "INSERT INTO emp5 (id, name, sal) VALUES (%s, %s, %s)"
            val = (id,name,sal)
            cursor.execute(query,val)
            mydb.commit()
        elif choice == 'No' or 'no':
            break
        else:
            print("Invalid Input....")
except mysql.connector.Error as e:
    print(e)