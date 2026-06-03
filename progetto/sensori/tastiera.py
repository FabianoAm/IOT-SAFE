from machine import Pin
from driver.keypad import Keypad
from time import sleep_ms
from sensori.schermo import Schermo
schermo=Schermo()
from sensori.buzzer import play_note


class Tastiera:
    
    def __init__(self):
        row_pins = [Pin(32),Pin(33),Pin(25),Pin(26)]
        column_pins = [Pin(27),Pin(14),Pin(12),Pin(2)]
        keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']]
        
        self.kaypad=Keypad(row_pins, column_pins, keys)
        
    def read(self,p):
            key_pressed = self.kaypad.read_keypad()
            if key_pressed:
                p.append(key_pressed)
                play_note(200)
                if p.is_null():
                    schermo.p_visibile(p)
                else:
                    schermo.p_non_visibile(p)
                sleep_ms(200)
                
