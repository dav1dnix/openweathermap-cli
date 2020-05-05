from flask import Flask, render_template

import sys
sys.path.append("../")

from index import weather 

w = weather("london")

class Weather:
    def __init__(self, location, weather, temp, country):
        self.location = location
        self.weather = weather
        self.temp = temp
        self.country = country

# Data

# Change kelvin to celsius
K = 273.15

location = f"Location: {w['name']}"
weather = f"Weather: {w['weather'][0]['description']}"
country = f"Country: {w['sys']['country']}"
temp = f"Temperature: {round(w['main']['temp'] - K, 2)}°c"
tempFeelsLike = f"Temperature feels like: {round(w['main']['feels_like'] - K, 2)}°c"
print(tempFeelsLike)

# Instance of class Flask
# needed so Flask knows where to look for static files etc
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
