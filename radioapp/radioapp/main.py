"""
Entry point for radioApp
"""
from ui import ui_manager
from hal import HAL

if __name__ == "__main__":
    hal = HAL()
    manager = ui_manager.UIManager(hal)
    manager.main_loop()
