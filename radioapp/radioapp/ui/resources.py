"""
radioapp.ui.resources
=====================
"""
import tkinter

WIFI_1 = r"""R0lGODlhGAAfAIAAAP///////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAAAYAB8A
AAIjjI+py+0Po5y02ouz3rz7D4aiBZRZCZwmhqopu14t/I52VwAAOw=="""

WIFI_2 = r"""R0lGODlhGAAfAIAAAP///////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAAAYAB8A
AAIxjI+py+0Po5y02ouz3rxfAGYgIIbYWJKnKaGB25pw5M5QzdJyfu9qrLI9cD+P8RgoAAA7"""
WIFI_3 = r"""R0lGODlhGAAfAIAAAP///////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAAAYAB8A
AAI8jI+py+0Po5y02juBxkED7oEbFpKjVJboqEbp6bIw9H6ZbDe10S57N1P8ekIcL5gYIhHKHKP5
gHKm1EgBADs="""
WIFI_4 = r"""R0lGODlhGAAfAIAAAP///////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAAAYAB8A
AAJNjI+py+0PIZiRTVDXzWpz5FVeGI1UZmLoSUrsKb5qkxptJ9uwlQd3UvPtNL0fqDgUqoI3Zu+4
RM4OzuhUZ8VqgdItdBv8KsHJj/mcKQAAOw=="""
WIFI_NONE = r"""R0lGODlhGAAfAKEBAD8AAP///////////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAIALAAA
AAAYAB8AAAJzlI+py+3fgARv0mTjZJvL4EmLBYbXQZbhEQRTq46d+7bVlsEQLgr6bbn8gB/DkAGr
GW2OVrB0XDhJy5g02IsqMjmmRrjR6jK+lNU3LaJTiuQHmvayaO8qNUEH/MYdBB0NV9KHEsb0Q2ZA
tmeICOH4CBlZAAA7"""


class Resources:
    def __init__(self):
        self.WIFI_1 = tkinter.PhotoImage(data=WIFI_1)
        self.WIFI_2 = tkinter.PhotoImage(data=WIFI_2)
        self.WIFI_3 = tkinter.PhotoImage(data=WIFI_3)
        self.WIFI_4 = tkinter.PhotoImage(data=WIFI_4)
        self.WIFI_NONE = tkinter.PhotoImage(data=WIFI_NONE)
