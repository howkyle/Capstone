from . import db

class Student(db.Model):
	studentID = db.Column(db.String, primary_key = True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	password = db.Column(db.String(50))
	csec_subjects = db.relationship("Studied")
	authenticated = db.Column(db.Boolean, default = False)

	def is_authenticated(self):
		return self.autheicated

	def is_active(self):
		return True

	def is_anonymous(self):
		return False


	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return "<Student %r>" %(self.studentID)

class CsecSubject(db.Model):
	subjectName = db.Column(db.String(50), primary_key =True)
	studied = db.relationship("Studied")

class Studied(db.Model):
	id = db.Column(db.Integer(),primary_key = True)
	studentID= db.Column(db.String(50), db.ForeignKey('student.id'))
	subjectName=  db.Column(db.String(50),db.ForeignKey('csecsubject.subjectName'))

class CapeSubject(db.Model):
	subjectName = db.Column(db.String(80), primary_key = True)
	application = db.relationship("Application")

class Application(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	studentID= db.Column(db.String(50), db.ForeignKey('student.id'))
	subjectName=  db.Column(db.String(50),db.ForeignKey('capesubject.subjectName'))


