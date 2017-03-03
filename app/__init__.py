from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 

#Config Values

USERNAME = ""
PASSWORD = ""
DATABASE_URI=""


SECRET_KEY="I hope no one finds out this key, it woild be dreadful"

app = Flask(__name__)
app.config['SECRET_KEY']=SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config.from_object(__name__)
from app import views

