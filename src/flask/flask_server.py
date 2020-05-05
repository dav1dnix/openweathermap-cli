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
location = w["name"]
weather = w["weather"][0]["description"]
country = w["sys"]["country"]
temp = w["main"]["temp"]
tempFeelsLike = w["main"]["feels_like"]
print(temp)

# Instance of class Flask
# needed so Flask knows where to look for static files etc
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
