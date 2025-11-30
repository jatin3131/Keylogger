import mysql.connector
from mysql.connector import Error

# MySQL connection configuration
MYSQL_CONFIG = {
    'host': 'localhost',
    'database': 'SPYWARE',
    'user': 'root',
    'password': 'jatinsql31'
}

def connect_to_mysql():
    """Establish a connection to MySQL."""
    try:
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_key_log(cursor, timestamp, activity, keyLog):
    """Insert a record into the keyLogs table."""
    query = "INSERT INTO keyLogs (timestamp, activity, keyLog) VALUES (%s, %s, %s)"
    values = (timestamp, activity, keyLog)
    cursor.execute(query, values)

def process_key_logs(file_path, cursor):
    """Read and insert key logs from the file."""
    with open(file_path, 'r') as file:
        for line in file:
            # Parse each line in the format: "HH:MM:SS key presses Key.enter"
            try:
                parts = line.strip().split(' ', 2)  # Split into timestamp, activity, and keyLog
                if len(parts) == 3:
                    timestamp = parts[0]  # HH:MM:SS
                    activity = parts[1]   # 'key'
                    keyLog = parts[2]     # Key pressed
                    insert_key_log(cursor, timestamp, activity, keyLog)
            except Exception as e:
                print(f"Error processing line: {line} | Error: {e}")

def main():
    # Establish a connection to MySQL
    connection = connect_to_mysql()
    
    if connection:
        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Process the key_logs.txt file and insert data
        process_key_logs("key_logs.txt", cursor)

        # Commit the changes to the database
        connection.commit()
        print("Data inserted successfully!")

        # Close the cursor and connection
        cursor.close()
        connection.close()
    else:
        print("Could not connect to the database.")

if __name__ == "__main__":
    main()
