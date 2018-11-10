"""
radiomanager.api
================

Provides a REST API for the radio clients to connect to.
"""

from .endpoints.handshaking import Ping

def setup_routing(api):
    api.add_resource(Ping, "/ping")