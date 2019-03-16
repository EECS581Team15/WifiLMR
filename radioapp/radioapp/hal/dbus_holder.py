"""
radioapp.hal.dbus_holder
========================
Holds dbus related instances
"""
import dbus.mainloop.glib

dbus_main_loop = dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
