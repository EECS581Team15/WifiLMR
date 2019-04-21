"""
radioapp.core
=============

The Core module encapsulates the business logic of RadioApp.
"""

import pymumble_py3
import uuid
from . import sound

class Core:
    def __init__(self):
        self.mumble = pymumble_py3.Mumble("mumble.zjcers.com", str(uuid.uuid4()), reconnect=True)
        self.mumble.setDaemon(True)
        self.mumble.start()
        self.sound_rx_tx = sound.SoundManager(self.mumble)
