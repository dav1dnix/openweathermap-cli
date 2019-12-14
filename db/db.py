import sqlite3

conn = sqlite3.connect("config.db")

# Allows execution of SQL commands
cursor = conn.cursor()

# cursor.execute("CREATE TABLE config ('app_id')")

x = cursor.execute("SELECT * FROM config")
print(x.fetchall())

# Save (commit changes)
# conn.commit()

# Close connection
conn.close()