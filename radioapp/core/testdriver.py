from mumble import MumbleAdapter
import time
from pymumble_py3.mumble import *
from pymumble_py3.users import *
from pymumble_py3.soundqueue import *
from pymumble_py3.constants import *


class TestDriver():

    def __init__(self):
        self.mumble = MumbleAdapter()
        self.mumble.initialize('192.168.1.111', 'test_client')
        self.mumble.mumble.set_receive_sound(True)
        self.mumble.set_mumble_callback(PYMUMBLE_CLBK_CONNECTED, self.has_connected)
        self.mumble.set_mumble_callback(PYMUMBLE_CLBK_SOUNDRECEIVED, self.sound_recieved)
        self.mumble.start(self.has_started)

    def has_started(self):
        print("STARTED")

    def sound_recieved(self, user, sound):
        print("SOUND RECIEVED")
        print(sound)

    def has_connected(self):
        print("CONNECTED")
        self.collect_audio()

    def collect_audio(self):
        pass
        #self.mumble.mumble.users.myself.recording()
        # while self.mumble.mumble.is_alive():
        #     for user in self.mumble.mumble.users.values():
        #         user.sound.lock.acquire()
        #         user.sound.set_receive_sound(True)
        #         print(user)
        #         print(user.sound.is_sound())
        #         user.sound.lock.release()
        #     time.sleep(4)
                
        
                
                
            
            

