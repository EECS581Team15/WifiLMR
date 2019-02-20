"""
Entry point for radioApp
"""
from ui import ui_manager
if __name__ == "__main__":
    manager = ui_manager.UIManager()
    manager.main_loop()
