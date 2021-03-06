"""
Radioapp.core.mumble
====================

Adapter for the pymumble library

The pymumble library used can be found here:
https://github.com/azlux/pymumble
"""

from pymumble_py3 import Mumble
from pymumble_py3.constants import *

class MumbleAdapter():
    """Adaptation of pymumble api"""

    def __init__(self):
        self.mumble = None

    def connect(self, host, user, port=64738, password='', certfile=None, keyfile=None, reconnect=True, tokens=[], debug=False):
        """
        Creates/initializes the Mumble object
        """
        if not self.mumble:
            self.mumble = Mumble(host, user, port, password, certfile, keyfile, reconnect, tokens, debug)

    def start(self):
        """
        Start and configure the mumble client
        """
        if not self.mumble:
            return
        self.mumble.set_application_string("Radio?")
        self.mumble.start()
    
    def on_connect(self, callback):
        self.set_mumble_callback(PYMUMBLE_CLBK_CONNECTED, callback)

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

    def get_users(self):
        return self.mumble.users

    def get_channels(self):
        return self.mumble.channels

    def send_sound(self, sound):
        self.mumble.sound_output.add_sound(sound)

    def upload_size(self, size):
        self.mumble.sound_output.set_audio_per_packet(size)
