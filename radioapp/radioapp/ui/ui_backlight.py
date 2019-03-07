import tkinter as tk


class UIBackLight:
    """Creates UI BackLight Screen."""

    def __init__(self, window, slider_number, master, hal):
        """Creates a frame, and adds slider and labels for UI BackLight."""

        self.window_copy = window
        self.hal = hal
        window.title("BackLight Setting")
        self.my_frame = tk.Frame(window, bg="#3399ff")

        # Binds key presses to change slider value.
        window.bind("<Right>", self.right_key)
        window.bind("<Left>", self.left_key)

        # Adds label to the window.
        self.add_label()

        # Adds slider to the window.
        self.current_slider_number = slider_number
        self.add_slider()
        self.modify_slider()

        # Adds save and back button.
        self.add_saver(master)

    def pack_screen(self):
        """Puts the screen on the main window."""

        self.my_frame.pack()

    def destroy_screen(self):
        """Destroys the screen from the main window."""

        self.window_copy.unbind("<Right>")
        self.window_copy.unbind("<Left>")
        self.my_frame.destroy()

    def add_saver(self, master):
        """Adds save and back button."""

        self.bottom_label = tk.Label(self.my_frame, bg="#3399ff")
        self.bottom_label.grid(row=4)
        self.save_button = tk.Button(self.my_frame, text="Save and Go Back", fg="white", bg="#3399ff", width=19,
                                     font="Helvetica 9", command=lambda: self.save_and_switch(master))
        self.save_button.grid(row=5)

    def save_and_switch(self, master):
        """Saves the slider value, and switches screen."""

        master.current_slider_number = self.current_slider_number
        master.switch_screen(master.display_home)

    def modify_slider(self):
        """Sets the slider value."""

        self.slider.configure(state="active")
        self.slider.set(self.current_slider_number)
        self.slider.configure(state="disabled")

    def add_slider(self):
        """Adds slider to the window."""

        self.top_label = tk.Label(self.my_frame, bg="#3399ff")
        self.top_label.grid(row=2)

        self.slider = tk.Scale(self.my_frame, from_=0, to=100, fg="white", bg="#3399ff", state="disabled",
                               sliderlength=20, orient=tk.HORIZONTAL, command=lambda value: self.hal.backlight.set_level(int(value)))
        self.slider.grid(row=3)

    def add_label(self):
        """Adds label to the window."""

        self.text_label = tk.Label(self.my_frame, text="Adjust Brightness", fg="white", bg="#3399ff",
                                   font="Helvetica 10 bold")
        self.text_label.grid(row=1)

    def right_key(self, event):
        """Binds Up key to change the slider value."""

        self.slider.configure(state="active")
        self.slider.set(self.current_slider_number + 10)
        self.current_slider_number = self.current_slider_number + 10
        self.slider.configure(state="disabled")

    def left_key(self, event):
        """Binds Down key to change the slider value."""

        self.slider.configure(state="active")
        self.slider.set(self.current_slider_number - 10)
        self.current_slider_number = self.current_slider_number - 10
        self.slider.configure(state="disabled")
