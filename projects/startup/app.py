
```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dreamweaver.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Initialize database
with app.app_context():
    db.create_all()

# Define routes
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users))

@app.route('/users', methods=['POST'])
def create_user():
    new_user = User(name=request.json['name'], email=request.json['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

if __name__ == '__main__':
    app.run(debug=True)
```
