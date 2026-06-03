from machine import Pin, PWM
from time import sleep_ms
from sensori.led import Led
led=Led()


class Serratura:
    def __init__(self):
        self.servo= PWM(Pin(13), freq=50, duty=0)
        self.flag_close=False
        self.s_open()
        
    
    def s_close(self):
        self.servo.duty(80)
        sleep_ms(500)
        self.servo.duty(0)
        self.flag_close=True
        led.switch()
        
    
    def s_open(self):
        self.servo.duty(32)
        sleep_ms(500)
        self.servo.duty(0)
        self.flag_close=False
        led.switch()
        
        
    def is_close(self):
        return self.flag_close
        

    def mqtt_c(self, msg):
        if(msg == "true"):
            if not self.is_close():
                self.s_close()
        if(msg == "false"):
            if self.is_close():
                self.s_open()



        
    