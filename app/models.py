from . import db

class UserProfile(db.Model):
	id = db.Column(db.Integer, primary_key =True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	password = db.Column(db.String(50))
	authenticated = db.Column(db.Boolean, default = False)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False


	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return "<User %r>" %(self.id)