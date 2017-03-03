
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import UserProfile

@app.route('/')
def home():
	return render_template("home.html")



#handles routing of webpages

