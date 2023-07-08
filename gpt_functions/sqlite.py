import sqlite3

def execute_sql_query(database, query):
    """
    Execute an SQL query on a SQLite database.

    Args:
        database (str): The path to the SQLite database file.
        query (str): The SQL query to execute.

    Returns:
        list: The result of the SQL query.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(database)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Execute the SQL query
        cursor.execute(query)

        # Fetch all rows from the result set
        result = cursor.fetchall()

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return result

    except Exception as e:
        # Rollback the changes and close the connection if an error occurs
        conn.rollback()
        conn.close()

        raise e

def execute_sql_query_schema():
    return {
        "name": "execute_sql_query",
        "description": "Execute an SQL query on a SQLite database",
        "parameters": {
            "type": "object",
            "properties": {
                "database": {
                    "type": "string",
                    "description": "The path to the SQLite database file"
                },
                "query": {
                    "type": "string",
                    "description": "The SQL query to execute"
                }
            },
            "required": ["database", "query"]
        }
    }

