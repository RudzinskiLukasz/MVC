from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7102FXVCTN7d!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes, models
