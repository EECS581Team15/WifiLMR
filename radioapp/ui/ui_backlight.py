from tkinter import *


class UIBackLight():
	"""Creates UI Backlight Screen."""

	def __init__(self):
		"""Creates a window, and adds slider and label for UI Backlight."""

		self.window = Tk()
		self.window.title("Backlight Setting")
		self.window.geometry("160x128")
		self.window.configure(background = "#ff9966")
		self.window.resizable(0, 0)
		self.window.pack_propagate(0)
		
		#Binds key presses to change slider value.
		self.window.bind("<Up>", self.up_key)
		self.window.bind("<Down>", self.down_key)		
		
		#Adds slider to the window.
		self.add_slider()
		
		#Adds label to the window.
		self.add_label()		
		
		self.window.mainloop()
		
	def add_slider(self):
		"""Adds slider to the window."""
		
		self.slider = Scale(self.window, from_ = 100, to = 0, bg = "#ff9966", state = "disabled", sliderlength = 20, command = self.print_slider_value)
		self.slider.pack(side = LEFT)
		
	def add_label(self):	
		"""Adds label to the window."""
	
		self.text_label = Label(self.window, text = "Adjust Brightness", bg = "#ff9966", font = "Helvetica 10 bold")
		self.text_label.pack(side = LEFT)
	
	def print_slider_value(self, slider_value):
		"""Prints slider value."""

		print(slider_value)
		
	def up_key(self, event):
		"""Binds Up key to change the slider value."""
		
		self.slider.configure(state = "active")
		self.current_slider_number = self.slider.get()
		self.slider.set(self.current_slider_number + 10)
		self.slider.configure(state = "disabled")
		
	def down_key(self, event):
		"""Binds Down key to change the slider value."""
		
		self.slider.configure(state = "active")
		self.current_slider_number = self.slider.get()
		self.slider.set(self.current_slider_number - 10)
		self.slider.configure(state = "disabled")
		
display = UIBackLight()
