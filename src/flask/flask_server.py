from flask import Flask, render_template, request
from os import getenv

import sys
sys.path.append("../")

from index import weather 

# Change kelvin to celsius
K = 273.15

# Instance of class Flask
# needed so Flask knows where to look for static files etc
app = Flask(__name__)

w = weather

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def testfunction():
    weather = request.form["weather"]
    return w(weather)
    
@app.route("/test")
def a():
    return f'key: { getenv("API_KEY") }'

if __name__ == "__main__":
    app.run(debug=True)
