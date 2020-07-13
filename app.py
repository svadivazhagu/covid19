from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cases.db'


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name
    def serialize(self):
        return {"id": self.id,
                "name" : self.name}

@app.route('/user/', methods=['GET'])
def index():
    return jsonify({'users': list(map(lambda user: user.serialize(), User.query.all()))})

@app.route('/user/<int:id>/')
def get_user(id):
    return jsonify({'user': User.query.get(id).serialize()})

@app.route('/user/', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = User(request.json['name'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'user': user.serialize()}), 201

@app.route('/user/<int:id>/', methods=['DELETE'])
def del_user(id):
    db.session.delete(User.query.get(id))
    db.session.commit()
    return jsonify({'result': True})

@app.route('/user/<int:id>/', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    user.name = request.json.get('name', user.name)
    db.session.commit()
    return jsonify({'user': user.serialize()})
