import sqlite3

def sqlite3db(conn, exec_sql): # Table=config, column=app_id 
    connect = sqlite3.connect(conn)
    cursor = connect.cursor()
    executed = cursor.execute(exec_sql).fetchall()

    connect.close()

    # If sql query in exec_sql do sql query, else return str
    if (len(exec_sql)):
        api_key = [print(x[0]) for x in executed]
        return api_key
    else:
        return ("You must specify something to execute")

# If being run directly
if __name__ == "__main__":
    sqlite3db(conn="config.db", exec_sql="SELECT * FROM config")
else:
    pass