"""
radioapp.hal.wifi
=================

Implements an interface to wpa_supplicant over DBus for control of the WiFi
interface.
"""

import os
import time
import dbus
import logging
from . import dbus_holder


USR1 = 10
USR2 = 12


class WpaSupplicant:
    INTERFACE = "wlan0"
    WPA_SUPPLICANT = "fi.w1.wpa_supplicant1"
    WPA_SUPPLICANT_INTERFACE_INTERFACE = "fi.w1.wpa_supplicant1.Interface"
    WPA_SUPPLICANT_OBJECT_PATH = "/fi/w1/wpa_supplicant1"

    def __init__(self, bus):
        self.bus = bus
        self.logger = logging.getLogger(__name__)
        self.interface = None
        self.last_state = None

    def signal_poll(self):
        """
        Calls fi.w1.wpa_supplicant1.Interface.SignalPoll() and returns the result
        """
        if self.interface is None:
            # Try to re-validate interface
            self.interface = self._get_interface(self.INTERFACE)
        if self.interface is not None:
            try:
                old_state = self.last_state
                new_state = self._get_state()
                self.last_state = new_state
                if new_state == "completed":
                    if old_state != "completed":
                        self._alert_udhcpc(USR1)  # Just became connected
                    return self.interface.SignalPoll()
                elif old_state == "completed":
                    self._alert_udhcpc(USR2)  # Just became disconnected
            except dbus.exceptions.DBusException:
                # Something bad happened (interface went away, not connected to wifi, etc.)
                self.interface = None
                return None

    def _get_interface(self, name):
        supplicant = self.bus.get_object(
            self.WPA_SUPPLICANT, self.WPA_SUPPLICANT_OBJECT_PATH)
        for interfacePath in dbus.Interface(supplicant, "org.freedesktop.DBus.Properties").Get(self.WPA_SUPPLICANT, "Interfaces"):
            obj = self.bus.get_object(self.WPA_SUPPLICANT, interfacePath)
            name = dbus.Interface(obj, "org.freedesktop.DBus.Properties").Get(
                self.WPA_SUPPLICANT_INTERFACE_INTERFACE, "Ifname")
            if name == self.INTERFACE:
                self.logger.debug("Found interface @ %s", interfacePath)
                return dbus.Interface(obj, self.WPA_SUPPLICANT_INTERFACE_INTERFACE)
        self.logger.info("Failed to find interface")

    def _get_state(self):
        if self.interface is not None:
            props = dbus.Interface(
                self.interface.proxy_object, "org.freedesktop.DBus.Properties")
            return props.Get(self.WPA_SUPPLICANT_INTERFACE_INTERFACE, "State")

    def _alert_udhcpc(self, signal):
        os.system("killall -%s udhcpc" % (signal,))


if __name__ == "__main__":
    supp = WpaSupplicant(dbus.SystemBus())
    while True:
        print(supp.signal_poll())
        time.sleep(3)
