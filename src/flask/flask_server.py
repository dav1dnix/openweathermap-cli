from flask import Flask, render_template

# Instance of class Flask
# needed so Flask knows where to look for static files etc
app = Flask(__name__)

@app.route("/")
def root():
    message = "Hello Flask!"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
