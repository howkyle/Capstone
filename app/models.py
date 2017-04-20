from . import db


class Student(db.Model):
	studentID = db.Column(db.String, primary_key = True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	password = db.Column(db.String(50))
	csec_subjects = db.relationship("Studied")
	chosen_subjects = db.relationship("Application")
	authenticated = db.Column(db.Boolean, default = True)

	def is_authenticated(self):
		return self.authenticated

	def is_active(self):
		return True

	def is_anonymous(self):
		return False


	def get_id(self):
		return str(self.studentID)

	def __repr__(self):
		return "<Student %r>" %(self.studentID)


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
	prequisiteSubject = db.Column(db.String(80), db.ForeignKey('csec.subjectName'))
	application = db.relationship("Application")


class Application(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	studentID= db.Column(db.String(50), db.ForeignKey('student.studentID'))
	subjectName= db.Column(db.String(80),db.ForeignKey('cape.subjectName'))


