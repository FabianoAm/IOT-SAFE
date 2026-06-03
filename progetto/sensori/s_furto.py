from machine import Pin
from driver.hcsr04 import HCSR04
from time import sleep_ms

class S_furto:
    
    def __init__(self):
        self.sens=HCSR04(15,35)
        self.soglia=0
        self.cont=0
        self.dis=0
    
    def set_soglia(self):
        self.soglia=self.sens.send_pulse()
        
    def is_rob(self):
        self.dis = self.sens.send_pulse()
        if((self.dis - self.soglia) > 200 or (self.dis - self.soglia) < -200):
            self.cont = self.cont + 1
        else:
            self.cont = 0
        if self.cont == 3:
            return True
        else:
            return False
        
