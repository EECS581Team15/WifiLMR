import tkinter
from tkinter import ttk
from .home import UI_Home

class UI():

    #Holds the main window
    def __init__(self):
        #initialize window and frame
        self.window = tkinter.Tk()
        self.window.columnconfigure(0, weight=1, uniform=1)
        self.window.rowconfigure(0, weight=1, uniform=1)
        self.window.geometry("160x128")
        self.window.resizable(0,0)
        self.window.pack_propagate(0)
        
        #Set defaults for the tkinter instance
        self.style = ttk.Style(self.window)
        self.style.configure('TFrame', background='blue')
        self.window.option_add("*Background", "blue")
        self.window.option_add("*Foreground", "white")


        #initialize the different windows

        #initalize to the homescreen
        self.goHome()
        self.window.mainloop()

    def goHome(self):
        UI_Home(self.window)




    

