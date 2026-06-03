from machine import Pin
from sensori.buzzer import play_note
from time import sleep 

class Led:
    def __init__(self):
        self.rosso=Pin(17,Pin.OUT)
        self.verde=Pin(16,Pin.OUT)
        self.start()
        sleep(1)
        
    def start(self):
        self.rosso.off()
        self.verde.on()
        
    def switch(self):
        play_note()
        self.rosso.value(not self.rosso.value())
        self.verde.value(not self.verde.value())
        
    def allarm(self):
        self.verde.off()
        self.rosso.value(not self.rosso.value())
    
