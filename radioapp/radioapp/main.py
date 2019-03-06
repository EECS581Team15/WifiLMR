"""
Entry point for radioApp
"""
from ui import ui_manager
from hal import HAL
from hal import backlight

if __name__ == "__main__":
    hal = HAL()
    manager = ui_manager.UIManager(hal)
    # Remove the backlight hardcoding once we've got proper UI support/state saving
    bklight = backlight.Backlight()
    bklight.set_level(100)
    manager = ui_manager.UIManager()
    manager.main_loop()
