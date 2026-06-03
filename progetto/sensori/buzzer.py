from machine import Pin, PWM
from time import sleep_ms
import math


buzzer=PWM(Pin(4, Pin.OUT))
sleep_ms(1)
buzzer.duty(0)

def play_note(dilay=1000):
    global buzzer
    buzzer.freq(3136)
    buzzer.duty(512)
    sleep_ms(dilay)
    buzzer.duty(0)

def play_allarm():
    global buzzer
    for x in range(0, 36):  
        sinVal = math.sin(x * 10 * math.pi / 180)  
        toneVal = 2000 + int(sinVal * 500)  
        buzzer.freq(toneVal) 
        buzzer.duty(512)
        sleep_ms(10)

