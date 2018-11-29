"""
Radioapp.core.mumble
====================

Adapter for the pymumble library
"""

from .pymumble.mumble import Mumble

class MumbleAdapter():
    """Addaptation of pymumble api"""

    def __init__(self):
        self.mumble = None

    def initialize(self, host, user, port=64738, password='', certfile=None, keyfile=None, reconnect=False, tokens=[], debug=False):
        """
        Creates/initializes the Mumble object
        """
        if not self.mumble:
            self.mumble = Mumble(host, user, port, password, certfile, keyfile, reconnect, tokens, debug)