import tkinter
from tkinter import ttk
from .home import UIHome
from .settings import UISettings

class UI():
    """Holds the main window."""
    
    def __init__(self):
         """
         Initializes window and frame.
         
         Set defaults for the tkinter instance.
         """
        
        self.window = tkinter.Tk()
        self.window.columnconfigure(0, weight=1, uniform=1)
        self.window.rowconfigure(0, weight=1, uniform=1)
        self.window.geometry("160x128")
        self.window.resizable(0,0)
        self.window.pack_propagate(0)
        
        #Set defaults for the tkinter instance.
        self.style = ttk.Style(self.window)
        self.style.configure('TFrame', background='blue')
        self.window.option_add("*Background", "blue")
        self.window.option_add("*Foreground", "white")

        self.start()
        
    def start(self):
        self.go_home()
        self.window.mainloop()

    def go_home(self):
        self.currentPage = UIHome(self.window, self.go_settings, None, None)

    def go_settings(self):
        self.currentPage = UISettings(self.window, self.go_home)




    

