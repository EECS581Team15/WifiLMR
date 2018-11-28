"""
radiomanager.api
================

Provides a REST API for the radio clients to connect to.
"""

from .endpoints.handshaking import Ping, Provision


def setup_routing(api):
    api.add_resource(Ping, "/api/ping")
    api.add_resource(Provision, "/api/provision")
