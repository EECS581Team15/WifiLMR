import tkinter as tk
import tkinter.ttk as ttk
import time
import pymumble_py3 as mumble
from . import resources
from .images import *


class UIHome:
    """Creates UI Home Screen."""

    def __init__(self, window, master, hal):
        """Creates a frame, and customizes and adds labels for UI Home Screen."""

        self.window = window
        window.title("Home")
        self.hal = hal
        self.my_frame = tk.Frame(window)
        self.icons = resources.Resources()

        window.bind("<Left>", self.button_1_action)
        window.bind("<KeyPress>", self.generic_keypress)
        window.bind("<KeyRelease>", self.generic_keyrelease)
        window.bind("<Right>", self.button_3_action)
        self.master = master

        self.add_top()
        self.add_middle()
        self.add_buttons()

    def pack_screen(self):
        """Puts the screen on the main window."""

        self.my_frame.pack(expand=1, fill="both")

    def destroy_screen(self):
        """Destroys the screen from the main window."""

        self.window.unbind("<Left>")
        self.window.unbind("<KeyPress>")
        self.window.unbind("<KeyRelease>")
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

        self.connected = tk.Label(self.middle_frame, text="disconnected",
                                  fg="white", bg="#3399ff", font="Helvetica 9 bold")
        self.connected.grid(row=4, column=1, sticky="nsew")
        self.update_connected()

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
        self.battery_style.configure(
            "Battery.Horizontal.TProgressbar", background="#3399ff", foreground="red", length=8)
        self.battery_label = ttk.Progressbar(self.top_frame, length=4, value=0, style="Battery.Horizontal.TProgressbar",
                                             orient=tk.VERTICAL, mode="determinate")
        self.battery_label.grid(row=0, column=2, sticky="nsew")

        self.wifi_icon = tk.Label(self.top_frame, height=31,
                                  width=24, image=self.icons.WIFI_NONE, bg="#3399ff")
        self.wifi_icon.place(x=136, y=0)

        self.update_clock()
        self.update_wifi()
        self.update_battery()

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

    def update_battery(self):
        percent = self.hal.battery.poll() * 100
        self.battery_label["value"] = percent
        if percent > 50:
            self.battery_style.configure(
                "Battery.Horizontal.TProgressbar", background="green", foreground="green")
        elif percent > 20:
            self.battery_style.configure(
                "Battery.Horizontal.TProgressbar", background="orange", foreground="orange")
        else:
            self.battery_style.configure(
                "Battery.Horizontal.TProgressbar", background="red", foreground="red")
        self.battery_label.after(2000, func=self.update_battery)

    def update_connected(self):
        state = self.master.sound.mumble.connected
        state = {
            mumble.constants.PYMUMBLE_CONN_STATE_NOT_CONNECTED: "Offline",
            mumble.constants.PYMUMBLE_CONN_STATE_AUTHENTICATING: "Offline",
            mumble.constants.PYMUMBLE_CONN_STATE_FAILED: "Offline",
            mumble.constants.PYMUMBLE_CONN_STATE_CONNECTED: "Online"
        }.get(state, "Unknown")
        self.connected.configure(text="Status: "+state)
        self.connected.after(500, self.update_connected)

    def button_1_action(self, *args):
        self.master.switch_screen(self.master.display_ui_back_light)

    def button_2_action(self, *args):
        print("Button 2")

    def button_3_action(self, *args):
        print("Button 3")

    def generic_keypress(self, ev):
        if ev.keysym == "space":
            self.master.ptt_pressed()

    def generic_keyrelease(self, ev):
        if ev.keysym == "space":
            self.master.ptt_release()
