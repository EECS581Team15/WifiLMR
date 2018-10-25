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