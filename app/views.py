
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import *

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/signup',methods =["GET","POST"])
def signUp():
	form = SignUpForm()
	return render_template("signup.html", form = form)
@app.route('/login', methods=["GET","POST"])
def login():
	pass



#handles routing of webpages

