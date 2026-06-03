import network
import time
from schermo import Schermo

class Wifi:
    def __init__(self):
        self.ssid="Federico's Galaxy A52s 5G"
        self.password="qazplmtgv"
        self.schermo=Schermo()



    def connect(self):
        self.wlan=network.WLAN(network.STA_IF)
        self.wlan.active(True)
        if not self.wlan.isconnected():
            self.schermo.print_connessione_wifi()
            time.sleep(1)
            self.wlan.connect(self.ssid, self.password)
            max_wait = 10
            while not self.wlan.isconnected() and max_wait > 0:
                time.sleep(1)
                max_wait -= 1
            if self.wlan.isconnected():
                self.schermo.print_connesso_wifi()
                time.sleep(1)
            else:
                self.schermo.print_non_connesso_wifi()
                time.sleep(1)
        else:
            self.schermo.print_connesso_wifi()
            
                