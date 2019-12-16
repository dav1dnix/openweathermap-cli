import requests
import chalk
import sqlite3
import argparse

from sys import path

# This inserts the path in sys.path second to the first value. This guarentees that this path is
# searched before others
path.insert(1, "../db")

# From package (db directory) import function (sqlite3db) from module (db.py)
from db import sqlite3db

# Runs the sqlite3db function with these keyword arguments.
x = sqlite3db(conn="../db/config.db", exec_sql="SELECT * FROM config")

def weather(location):
	url = "https://api.openweathermap.org/data/2.5/weather?q="
	appid = f"&appid="
	response = requests.get(f"{url}{location}{appid}")
	# print(response.json())
# Call function weather
weather("London")
