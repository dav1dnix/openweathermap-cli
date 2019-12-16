import chalk
from pyfiglet import Figlet
import sqlite3
from sys import path
print(path)

# SQLite
path.insert(1, "../db")
from db import sqlite3db

def setup():
    fig = Figlet()
    print(chalk.blue(fig.renderText("weather-cli")))

    # Create array for appid key
    appid_input = input("What is your app_id? : ")
    if (len(appid_input) < 32):
        print("The app_id for openweathermap is 32 characters")
    elif (len(appid_input) >= 32):
        # Insert app_id into database
        sqlite3db(conn="config.db", exec_sql=f"INSERT INTO config VALUES ('{appid_input}')")

setup()
