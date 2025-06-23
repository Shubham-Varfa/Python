import psycopg2 #connect to PostgreSQL databases

# postgres credencials
conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="1234"
)

# Create a cursor object: used to interact with the database
cursor = conn.cursor()

# Example: Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        age INT
    );
""")

# Example: Insert data
#cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 30))
#cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Lisa", 25))

# Commit changes
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Clean up
cursor.close()
conn.close()
