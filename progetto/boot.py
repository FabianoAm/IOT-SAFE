# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from sensori.led import Led
from sensori.schermo import Schermo
from sensori.serratura import Serratura
from sensori.sportello import Sportello
from sensori.s_card import S_card
from sensori.s_furto import S_furto
from sensori.tastiera import Tastiera
from entita.password import Password
from time import sleep_ms
from rete.wifi import Wifi
from rete.mqtt import Client


led=Led()
schermo=Schermo()
serratura=Serratura()
sportello=Sportello()
s_card=S_card()
s_furto=S_furto()
tastiera=Tastiera()
password=Password()
allarm_flag= False
tentativi_tot = 3
tentativi_n = 0



schermo.show_logo()
sleep_ms(5000)
wifi=Wifi()
wifi.connect()
sleep_ms(1000)

def callback(topic,msg):
    global serratura
    global password
    global allarm_flag
    global s_card
    global tentativi_tot
    if(topic.decode('utf-8')== "serratura"):
        serratura.mqtt_c(msg.decode('utf-8'))
    if(topic.decode('utf-8')== "password"):
        password.mqtt_c(msg.decode('utf-8'))
    if(topic.decode('utf-8')== "allarme"):
        if(msg.decode('utf-8') == "0"):
            allarm_flag= False
    if(topic.decode('utf-8')== "card"):
        s_card.mqtt_c(msg.decode('utf-8'))
    if(topic.decode('utf-8')== "tentativi"):
        tentativi_tot=int(msg.decode('utf-8'))
        mqtt_client.publish("tentativiRimasti",str(tentativi_tot-tentativi_n))
    
    

    

mqtt_client= Client()
mqtt_client.set_callback(callback)
mqtt_client.connect()

mqtt_client.subscribe("sportello")
mqtt_client.subscribe("serratura")
mqtt_client.subscribe("tentativi")
mqtt_client.publish("tentativi","3")
mqtt_client.subscribe("password")
mqtt_client.subscribe("allarme")
mqtt_client.subscribe("card")

led.start()
