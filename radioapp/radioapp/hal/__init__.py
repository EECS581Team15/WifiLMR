"""
radioapp.hal
============

Any hardware-specific device driver interactions will be handled in the HAL
submodule. This is what allows the RadioApp to run on normal Linux machines to
ease development. This module should be rather minimal and will consist mostly
of configuration values (such as device path names and boolean flags) that
describe the platform that the RadioApp is running on. There will be only two
of these platforms: a dummy platform for development use and a platform
describing the actual radio hardware. There may be some classes that provide
abstracted access to hardware that is too custom to use standard drivers.
The only likely use of this will be the hardware channel knob if it is not
mapped to a keyboard-like device.

The HAL also will provide an interaction layer to the WiFi hardware via
communicating with wpa_supplicant over DBus. This will be used to connect to
the configured network, provision the network connection via WiFi Protected
Setup, and retrieve current connection status information.
"""
import dbus
from . import wifi
from . import backlight


class HAL:
    def __init__(self):
        self.wifi = wifi.WpaSupplicant(dbus.SystemBus())
        self.backlight = backlight.Backlight()
