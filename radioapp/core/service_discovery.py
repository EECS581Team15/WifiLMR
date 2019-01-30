"""
radio.core.service_discovery
============================
The Service Discovery submodule is responsible for locating and identifying
backend instances. In normal operation, it must find the address of the backend
that was configured in the provisioning mode. In provisioning mode, it must
discover and return the names of all available backend instances present on the
local network. This will accomplished via a standard service discovery protocol,
multicast DNS (mDNS).
"""

from zeroconf import ServiceBrowser, Zeroconf
import logging

class BackendDiscovery:

    def __init__(self, callbackadd, callbackremove):
        self.zeroconf = Zeroconf()
        self.servicebrowser = None
        self.listener = LmrListener(callbackadd, callbackremove)

    class LmrListener: #declare this before calling PairingScan

        def __init__(self, callbackadd, callbackremove):
            self.callbackadd = callbackadd
            self.callbackremove = callbackremove
            self.logger = logging.getLogger(__name__)

        def remove_service(self, zeroconf, type, name):
            self.logger.debug("Service %s removed" % (name,))
            self.callbackremove(name)

        def add_service(self, zeroconf, type, name):
            info = zeroconf.get_service_info(type, name)
            self.logger.debug("Service %s added, service info: %s" % (name, info))
            self.callbackadd(name, info)

    def start(self):
        self.servicebrowser = ServiceBrowser(self.zeroconf, "WifiLMR._tcp.local.", self.listener)

    def stop(self):
        self.zeroconf.close()
