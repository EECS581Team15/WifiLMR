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
import dbus

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
    @app.route('/', methods=['GET','POST'])
    def homepage():

        MUMBLE_SERVICE = "net.sourceforge.mumble.murmur"
        bus = dbus.SystemBus()
        server = bus.get_object(MUMBLE_SERVICE, "/1")
        murmur = dbus.Interface(server, 'net.sourceforge.mumble.Murmur')
        devices = murmur.getPlayers(dbus_interface='net.sourceforge.mumble.Murmur')
        print(devices, file=sys.stderr)
        outputList = []
        for d in devices:
            device = {
                'name': d[8],
                'radioID': d[7],
                'channel': d[6],
                'onlineseconds': d[9]
            }
            outputList.append(device)

        return render_template('console.html', deviceList=outputList)
    return app


def init_app(is_testing=False):
    config_obj = TESTING_CONFIG if is_testing else PRODUCTION_CONFIG
    mdns.register_service()
    return create_app(config_obj)
