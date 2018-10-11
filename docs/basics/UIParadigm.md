User Interface Paradigm
=======================

Introduction
------------

A lot of the user interface choices on the radio are dictated by hardware choices. In turn, a lot of the hardware choices are driven by the desire to make the mechanical and digital designs simpler.

User Interface Hardware:

* Relatively small, low-resolution color screen (128x128 to 160x128)
* Push-to-talk button on the left side
* Volume/Power knob (on top)
* Channel knob (on top)
* D-pad or 4-direction joystick plus select on front for menu navigation


Main Status Page
----------------

Most LMRs normally idle on some sort of status page. This page is generally simple (and optimized to be to easy to read in a glance). It should, at minimum, display the channel information and basic status information icons such as channel activity, battery status, and signal strength.

Menu
----

Additional information and functions that are not normally required can be pushed into a menu. Some examples include extended battery health information, network information, an about page, etc. The menu can be presented as either a list screen or some sort of grid, either of which map well to the joystick/d-pad input device. Since it may not immediately obvious to the user, we should consider putting small "hints" (arrows or similar) to guide the user in how to navigate the menu system.

Push-to-talk
------------

It should be noted that at any time, PTT can be pressed. Upon press, this should return the UI to the main screen and transmit normally. We should to trust that the user meant to do this in the event that the suddenly need to transmit without taking the time exit all of the menus.