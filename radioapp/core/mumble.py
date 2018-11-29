"""
Radioapp.core.mumble
====================

Adapter for the pymumble library
"""

from .pymumble.mumble import Mumble

class MumbleAdapter():

    initialize(host, user, port=64738, password='', certfile=None, keyfile=None, reconnect=False, tokens=[], debug=False):
        self.mumble = Mumble(host, user, port, password, certfile, keyfile, reconnect, tokens, debug)