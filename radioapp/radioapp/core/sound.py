import pymumble_py3 as mumble
import alsaaudio
import logging
import select
import threading
import time

class SoundManager():
    SR = 48000
    PERIOD_MS = 0.01
    PERIOD_SIZE = int(SR * PERIOD_MS)

    class AudioOutput:
        def __init__(self):
            self.pcm = alsaaudio.PCM(type=alsaaudio.PCM_PLAYBACK,
                                     mode=alsaaudio.PCM_NONBLOCK)
            self.pcm.setrate(SoundManager.SR)
            self.pcm.setchannels(1)
            self.pcm.setperiodsize(SoundManager.PERIOD_SIZE)
    def __init__(self, mumble_):
        """ 
            Constructor for the Sound Manager
            mumble: an instance of MumbleAdapter
        """
        self.mumble = mumble_
        self.log = logging.getLogger(self.__class__.__name__)
        self._on_status_change = None
        self.mumble.callbacks.set_callback(
            mumble.constants.PYMUMBLE_CLBK_SOUNDRECEIVED, self.sound_received)
        self.mumble.callbacks.set_callback(
            mumble.constants.PYMUMBLE_CLBK_USERCREATED, self.user_added)
        self.mumble.callbacks.set_callback(
            mumble.constants.PYMUMBLE_CLBK_USERREMOVED, self.user_removed)
        self.mumble.set_receive_sound(True)
        self.pcm_in = alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE)
        self.pcm_in.setrate(self.SR)
        self.pcm_in.setchannels(1)
        self.pcm_in.setperiodsize(self.PERIOD_SIZE)
        self.pcm_in.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        self.should_record = threading.Event()
        self.audio_outputs = {}
        self.send_thread = threading.Thread(target=self.recording_process, daemon=True)
        self.send_thread.start()

    def sound_received(self, user, raw_sound):
        """ 
        Callback used when sound is received. 
        user_queue is the queue of the user speaking.
        raw_sound is the sound object being placed in queue.
        """
        if user["session"] in self.audio_outputs:
            output = self.audio_outputs[user["session"]]
            sound = user.sound.get_sound()
            output.pcm.write(sound.pcm)
        else:
            self.log.error("User %s not in audio_outputs!", user)

    def user_added(self, user):
        output = self.AudioOutput()
        self.audio_outputs[user["session"]] = output

    def user_removed(self, user, msg):
        del self.audio_outputs[user["session"]]

    def set_recording(self, should_record):
        """ 
        Sets variable responsible for controlling microphone input
        """
        if should_record:
            self.should_record.set()
        else:
            self.should_record.clear()

    def recording_process(self):
        while True:
            self.should_record.wait()
            print("Unmuting...")
            self.mumble.sound_output.clear_buffer()
            while self.should_record.is_set():
                _, data = self.pcm_in.read()
                # The overshoot non-sense gets around an issue in pymumble that
                # causes previous recordings to "stack up"
                if self.mumble.sound_output.get_buffer_size() < 0.2:
                    self.mumble.sound_output.add_sound(data)
    def on_status_change(self, callback):
        self._on_status_change = callback


if __name__ == "__main__":
    mum = mumble.Mumble("localhost", "foouser")
    mum.setDaemon(True)
    sm = SoundManager(mum)
    mum.start()
    while True:
        input("Press enter to unmute")
        sm.set_recording(True)
        input("Press enter to mute")
        sm.set_recording(False)
