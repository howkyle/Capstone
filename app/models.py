from . import db


class Student(db.Model):
	studentID = db.Column(db.String, primary_key = True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	password = db.Column(db.String(50))
	csec_subjects = db.relationship("Studied", backref='student', cascade="all, delete-orphan" , lazy='dynamic')
	chosen_subjects = db.relationship("Application",backref='student', cascade="all, delete-orphan" , lazy='dynamic')
	assigned_subjects = db.relationship("SuccessfulApplication",backref='student', cascade="all, delete-orphan" , lazy='dynamic')
	authenticated = db.Column(db.Boolean, default = True)

	def is_authenticated(self):
		return self.authenticated

	def is_active(self):
		return True

	def is_anonymous(self):
		return False


	def get_id(self):
		return str(self.studentID)

	# def __init__(self, sid, fname, lname, password):
	# 	self.studentID = sid
	# 	self.first_name = fname
	# 	self.last_name = lname
	# 	self.password = password
	# 	self.csec_subjects =[]
	# 	self.chosen_subjects = []

	def __repr__(self):
		return "<Student %r>" %(self.studentID)


	@property
	def json(self):
		return {'id': self.studentID,'fname': self.first_name,'lname': self.last_name}


class Csec(db.Model):
	# id = db.Column(db.Integer, primary_key = True)
	subjectName = db.Column(db.String(50), primary_key  = True)
	studied = db.relationship("Studied")
	cape  = db.relationship("Cape")


class Studied(db.Model):
	id = db.Column(db.Integer(),primary_key = True)
	studentID= db.Column(db.String(50), db.ForeignKey('student.studentID'))
	grade = db.Column(db.String(5))
	subjectName=  db.Column(db.String(50),db.ForeignKey('csec.subjectName'))


class Cape(db.Model):
	# id = db.Column(db.Integer, primary_key = True)
	subjectName = db.Column(db.String(80), primary_key  = True)
	capacity = db.Column(db.Integer())
	prerequisiteSubject = db.Column(db.String(80), db.ForeignKey('csec.subjectName'))
	application = db.relationship("Application")
	successful_application = db.relationship("SuccessfulApplication")


class Application(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	studentID= db.Column(db.String(50), db.ForeignKey('student.studentID'))
	subjectName= db.Column(db.String(80),db.ForeignKey('cape.subjectName'))
	subjectPriority = db.Column(db.Integer())

class SuccessfulApplication(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	studentID= db.Column(db.String(50), db.ForeignKey('student.studentID'))
	subjectName= db.Column(db.String(80),db.ForeignKey('cape.subjectName'))
	


