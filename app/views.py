
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import *
from models import *
import json

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/signup',methods =["GET","POST"])
def signUp():
	form = SignUpForm()
	if request.method == "POST":
		print("post \n\n\n\n\n")
		if form.validate_on_submit():
			fname = form.fname.data
			lname = form.lname.data
			print (lname)
			studID = form.studentID.data
			password = form.confPassword.data

			student = Student(studentID = studID, first_name = fname, last_name = lname, password = password)
			db.session.add(student)
			db.session.commit()
			return redirect(url_for('login'))

	return render_template("signup.html", form = form)

@app.route('/login', methods=["GET","POST"])
def login():
	form = LoginForm()
	if request.method== "POST":
		if form.validate_on_submit():
			studentID = form.studentID.data
			password = form.password.data
			student = Student.query.filter_by(studentID = studentID, password = password).first()
			if student:
				login_user(student)
				print("login in successful")
				return redirect(url_for('profile'))

	return render_template("login.html", form = form), 

@app.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
	studentID = current_user.get_id()
	if request.method == "POST":
		print "POST"
		print request.headers["Content-Type"]
		if request.headers["Content-Type"] == 'csec-subjects':
			csecSubjects = json.loads(request.data)
			for sub in csecSubjects:
				db.session.add(Studied(studentID = studentID,grade = sub['grade'],subjectName=sub['subjectName']))
			db.session.commit()

			return jsonify(request.data)

		if request.headers["Content-Type"] == 'cape-subjects':
			capeSubjects = json.loads(request.data)
			for sub in capeSubjects:
				db.session.add(Application(studentID = studentID,subjectName=sub['subjectName']))
			db.session.commit()
			
			return jsonify(request.data)


	elif request.method  == "GET":

		if request.headers['Accept'] =="csec-list":
			# returns list of csec subjects from the database to the angular front end
			sub_list = []
			subjects = Csec.query.all()
			for subject in subjects:
				sub_list.append(str(subject.subjectName))

			return jsonify(sub_list)

		if request.headers['Accept'] == "cape-list":
			# returns list of cape subjects from the database to the angular front end
			sub_list = []
			subjects = Cape.query.all()
			for subject in subjects:
				# print subject
				sub_list.append(str(subject.subjectName))

			return jsonify(sub_list)

		student = Student.query.filter_by(studentID= studentID).first()
		if student:
			return render_template("profile.html", student = student)

@login_manager.user_loader
def load_user(id):
    return Student.query.get(str(id))

@app.route("/logout", methods = ["GET","POST"])
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))



#handles routing of webpages

