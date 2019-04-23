"""
Entry point for radioApp
"""
import subprocess
import atexit
import fcntl
from ui import ui_manager
from hal import HAL
from hal import backlight
from core import Core

def force_random_entropy():
    RNDADDTOENTCNT = 0x40045201 # Divined by S C I E N C E
    rand = open("/dev/urandom", 'w')
    fcntl.ioctl(rand.fileno(), RNDADDTOENTCNT, (1024).to_bytes(4, "little", signed=False))

if __name__ == "__main__":
    force_random_entropy()
    subprocess.run(["xset", "r", "off"]) # disable key rollover
    atexit.register(lambda: subprocess.run(["xset", "r", "on"])) # only here to not goof up your dev machine
    hal = HAL()
    core = Core()
    # Remove the backlight hardcoding once we've got proper UI support/state saving
    backlight = int(core.state.state.get("backlight", 100))
    hal.backlight.set_level(backlight)
    manager = ui_manager.UIManager(hal, core)
    manager.main_loop()
