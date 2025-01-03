from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

api = Blueprint('api', __name__)

@api.route('/')
def home(): 
    return jsonify({"message": "Welcome to the API!"})

@api.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Invalid input"}), 400

    hashed_password = generate_password_hash(data['password'], method='scrypt', salt_length=16)
    user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        access_token = create_access_token(identity={"username": user.username})
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401
