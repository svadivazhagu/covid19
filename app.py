from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases.db'


db = SQLAlchemy(app)

# class CountryCases(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.String(10))
#     cases = db.Column(db.Integer)
#     deaths = db.Column(db.Integer)


# #Route for inserting new data COUNTRY-wide into the DB
# @app.route('/<date>/<cases>/<deaths>')
# def index(date, cases, deaths):
#     countryCases = CountryCases(date = date, cases = cases, deaths = deaths)
#     db.session.add(countryCases)
#     db.session.commit()
#
#     return '<h1>Added new row</h1>'
#
#


