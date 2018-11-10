"""
radiomanager.api
================

Provides a REST API for the radio clients to connect to.
"""

import flask
import flask_restful
from .endpoints.handshaking import Ping

class Application:
    def __init__(self):
        self._app = flask.Flask(__name__)
        self._api = flask_restful.Api(self._app)
        self._api.add_resource(Ping, "/ping")
    def run(self):
        self._app.run("0.0.0.0", 8000, debug=True)