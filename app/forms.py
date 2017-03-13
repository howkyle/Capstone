from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
	studentID = StringField("ID Number", validators = [InputRequired()])
	password = PasswordField("Password", validators= [InputRequired()])


class SignUpForm(FlaskForm):
	fname= StringField("First Name", validators= [InputRequired()])
	lname= StringField("Last Name", validators= [InputRequired()])
	studentID = StringField("ID Number", validators = [InputRequired()])
	password = PasswordField("Password", validators= [InputRequired()])
	confPassword = PasswordField("Confirm Password", validators= [InputRequired(),EqualTo("password")])





