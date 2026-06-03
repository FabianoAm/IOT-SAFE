from machine import Pin, SPI
from driver.mfrc522 import MFRC522
from sensori.buzzer import play_note

class S_card:
    def __init__(self):
        sck = Pin(18, Pin.OUT)
        mosi = Pin(23, Pin.OUT)
        miso = Pin(19, Pin.OUT)
        spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
        sda = Pin(5, Pin.OUT)
        self.rdr = MFRC522(spi, sda)
        self.flag = True
        
        
    def read(self):
        (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)
        if stat == self.rdr.OK:
            (stat, raw_uid) = self.rdr.anticoll()
            if stat == self.rdr.OK:
                uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                print(uid)
                return uid
        return None
    
    def is_admin(self):
        if self.read() =="0x5f3698c2":
            play_note()
            return  True
        return False
    
    def is_pass(self):
        if self.read() == "0x85184c05":
            play_note()
            return True
        return False
    
    def is_active(self):
        return self.flag
    
    def mqtt_c(self, msg):
        if(msg == "0"):
            self.flag = False
        if(msg == "1"):
            self.flag = True
            
