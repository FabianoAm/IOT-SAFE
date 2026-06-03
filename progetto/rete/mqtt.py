from umqtt.simple import MQTTClient
from schermo import Schermo


class Client:
    def __init__(self):
        self.client = MQTTClient("esp32_client","test.mosquitto.org",1883)
        self.schermo =Schermo()
        self.schermo.show_txt("connessione","broker")
        
    def set_callback(self,txt):
        self.client.set_callback(txt)
    
    def connect(self):
        try:
            self.client.connect()
            self.schermo.print_connesso_mqtt()
        except Exception as e:
            self.schermo.print_non_connesso_mqtt()
            
    def publish(self,topic, messaggio):
        try:
            self.client.publish(topic, messaggio)
        except Exception as e:
            print('Errore durante la pubblicazione:', e)
            
    def subscribe(self, topic):
        try:
            self.client.subscribe(topic)
        except Exception as e:
            print('Errore durante la sottoscrizione:',topic, e)
            
    def check_msg(self):
        try:
            self.client.check_msg()
        except Exception as e:
            print('Errore di connessione MQTT:', e)

            
    
        
