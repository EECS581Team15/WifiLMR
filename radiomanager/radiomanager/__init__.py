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

        MUMBLE_SERVICE = "net.sourceforge.mumble.murmur"
        bus = dbus.SystemBus()
        server = bus.get_object(MUMBLE_SERVICE, "/1")
        # playerList = server.getPlayers()
        murmur = dbus.Interface(server, 'net.sourceforge.mumble.Murmur')
        intro = murmur.getPlayers(dbus_interface='net.sourceforge.mumble.Murmur')
        # devices = Device.query.all()
        print(intro, file=sys.stderr)

        outputList = []

        # for device in devices:
        #     added = False
        #     for player in playerList:
        #         if device.uuid == player.name:
        #             outputList.append((device, player))
        #             added = True
        #             break
        #     if not added:
        #         outputList.append((device, None))

        return render_template('console.html', deviceList=outputList)
    return app


def init_app(is_testing=False):
    config_obj = TESTING_CONFIG if is_testing else PRODUCTION_CONFIG
    mdns.register_service()
    return create_app(config_obj)
