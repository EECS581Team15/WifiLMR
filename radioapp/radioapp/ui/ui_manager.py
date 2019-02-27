from .home import UIHome
from .ui_backlight import UIBackLight
import tkinter as tk


class UIManager:
    """Manages UI Screens and Settings."""

    def __init__(self):
        """Creates a window, and manages different screens and settings."""

        self.current_slider_number = 0
        self.current_screen = None

        self.initialize_window()

        self.switch_screen(self.display_home)

    def display_home(self):
        """Displays the Home screen."""

        self.current_screen = UIHome(self.window, self)
        self.current_screen.pack_screen()

    def display_ui_back_light(self):
        """Displays the UI BackLight screen."""

        self.current_screen = UIBackLight(self.window, self.current_slider_number, self)
        self.current_screen.pack_screen()

    def initialize_window(self):
        """Initializes the main window."""

        self.window = tk.Tk()
        self.window.geometry("160x128")
        self.window.configure(background="#3399ff")
        self.window.resizable(0, 0)
        self.window.pack_propagate(0)

    def switch_screen(self, screen_class):
        """Switches between Screen."""

        if self.current_screen is not None:
            self.current_screen.destroy_screen()

        screen_class()

    def main_loop(self):
        """Loops the main window."""

        self.window.mainloop()
