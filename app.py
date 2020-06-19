from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.states'


db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    insert_date = db.Column(db.DateTime, default=datetime.now)
    date = db.Column(db.DateTime, default=datetime.now)
    state = db.Column(db.String(50))
    fips = db.Column(db.Integer)
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)


