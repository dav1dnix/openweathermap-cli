from flask import Flask

# Instance of Flask class
app = Flask(__name__)

@app.route("/")
def hi():
    return "hello"
