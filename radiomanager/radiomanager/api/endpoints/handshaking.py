"""
radiomanager.api.endpoints.handshaking
======================================

Endpoints for pinging the backend, provisioning, and registering/deregistering
"""

import uuid
import re
from werkzeug.exceptions import BadRequest
from flask import request
from flask_restful import reqparse, Resource
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import UnsupportedAlgorithm
from ... import FlaskExtensions
from ...models.device import Device


class Ping(Resource):
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


class Provision(Resource):
    """
    Clients use this to get setup on the system
    """
    POST_PARSER = reqparse.RequestParser()
    POST_PARSER.add_argument("name", type=str)
    POST_PARSER.add_argument("public_key", type=str)
    ALPHANUMERIC_WITH_SPACES = re.compile("([a-z]|[A-Z]|[0-9]| )*")

    def post(self):
        """
        POSTing to this endpoint provisions a new client with no authentication
        capabilities. The client is expected to pass a UUID.
        """
        args = self.POST_PARSER.parse_args()
        raw_key = args["public_key"].encode("utf-8")
        raw_name = args["name"]
        self._check_key(raw_key)
        self._check_name(raw_name)
        device = Device(public_key=raw_key, name=args["name"].encode("utf-8"))
        FlaskExtensions.db.session.add(device)
        FlaskExtensions.db.session.commit()
        return {"result": "success"}

    @staticmethod
    def _check_key(raw_key):
        try:
            load_pem_public_key(raw_key, default_backend())
        except (ValueError, UnsupportedAlgorithm):
            raise BadRequest("Invalid public key")

    @classmethod
    def _check_name(cls, raw_name):
        if cls.ALPHANUMERIC_WITH_SPACES.fullmatch(raw_name) is None:
            raise BadRequest("Invalid radio name")
