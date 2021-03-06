import tkinter as tk
import tkinter.ttk as ttk
import time
from . import resources
from .images import *


class UIHome:
    """Creates UI Home Screen."""

    def __init__(self, window, master, hal, battery_number, battery_color):
        """Creates a frame, and customizes and adds labels for UI Home Screen."""

        self.window = window
        window.title("Home")
        self.hal = hal
        self.my_frame = tk.Frame(window)
        self.icons = resources.Resources()
        self.current_battery_number = battery_number
        self.battery_color = battery_color

        window.bind("<Left>", self.button_1_action)
        window.bind("<space>", self.button_2_action)
        window.bind("<Right>", self.button_3_action)
        self.master = master

        self.add_top()
        self.add_middle()
        self.add_buttons()
        self.set_battery()

    def pack_screen(self):
        """Puts the screen on the main window."""

        self.my_frame.pack(expand=1, fill="both")

    def destroy_screen(self):
        """Destroys the screen from the main window."""

        self.window.unbind("<Left>")
        self.window.unbind("<space>")
        self.window.unbind("<Right>")
        self.my_frame.destroy()

    def add_buttons(self):
        """Adds buttons at the bottom frame."""

        self.bottom_frame = tk.Frame(self.my_frame, bg="yellow")
        self.bottom_frame.pack(side="bottom", fill="x")

        self.button_1 = tk.Button(self.bottom_frame, text="1", bg="#3399ff", fg="white", height=1, width=3,
                                  command=self.button_1_action)
        self.icon_1 = tk.PhotoImage(data=setting)
        self.button_1.config(image=self.icon_1, width="46", height="25")
        self.button_1.grid(row=7, column=0, sticky="nsew")

        self.button_2 = tk.Button(
            self.bottom_frame, text="2", height=1, width=3, fg="white", bg="#3399ff")
        self.icon_2 = tk.PhotoImage(data=radio)
        self.button_2.config(image=self.icon_2, width="48", height="25")
        self.button_2.grid(row=7, column=1, sticky="nsew")

        self.button_3 = tk.Button(
            self.bottom_frame, text="3", height=1, width=4, fg="white", bg="#3399ff")
        self.icon_3 = tk.PhotoImage(data=message)
        self.button_3.config(image=self.icon_3, width="48", height="25")
        self.button_3.grid(row=7, column=2, sticky="nsew")

    def add_middle(self):
        """Customizes and adds labels at the middle frame."""

        self.middle_frame = tk.Frame(self.my_frame, bg="#3399ff")
        self.middle_frame.pack(expand=1, fill="both")

        self.label_4 = tk.Label(
            self.middle_frame, text="", fg="white", bg="#3399ff", font="Helvetica 9 bold")
        self.label_4.grid(row=2, column=0, sticky="nsew")

        self.label_5 = tk.Label(self.middle_frame, text=" Channel 0",
                                fg="white", bg="#3399ff", font="Helvetica 9 bold")
        self.label_5.grid(row=4, column=0, sticky="nsew")

        self.label_6 = tk.Label(self.middle_frame, text="          ",
                                fg="white", bg="#3399ff", font="Helvetica 9 bold")
        self.label_6.grid(row=4, column=1, sticky="nsew")

    def add_top(self):
        """Customizes and adds labels at the top frame."""

        self.top_frame = tk.Frame(self.my_frame, bg="#3399ff")
        self.top_frame.pack(side="top", fill="x")

        self.label_1 = tk.Label(self.top_frame, text="12:00:00", height=2, width=8, fg="white", bg="#3399ff",
                                font="Helvetica 9 bold")
        self.label_1.grid(row=0, column=0, sticky="nsew")

        self.label_2 = tk.Label(self.top_frame, text="",
                                height=2, width=6, fg="white", bg="#3399ff")
        self.label_2.grid(row=0, column=1, sticky="nsew")
        self.battery_style = ttk.Style()
        self.battery_style.theme_use("classic")
        self.battery_style.configure("Battery.Horizontal.TProgressbar", background=self.battery_color, foreground="red")
        self.label_3 = ttk.Progressbar(self.top_frame, length=15, value=0, style="Battery.Horizontal.TProgressbar",
                                       orient=tk.VERTICAL, mode="determinate")
        self.label_3.grid(row=0, column=2, sticky="nsew")
        
        self.wifi_icon = tk.Label(self.top_frame, height=31,
                                  width=24, image=self.icons.WIFI_NONE, bg="#3399ff")
        self.wifi_icon.place(x=136, y=0)

        self.update_clock()
        self.update_wifi()

    def update_clock(self):
        """Updates the clock time."""

        time_string = time.strftime('%H:%M:%S')
        self.label_1.configure(text=time_string)
        self.label_1.after(200, func=self.update_clock)

    def update_wifi(self):
        """
        Updates the wifi icon
        """
        info = self.hal.wifi.signal_poll()
        image = self.icons.WIFI_NONE
        if info is not None and "rssi" in info:
            quality = 2 * (info["rssi"] + 100)
            if quality >= 75:
                image = self.icons.WIFI_4
            elif quality >= 50:
                image = self.icons.WIFI_3
            elif quality >= 25:
                image = self.icons.WIFI_2
            else:
                image = self.icons.WIFI_1
        self.wifi_icon.config(image=image)
        self.wifi_icon.after(500, func=self.update_wifi)
    
    def set_battery(self):
        self.label_3["value"] = self.current_battery_number

    def modify_battery(self):
        self.label_3["value"] = self.label_3["value"] + 4
        self.current_battery_number = self.label_3["value"]
        if self.current_battery_number > 50:
            self.battery_style.configure("Battery.Horizontal.TProgressbar", background="green", foreground="green")
            self.battery_color = "green"
        if self.current_battery_number < 50 and self.current_battery_number >= 20:
            self.battery_style.configure("Battery.Horizontal.TProgressbar", background="orange", foreground="orange")
            self.battery_color = "orange"
        if self.current_battery_number < 20:
            self.battery_style.configure("Battery.Horizontal.TProgressbar", background="red", foreground="red")
            self.battery_color = "red"

    def button_1_action(self, *args):
        self.master.current_battery_number = self.current_battery_number
        self.master.current_battery_color = self.battery_color
        self.master.switch_screen(self.master.display_ui_back_light)

    def button_2_action(self, *args):
        self.modify_battery()

    def button_3_action(self, *args):
        print("Button 3")
