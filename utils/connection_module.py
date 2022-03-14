import os

from psycopg import connect, OperationalError


def create_connection():
    try:
        connection_object = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return connection_object
    except OperationalError:
        return "Could not connect to database"


connection = create_connection()
print(connection)
