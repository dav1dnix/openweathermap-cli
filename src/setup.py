import chalk
from pyfiglet import Figlet
import sqlite3

# SQLite
# Connect to db stored in db path
conn = sqlite3.connect("../db/config.db")

# Allow for execution of sql statements
cursor = conn.cursor()

def setup():
    fig = Figlet()
    print(chalk.blue(fig.renderText("weather-cli")))

    # Create array for appid key
    appid_input = input("What is your app_id? : ")
    if (len(appid_input) < 32):
        print("test")
    else:
        # Insert app_id into database
        cursor.execute(f"INSERT INTO config VALUES ('{appid_input}')")
        
        x = cursor.execute("SELECT * FROM config")
        print(x.fetchall())

        # Save x into db
        conn.commit()

        conn.close()
setup()
