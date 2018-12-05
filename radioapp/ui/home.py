"""
File to hold the model of home
"""
import tkinter
from tkinter import ttk
import time

class UIHome():
    """Contains UI Home Screen."""
    
    def __init__(self, window, b1Action, b2Action, b3Action):
         """
         Sets up frame.
         
         Sets up buttons.
         
         Sets up time and channel.
         
         """
        
        #set up frame
        self.frame = ttk.Frame(window, padding="3 3 3 3")
        self.frame.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        self.frame.columnconfigure(0, weight=1, uniform="one")
        self.frame.columnconfigure(1, weight=1, uniform="two")
        self.frame.columnconfigure(2, weight=1, uniform="buckle")
        self.frame.rowconfigure(0, weight=1, uniform="my")
        self.frame.rowconfigure(1, weight=1, uniform="shoe")
        self.frame.rowconfigure(2, weight=1, uniform="!")

        #set up buttons
        self.b1Action = b1Action

        #Label Variables
        self.time = tkinter.StringVar(value="10:34", name="time")
        self.battery = tkinter.StringVar(value="100%", name="battery")
        self.strength = tkinter.StringVar(value="-120dB", name="strength")


        #set up time and channel
        self.channel = tkinter.StringVar(value="Channel 1", name="channel")
        tkinter.Label(self.frame, textvariable=self.time).grid(row=0, column=0, columnspan=2, sticky=(tkinter.N, tkinter.W))
        tkinter.Label(self.frame, textvariable=self.battery).grid(row=0, column=2, columnspan=2, sticky=(tkinter.N, tkinter.E))
        tkinter.Label(self.frame, textvariable=self.strength).grid(row=1, column=1, columnspan=2, sticky=(tkinter.N, tkinter.E))
        tkinter.Label(self.frame, textvariable=self.channel).grid(row=1, column=0, columnspan=2, sticky=(tkinter.N, tkinter.W))
        self.__clock()

        #set up buttons
        #they do nothing for now.
        tkinter.Button(self.frame, text="1", command=self.button1).grid(row=3, column=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        tkinter.Button(self.frame, text="2").grid(row=3, column=1, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        tkinter.Button(self.frame, text="3").grid(row=3, column=2, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))

    def update_channel(self, channel):
        self.channel.set(channel)

    def __clock(self):
        timeNow = time.strftime('%H:%M:%S')
        self.time.set(timeNow)
        self.frame.after(200, func=self.__clock)
        
    def button1(self):
        self.b1Action()

    def button2(self):
        pass
    
    def button3(self):
        pass
