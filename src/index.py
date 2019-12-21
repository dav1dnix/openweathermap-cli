import requests
import chalk
import json
import argparse

with open("./config.json") as json_file:
	x = json.load(json_file)

parser = argparse.ArgumentParser(description="Get information about the weather")

# --location argument
parser.add_argument("--location", "-l", type=str, help="location", metavar="", required=True)

arguments = parser.parse_args()

def weather(location):
	url = "https://api.openweathermap.org/data/2.5/weather?q="
	api_key = f"&appid={x['api_key']}"
	response = (f"{url}{location}{api_key}")
	return requests.get(response).json()

if __name__ == "__main__":
	print(weather(arguments.location))
