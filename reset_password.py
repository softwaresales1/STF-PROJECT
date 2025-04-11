import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    dbname='postgres',  # Connect to the default database
    user='postgres',    # Superuser
    password='your_superuser_password',  # Replace with your superuser password
    host='localhost',
    port='5432'
)

# Create a cursor object
cur = conn.cursor()

# Reset the password for the user "ADMIN"
cur.execute("ALTER USER ADMIN WITH PASSWORD 'TempPassword123';")

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
