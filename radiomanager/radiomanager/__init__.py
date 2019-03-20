"""
radiomanager
============

WifiLMR's backend server. Handles authentication, fleet management, and call
routing.
"""

from flask import Flask, render_template, request
from . import mdns
from . import FlaskExtensions
from .models.device import Device
import sys

class PRODUCTION_CONFIG:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://db"


class TESTING_CONFIG:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


def create_app(config_obj=TESTING_CONFIG):
    from .api import setup_routing
    app = Flask(__name__)
    app.config.from_object(config_obj)
    setup_routing(FlaskExtensions.api)
    with app.app_context():
        FlaskExtensions.api.init_app(app)
        FlaskExtensions.db.init_app(app)
        FlaskExtensions.db.create_all()
    @app.route('/', methods=['GET','POST'])
    def homepage():
        """print(Device.query.first().name, file=sys.stderr)"""
        keyRevoked = request.form.post("form2","")
        return render_template('console.html', deviceList=Device.query.all())
    return app


def init_app(is_testing=False):
    config_obj = TESTING_CONFIG if is_testing else PRODUCTION_CONFIG
    mdns.register_service()
    return create_app(config_obj)
