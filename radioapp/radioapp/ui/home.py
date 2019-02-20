import tkinter as tk
import time


class UIHome:
    """Creates UI Home Screen."""

    def __init__(self, window, master):
        """Creates a frame, and customizes and adds labels for UI Home Screen."""

        window.title("Home")
        self.my_frame = tk.Frame(window)

        self.add_top()
        self.add_middle()
        self.add_buttons(master)

    def pack_screen(self):
        """Puts the screen on the main window."""

        self.my_frame.pack(expand=1, fill="both")

    def destroy_screen(self):
        """Destroys the screen from the main window."""

        self.my_frame.destroy()

    def add_buttons(self, master):
        """Adds buttons at the bottom frame."""

        self.bottom_frame = tk.Frame(self.my_frame, bg="yellow")
        self.bottom_frame.pack(side="bottom", fill="x")

        self.button_1 = tk.Button(
            self.bottom_frame, text="1", bg="#3399ff", fg="white", height=1, width=3)
        self.button_1.grid(row=7, column=0, sticky="nsew")

        self.button_2 = tk.Button(
            self.bottom_frame, text="2", height=1, width=3, fg="white", bg="#3399ff")
        self.button_2.grid(row=7, column=1, sticky="nsew")

        self.button_3 = tk.Button(
            self.bottom_frame, text="3", height=1, width=4, fg="white", bg="#3399ff")
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

        self.label_7 = tk.Label(self.middle_frame, text="-120 dBm",
                                fg="white", bg="#3399ff", font="Helvetica 9 bold")
        self.label_7.grid(row=4, column=2, sticky="nsew")

    def add_top(self):
        """Customizes and adds labels at the top frame."""

        self.top_frame = tk.Frame(self.my_frame, bg="yellow")
        self.top_frame.pack(side="top", fill="x")

        self.label_1 = tk.Label(self.top_frame, text="12:00:00", height=1, width=8, fg="white", bg="#3399ff",
                                font="Helvetica 9 bold")
        self.label_1.grid(row=0, column=0, sticky="nsew")

        self.label_2 = tk.Label(self.top_frame, text="",
                                height=1, width=6, fg="white", bg="#3399ff")
        self.label_2.grid(row=0, column=1, sticky="nsew")

        self.label_3 = tk.Label(self.top_frame, text="100%", height=1, width=7, fg="white", bg="#3399ff",
                                font="Helvetica 9 bold")
        self.label_3.grid(row=0, column=2, sticky="nsew")

        self.update_clock()

    def update_clock(self):
        """Updates the clock time."""

        time_string = time.strftime('%H:%M:%S')
        self.label_1.configure(text=time_string)
        self.label_1.after(200, func=self.update_clock)
