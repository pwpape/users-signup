from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("form.html")


def validate():
    name = request.form["name"]
    pass1 = request.form["pass1"]
    pass2 = request.form["pass2"]
    email = request.form["email"]

    return render_template("validated.html", name=name)



@app.route("/validate")
def validated():
    name = request.form["name"]
    return render_template("validated.html", name=name)

app.run()