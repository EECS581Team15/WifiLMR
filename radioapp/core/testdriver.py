from mumble import MumbleAdapter
from multiprocessing import Queue, Process
import time
import alsaaudio
from pymumble_py3.mumble import *
from pymumble_py3.users import *
from pymumble_py3.soundqueue import *
from pymumble_py3.constants import *


class TestDriver():

    def __init__(self):
        self.pa = None
        self.stream = None
        self.queue = Queue()

        proc = Process(target=self.collect_audio)
        proc.start()

        self.mumble = MumbleAdapter()
        self.mumble.initialize('192.168.1.112', 'test_client')
        self.mumble.mumble.set_receive_sound(True)
        self.mumble.set_mumble_callback(PYMUMBLE_CLBK_CONNECTED, self.has_connected)
        self.mumble.set_mumble_callback(PYMUMBLE_CLBK_SOUNDRECEIVED, self.sound_recieved)
        self.mumble.start(self.has_started)

    def has_started(self):
        print("STARTED")

    def sound_recieved(self, user, sound):
        #print("SOUND RECIEVED")
        #print(sound)
        self.play_audio(sound)

    def has_connected(self):
        print("CONNECTED")

    # def get_audio(self, in_data, frame_count, time_info, status):
    #     data = self.queue.get()
    #     print("ASDF")
    #     return (in_data, pyaudio.paContinue)
        
    def play_audio(self, sound):
        # pass

        """ PyAudio Solution """
        self.queue.put(sound.pcm)
        #print("ASdf")
        #self.stream.write(self.queue.get()[:1024])

        """ PyAlsaAudio Solution """
        # if self.pa is None:
        #     self.pa = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device='default')
        #     self.pa.setchannels(1)
        #     self.pa.setrate(48000)
        #     self.pa.setformat(alsaaudio.PCM_FORMAT_U16_LE)
        #     proc = Process(target=self.collect_audio)
        #     proc.start()
        # self.queue.put(sound.pcm)


    def collect_audio(self):
        import pyaudio
        
        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=48000,
                                    output=True)
            #self.stream.start_stream()
        while True:
            sound = self.queue.get()
            if sound is None:
                time.sleep(.5)
            else:
                #self.pa.write(sound)
                stream.write(sound[:1024])
                
        
                
                
            
            

