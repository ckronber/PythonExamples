from flask import Blueprint, render_template,redirect,url_for

auth = Blueprint("auth",__name__)

@auth.route("/login")
def login():
    return render_template("Login.html")

@auth.route("/sign-up")
def sign_up():
    return render_template("signUp.html")

@auth.route("/logout")
def logOut():
    return redirect(url_for("views.home"))