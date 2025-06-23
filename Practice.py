import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = '1234',
    database = 'postgres'
)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE student(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT 
     )
''')

cursor.execute('''
    INSERT INTO student (name, age) VALUES
        ('Krishna', 25),
        ('Shantanu', 30)
''')

cursor.execute('''
    SELECT * FROM student             
''')

for row in cursor:
    print(row)

conn.close()
cursor.close()