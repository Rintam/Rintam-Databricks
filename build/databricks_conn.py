from connection import get_connection

def execute_query(query):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

result=execute_query("select current_user")

print(result)
