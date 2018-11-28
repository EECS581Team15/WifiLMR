"""
radiomanager
============

WifiLMR's backend server. Handles authentication, fleet management, and call
routing.
"""

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


class FlaskExtensions:
    """
    """
    db = SQLAlchemy()
    api = Api()

    @classmethod
    def reset(cls):
        # cls.db = SQLAlchemy()
        cls.api = Api()


class PRODUCTION_CONFIG:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://db"


class TESTING_CONFIG:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


def create_app(config_obj=PRODUCTION_CONFIG):
    from .api import setup_routing
    app = Flask(__name__)
    app.config.from_object(config_obj)
    setup_routing(FlaskExtensions.api)
    with app.app_context():
        FlaskExtensions.api.init_app(app)
        FlaskExtensions.db.init_app(app)
    return app


def init_app(is_testing=False):
    config_obj = TESTING_CONFIG if is_testing else PRODUCTION_CONFIG
    return create_app(config_obj)
