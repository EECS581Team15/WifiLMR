"""
radiomanager.api.endpoints.handshaking
======================================

Endpoints for pinging the backend, provisioning, and registering/deregistering
"""

from werkzeug.exceptions import BadRequest
from flask import request
import flask_restful

class Ping(flask_restful.Resource):
    """
    An example endpoint, useful for testing purposes.
    """

    def get(self):
        return "ping"

    def post(self):
        data = request.form["data"]
        if data == "ping":
            return "pong"
        elif data == "pong":
            return "ping"
        else:
            raise BadRequest("Expected \"data=ping\" or \"data=pong\"")
