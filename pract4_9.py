import mysql.connector

try:
    # Establish a connection to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="SampleDB"
    )
    if mydb.is_connected():
        print("Connected to the database")
    else:
        print("Connection failed")

    cursor = mydb.cursor()

    # Delete data dynamically...
    id = input("Enter Employee id: ")
    query = "DELETE FROM emp5 WHERE id = %s"
    val = (id,)  # Tuple with one element
    cursor.execute(query, val)
    
    mydb.commit()
    print("1 Row Deleted...")

except mysql.connector.Error as e:
    print(f"Error occurred: {e}")
    mydb.rollback()

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")
