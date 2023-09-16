import pymysql

try:
    # Establish a database connection
    dataBase = pymysql.connect(
        host='localhost',
        user='root',
        passwd='**********' #Add ur  Password to connect to MYSQL DATABASE
    )

    # Create a cursor using a context manager
    with dataBase.cursor() as cursorObject:
        # Create the 'elderco' database
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

    print("Database 'elderco' created successfully.")

except pymysql.Error as err:
    print(f"Error: {err}")


