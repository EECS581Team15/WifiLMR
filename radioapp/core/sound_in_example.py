from mumble import MumbleAdapter
from sound import SoundManager

def connected():
    print('Mumble: Connected')

mumble = MumbleAdapter()
mumble.connect('192.168.1.112', 'test_client')
mumble.start()
mumble.on_connect(connected)

sound = SoundManager(mumble)