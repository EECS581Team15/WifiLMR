from zeroconf import ServiceBrowser, Zeroconf
import threading


class LmrListener(object): #declare this before calling PairingScan

    def __init__(self, my_ip):
        self.ip_address = my_ip
        self.stop_searching = threading.Event()

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))

def PairingScan(listener, wait_time=2):
    zeroconf = Zeroconf()
    try:
        ServiceBrowser(zeroconf, "WifiLMR._tcp.local.", listener)
        listener.stop_searching.wait(wait_time) #wait before closing connections
    finally:
        zeroconf.close()

    return listener.ip_address