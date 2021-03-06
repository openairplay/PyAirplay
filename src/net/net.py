#Main Network code for PyAirplay

#If anyone thinks of better debug messages feel free to change -Ben

#Variable name definitions:
#F_<Name>: For flags, only boolean
#F_Discovery: if in discovery mode
#F_Started: if network discovery is on or not
#apRecv: currently connected devices

class Network:
    def __init__(self):
        self.apRecv = []
        self.F_Discovery = False
        self.ZC = zeroconf.Zeroconf()
        self.listener = Listener()
        self.browser = None
        self.F_Started = False
        logging.debug("[Networking] Network Init Done")
        
    def start(self):
        self.browser = zeroconf.ServiceBrowser(self.ZC, "_airplay._tcp.local.", self.listener)
        self.F_Started = True
        logging.debug("[Networking] Network Started")
        return 0
        
    def stop(self):
        if (self.browser is not None) or (self.F_Started is True):
            ZC.close()
            self.F_Discovery = False
            logging.debug("[Networking] Network Stopped")
            return 0
        else:
            logging.warning("[Networking] Tried to stop network but nothing was running")
            return 1
    
    def doUpdate(self, inputs):
        #inputs should be structured like:
        #{"Function to do", "input value 1::input value 2:: etc"}
        #outputs/return value should be structured the same way but without the function.
        #inputs will call a function, then the return value/output will tell if that worked or not
    
#I still have to research more into ZeroConf and how it works to understand this -Ben    
class Listener(object):
    def remove_service(self, zeroconf, type, name):
        self.apRecv.remove(name)
        logging.debug(f"[Networking] Airplay receiver {name} removed")

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        self.apRecv.append(name)
        if DEBUG:
            logging.debug(f"[Networking] Airplay receiver {name} added, service info: {info}")

    def update_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if name not in self.apRecv:
            logging.warning(f"[Networking] {name}'s service was updated, but is not known to us yet.")
