import dbus.mainloop.glib
import dbus
import enum
import atexit

mainloop = dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)


class AvahiIface(enum.IntEnum):
    UNSPEC = -1


class AvahiProto(enum.IntEnum):
    INET = 0
    INET6 = 1
    UNSPEC = -1


class AvahiConnection:
    AVAHI_SERVICE = "org.freedesktop.Avahi"

    def __init__(self, bus):
        self.bus = bus
        self.server = self.bus.get_object(self.AVAHI_SERVICE, "/")

    @property
    def version(self):
        return self.server.GetVersionString()

    def get_network_interface_index_by_name(self, name):
        return self.server.GetNetworkInterfaceIndexByName(name)

    def get_interfaces(self):
        index = 1
        while True:
            try:
                self.server.GetNetworkInterfaceNameByIndex(index)
                yield index
                index += 1
            except dbus.exceptions.DBusException:
                break

    @property
    def domain_name(self):
        return self.server.GetDomainName()

    @property
    def hostname_fqdn(self):
        return self.server.GetHostNameFqdn()

    def create_entry_group(self):
        path = self.server.EntryGroupNew()
        obj = self.bus.get_object(self.AVAHI_SERVICE, path)
        return dbus.Interface(obj, "org.freedesktop.Avahi.EntryGroup")


__connection = None
__entry = None


def _get_connection():
    global __connection
    if __connection is None:
        __connection = AvahiConnection(dbus.SystemBus())
    return __connection


SERVICE_PATH = "_wifilmr_api._tcp"
SERVICE_NAME = "WiFiLMR API"


def register_service(service_port=8000, extra_txt=""):
    global __entry
    if __entry is not None:
        raise RuntimeError("EntryGroup already created")
    conn = _get_connection()
    domain_name = conn.domain_name
    hostname = conn.hostname_fqdn

    __entry = conn.create_entry_group()
    __entry.AddService(AvahiIface.UNSPEC,
                       AvahiProto.UNSPEC,
                       0,
                       SERVICE_NAME,
                       SERVICE_PATH,
                       domain_name,
                       hostname,
                       service_port,
                       extra_txt)
    __entry.Commit()


@atexit.register
def deregister_service():
    global __entry
    if __entry is not None:
        __entry.Free()
        __entry = None
