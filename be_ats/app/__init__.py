from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'apdfbap9IBIUtvivTviutIjbKhg77tHGjhGIbuyt7t7'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    from app.urls import __URLPATH__

    __URLPATH__()
    api.init_app(app)
    from app.models.data import Incomes, Outcomes
    Migrate(app, db)
    return app
