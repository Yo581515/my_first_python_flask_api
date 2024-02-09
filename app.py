import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')

db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    drinks_list = [drink.to_dict() for drink in drinks]
    return drinks_list


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    print(type(drink))
    print()
    print(drink)
    print()
    return drink.to_dict()


@app.route('/drinks', methods=['POST'])
def add_drink():
    print('post here')
    drink = Drink(name=request.json['n'],
                  description=request.json['d'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "yeet!@"}
