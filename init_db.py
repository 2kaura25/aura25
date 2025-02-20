import psycopg2

# PostgreSQL database configuration
DB_NAME = "events_db"
DB_USER = "postgres"  # Change if you set a different username
DB_PASSWORD = "1919"  # Replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

# Function to connect to PostgreSQL and create tables
def create_tables():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()

    # Create tables for different events
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cipher_chase (
            id SERIAL PRIMARY KEY,
            team_name VARCHAR(100),
            member1_name VARCHAR(100),
            member1_department_and_year VARCHAR(100),
            member2_name VARCHAR(100),
            member2_department_and_year VARCHAR(100)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scrunch_and_pick (
            id SERIAL PRIMARY KEY,
            team_name VARCHAR(100),
            member1_name VARCHAR(100),
            member1_department_and_year VARCHAR(100),
            member2_name VARCHAR(100),
            member2_department_and_year VARCHAR(100)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ryz_n_fall (
            id SERIAL PRIMARY KEY,
            team_name VARCHAR(100),
            member1_name VARCHAR(100),
            member1_department_and_year VARCHAR(100),
            member2_name VARCHAR(100),
            member2_department_and_year VARCHAR(100),
            member3_name VARCHAR(100),
            member3_department_and_year VARCHAR(100)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dalgona (
            id SERIAL PRIMARY KEY,
            player_name VARCHAR(100),
            department_and_year VARCHAR(100)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS booth (
            id SERIAL PRIMARY KEY,
            team_name VARCHAR(100),
            member1_name VARCHAR(100),
            member1_department_and_year VARCHAR(100),
            member2_name VARCHAR(100),
            member2_department_and_year VARCHAR(100)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS moviemania (
            id SERIAL PRIMARY KEY,
            team_name VARCHAR(100),
            member1_name VARCHAR(100),
            member1_department_and_year VARCHAR(100),
            member2_name VARCHAR(100),
            member2_department_and_year VARCHAR(100),
            member3_name VARCHAR(100),
            member3_department_and_year VARCHAR(100)
        );
    ''')

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully!")

# Run the function
if __name__ == "__main__":
    create_tables()
