import pymongo
from flask import Flask, current_app as capp
from config import AppConfig
from flask_cors import CORS

# Inorder to connect to mongodb first get mongodb client
def get_db_client():
    return pymongo.MongoClient(capp.config['DB_HOST'], capp.config['DB_PORT'])

# Now from the client get the db. db_client[mydb] will create 'mydb' if mydb doesn't exist.
def get_db_instance():
    db_client = get_db_client()
    return db_client[capp.config['DB_NAME']]

# Main app creation logic here.
def create_app(app_config=AppConfig):
    app = Flask(__name__)
    app.config.from_object(app_config)
    cors = CORS(app, resources={ r"/api/*": { "origins": "*" }})

    from src.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

from src import models
