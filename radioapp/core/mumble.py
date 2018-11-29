"""
Radioapp.core.mumble
====================

Adapter for the pymumble library
"""

from .pymumble.mumble import Mumble
from .pymumble.constants import *

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

    def start(self, callback):
        """
        Start and configure the mumble client
        """
        if not self.mumble:
            return
        self.mumble.set_application_string("Radio?")
        self.mumble.start()
        while not self.mumble.is_ready():
            continue
        self.mumble.set_bandwidth(8)
        self.mumble.set_loop_rate(0.05)
        self.mumble.set_receive_sound(True)
        callback()

    def set_mumble_callback(self, callbackConstant, callback):
        """
        PYMUMBLE_CLBK_CONNECTED: connection succeeded
        PYMUMBLE_CLBK_CHANNELCREATED: send the created channel object as parameter
        PYMUMBLE_CLBK_CHANNELUPDATED: send the updated channel object and a dict with all the modified fields as parameter
        PYMUMBLE_CLBK_CHANNELREMOVED: send the removed channel object as parameter
        PYMUMBLE_CLBK_USERCREATED: send the added user object as parameter
        PYMUMBLE_CLBK_USERUPDATED: send the updated user object and a dict with all the modified fields as parameter
        PYMUMBLE_CLBK_USERREMOVED: send the removed user object and the mumble message as parameter
        PYMUMBLE_CLBK_SOUNDRECEIVED: send the user object that received the sound and the SoundChunk object itself
        PYMUMBLE_CLBK_TEXTMESSAGERECEIVED: send the received message
        """

        if not self.mumble:
            return
        self.mumble.callbacks.set_callback(callbackConstant, callback)
