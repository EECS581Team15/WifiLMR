from .mumble import MumbleAdapter
from pymumble_py3.constants import *
from collections import deque
from threading import Thread

class SoundManager():

    def __init__(self, mumble):
        """ 
            Constructor for the Sound Manager
            mumble: an instance of MumbleAdapter
        """
        self.mumble = mumble
        self.CHUNK = 1920
        self.STEREO_MIC = True

        self.sound_in_queue = deque()
        self.mumble.set_mumble_callback(PYMUMBLE_CLBK_SOUNDRECEIVED, self.sound_received)

        self.sound_play_proc = Thread(target=self.play_raw_audio_proc)
        self.should_play_sound = False

        self.record_proc = Thread(target=self.start_recording)
        self.should_record = False

        self.sound_play_proc.start()
        self.record_proc.start()

    def set_playing(self, should_play_sound):
        """ 
            Set variable responsible for speaker output control
        """
        self.should_play_sound = should_play_sound

    def sound_received(self, user_queue, raw_sound):
        """ 
        Callback used when sound is received. 
        user_queue is the queue of the user speaking.
        raw_sound is the sound object being placed in queue.
        """
        self.play_raw_audio(raw_sound.pcm)

    def play_raw_audio(self, sound):
        """ 
        Places raw pcm audio into the sound queue for the raw_audio
            process to play.
        """
        self.sound_in_queue.append(sound)

    def play_raw_audio_proc(self):
        """ 
        Target for a thread that consumes raw audio and
            feeds it to PyAudio
        """
        import pyaudio
        
        pa = pyaudio.PyAudio()
        stream = pa.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=48000,
                                    output=True,
                                    input=False,
                                    frames_per_buffer=self.CHUNK)

        while len(self.sound_in_queue) > 0:
            if self.should_play_sound:
                stream.write(self.sound_in_queue.popleft())

    
    def set_recording(self, should_record):
        """ 
        Sets variable responsible for controlling microphone input
        """
        self.should_record = should_record

    def start_recording(self):
        """ 
        Process for recording audio and sending it to mumble server
        """
        import pyaudio

        self.mumble.upload_size(0.02)

        def recording_received(in_data, frame_count, time_info, status):
            if self.should_record:
                self.mumble.send_sound(in_data)
                #print(len(in_data))
            return (None, pyaudio.paContinue)

        pa = pyaudio.PyAudio()
        xChunk = 2 if self.STEREO_MIC else 1
        chunk = self.CHUNK // xChunk
        stream = pa.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=48000,
                                    output=False,
                                    input=True,
                                    stream_callback=recording_received,
                                    frames_per_buffer=chunk)

        stream.start_stream()



    
