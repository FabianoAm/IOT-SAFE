from machine import Pin

class Sportello:
    
    def __init__(self):
        self.irs= Pin(34,Pin.IN)
        
    def is_close(self):
        if (self.irs.value()==0):
            return True
        else:
            return False
        
