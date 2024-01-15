# app/__init__.py
from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("app/credentials.json")
firebase = initialize_app(cred)

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = "12345"

    from .routes import bp_receive_sensor_data, bp_get_sensor_data

    app.register_blueprint(bp_receive_sensor_data)
    app.register_blueprint(bp_get_sensor_data)

    return app
