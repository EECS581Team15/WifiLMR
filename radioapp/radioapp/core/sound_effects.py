import pyaudio
import wave

class SoundEffects():

    def __init__(self):
        """ 
        Class used to play a wav file
        play_wave_file(file): plays a file
        stop(): stops currently playing file early
        """
        self.CHUNK = 1024
        self.should_play = True
        self.audio = pyaudio.PyAudio()

    def play_wave_file(self, file_to_play):
        """ Plays a wave file """
        wave_file = wave.open(file_to_play, 'rb')
        stream = self.audio.open(format=self.audio.get_format_from_width(wave_file.getsampwidth()),
                                    channels=wave_file.getnchannels(),
                                    rate=wave_file.getframerate(),
                                    output=True)
        
        sound_data = wave_file.readframes(self.CHUNK)

        while len(sound_data) > 0 and self.should_play:
            stream.write(sound_data)
            sound_data = wave_file.readframes(self.CHUNK)

        stream.stop_stream()
        stream.close()

    def stop(self):
        """ Stops the current playing audio """
        self.should_play = False



