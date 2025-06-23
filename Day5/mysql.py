import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="python_user",
    password="MyPassword123!",
    database="new"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM student")
for db in cursor:
    print(db)

conn.close()
