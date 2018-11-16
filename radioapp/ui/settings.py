"""
File to hold the model of home
"""
import tkinter
from tkinter import ttk

class UISettings():
    """Contains UI Settings."""
    
    def __init__(self, window, back):
         """
         Sets up frame.
         
         Sets up back.
         
         Sets up options menu.
         
         Sets up buttons.
         """
            
        #set up frame
        self.frame = ttk.Frame(window, padding="3 3 3 3")
        self.frame.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        self.time = tkinter.StringVar(value="10:34", name="time")
        self.frame.columnconfigure(0, weight=1, uniform="one")
        # self.frame.columnconfigure(1, weight=1, uniform="two")
        # self.frame.columnconfigure(2, weight=1, uniform="buckle")
        self.frame.rowconfigure(0, weight=2, uniform="my")
        self.frame.rowconfigure(1, weight=0, uniform="shoe")
        # self.frame.rowconfigure(2, weight=1, uniform="!")

        #set up back
        self.back = back

        #set up options menu

        #set up buttons
        #they do nothing for now.
        tkinter.Button(self.frame, text="<- Save", command=self.back).grid(row=1, column=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
