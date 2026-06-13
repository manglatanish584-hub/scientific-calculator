from flask import Flask, render_template, request
import math

import math

allowed_names = {}
allowed_names.update(vars(math))

app = Flask(__name__)

# allow math functions properly
allowed_names = {}
allowed_names.update(vars(math))  # adds sin, cos, tan, log, log10, sqrt, etc.

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    expression = request.form["expression"]

    try:
        result = eval(expression, {"__builtins__": None}, allowed_names)
    except Exception as e:
        result = "Error"

    return render_template("index.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)