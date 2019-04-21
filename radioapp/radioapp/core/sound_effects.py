import wave
import os
import threading
import alsaaudio

class SoundEffects():
    PERIOD_SIZE = 1024
    FX_DIR = os.path.join(os.path.dirname(__file__), "..", "sounds")
    def __init__(self):
        """ 
        Class used to play a wav file
        play_wave_file(file): plays a file
        stop(): stops currently playing file early
        """
        self.file_changed = threading.Event()
        self.wave_file = None
        self.play_thread = threading.Thread(target=self.play_process, daemon=True)
        self.play_thread.start()

    def play_wave_file(self, file_to_play):
        """ Plays a wave file """
        self.wave_file = wave.open(file_to_play, 'rb')
        self.file_changed.set()

    def stop(self):
        """ Stops the current playing audio """
        self.wave_file = None
        self.file_changed.set()

    def play_process(self):
        pcm = alsaaudio.PCM()
        pcm.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        pcm.setrate(48000)
        pcm.setchannels(1)
        pcm.setperiodsize(self.PERIOD_SIZE)
        while True:
            self.file_changed.wait()
            if self.wave_file is not None:
                while True:
                    sound_data = self.wave_file.readframes(self.PERIOD_SIZE // 2) # 2 bytes per sample
                    if len(sound_data) == 0:
                        self.wave_file = None
                        break
                    else:
                        pcm.write(sound_data)
            self.file_changed.clear()

    def beep(self):
        self.play_wave_file(os.path.join(self.FX_DIR, "beep.wav"))
    
    def error(self):
        self.play_wave_file(os.path.join(self.FX_DIR, "error.wav"))
