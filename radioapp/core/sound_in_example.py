from mumble import MumbleAdapter
from sound import SoundManager

def started():
    print('Mumble: Started')

def connected():
    print('Mumble: Connected')

mumble = MumbleAdapter()
mumble.initialize('192.168.1.112', 'test_client')
mumble.start(started)
mumble.connect(connected)

sound = SoundManager(mumble)