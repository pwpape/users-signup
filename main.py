from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["GET","POST"])
def index():
    name = ""
    pass1= ""
    pass2 = ""
    email = ""
    valid_name = ""
    valid_pass = ""
    matching_pass = ""
    emailok = ""
    if request.method == "POST":
        name = request.form["name"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        email = request.form["email"]
        if name == "":
            valid_name = "Field required"
        else:
            valid_name = validate_userORpass(name)
        if pass1 == "":
            valid_pass = "Field required"
        else:
            valid_pass = validate_userORpass(pass1)
        if valid_pass == "":
            matching_pass = match_pass(pass1, pass2)
        if email != "":
            emailok = check_email(email)
        if valid_name == "" and valid_pass == "" and matching_pass == "" and emailok == "":
            return redirect("/validated")
    
    return render_template("form.html", name=name, name_error=valid_name, pass1="", pass1_error=valid_pass, pass2="", pass2_error=matching_pass, email=email, email_error=emailok)

def validate_userORpass(submission):
    if not re.match("...", submission):
        return "Must be at least 3 characters"
    elif re.match(".{21,}" , submission):
        return "Must be fewer than 20 characters"
    elif re.match(".*\s" , submission):
        return "Cannot contain spaces"
    else:
        return ""

def match_pass(pass1, pass2):
    if pass2 != pass1:
        return "Passwords must match"
    else: 
        return ""

def check_email(submission):
    if not re.match("...", submission):
        return "Must be at least 3 characters"
    elif re.match(".{21,}" , submission):
        return "Must be fewer than 20 characters"
    elif re.match(".*\s" , submission):
        return "Cannot contain spaces"
    else:
        return ""


@app.route("/validated", methods=["POST"])
def validated():
    return render_template("validated.html", name=name)

app.run()