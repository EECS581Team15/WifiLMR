"""
Entry point for radioApp
"""
import subprocess
import atexit
from ui import ui_manager
from hal import HAL
from hal import backlight
from core import Core

if __name__ == "__main__":
    subprocess.run(["xset", "r", "off"]) # disable key rollover
    atexit.register(lambda: subprocess.run(["xset", "r", "on"])) # only here to not goof up your dev machine
    hal = HAL()
    core = Core()
    # Remove the backlight hardcoding once we've got proper UI support/state saving
    hal.backlight.set_level(100)
    manager = ui_manager.UIManager(hal, core.sound_rx_tx)
    manager.main_loop()
