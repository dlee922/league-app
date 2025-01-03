from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
  app = Flask(__name__)
  CORS(app)

  # load configurations
  app.config.from_object('app.config.Config')

  # Initialize extensions
  db.init_app(app)

  with app.app_context():
    db.create_all() # create tables

  jwt.init_app(app)

  # Register routes
  from .routes import api
  app.register_blueprint(api)


  return app