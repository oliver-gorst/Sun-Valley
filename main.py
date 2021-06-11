#render_template is to use one template for all the pages, making the menu possible
from flask import Flask, render_template

#request is for 'get' request for using the user input in the converter
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/feature1")
def feature1():
    return render_template("feature1.html")

@app.route("/feature2")
def feature2():
    return render_template("feature2.html")

@app.route("/feature3")
def feature3():
    return render_template("feature3.html")


@app.route("/convert")
def index():
    feet = request.args.get("feet", "")
    if feet:
        meters = meters_from(feet)
    else:
        meters = ""
    return (
    """<form action="" method="get">
            Height in feet: <input type="text" name="feet"/>
            <input type="submit" value="Convert to meters"/>
        </form>"""
    + "Meters: "
    + meters
    )

def meters_from(feet):
    """Convert feet to meters."""
    try:
        meters = float(feet) / 3.28
        meters = round(meters, 2)  # Round to two decimal places
        return str(meters)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

