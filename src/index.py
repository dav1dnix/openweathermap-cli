import requests
import pprint
import chalk
import sqlite3

peepee = pprint.PrettyPrinter(indent=4)

def weather(location):
	url = "https://api.openweathermap.org/data/2.5/weather?q="
	appid = ""
	response = requests.get(f"{url}{location}{appid}")
	print(response.json())

# Call function weather
weather("London")
