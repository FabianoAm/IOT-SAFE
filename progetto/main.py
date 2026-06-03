from sensori.buzzer import play_allarm, play_note
from sensori.led import Led
from sensori.schermo import Schermo
from sensori.serratura import Serratura
from sensori.sportello import Sportello
from sensori.s_card import S_card
from sensori.s_furto import S_furto
from sensori.tastiera import Tastiera
from time import sleep_ms
from rete.wifi import Wifi
from rete.mqtt import Client
from entita.password import Password


def allarm(mode):
    global allarm_flag
    allarm_flag= True
    if mode == 1:
        schermo.print_allarme_furto_infra()
        mqtt_client.publish("allarme","1")
    if mode == 2:
        schermo.print_allarme_serratura_manomessa()
        mqtt_client.publish("allarme","2")
    if mode == 3:
        schermo.show_txt("allarm","tentativi")
        mqtt_client.publish("allarme","3")
    while allarm_flag:
        mqtt_client.check_msg()
        play_allarm()
        led.allarm()
        tastiera.read(password)
        if password.is_correct():
            mqtt_client.publish("allarme","0")
            break
        if password.is_not_correct():
            password.clear()
            schermo.print_pass_sbagliata()
            sleep_ms(1000)
            
    password.clear()
    schermo.print_fine_allarme()
    serratura.s_open()
    sleep_ms(100)
    led.start()
    tentativi_n=0
        




while True:
    if serratura.is_close():
        mqtt_client.publish("serratura","true")
        mqtt_client.publish("tentativiRimasti",str(tentativi_tot-tentativi_n))
        schermo.show_lucchetto()
        s_furto.set_soglia()
        while serratura.is_close():
            mqtt_client.check_msg()
            if s_furto.is_rob():
                allarm(mode=1)
                break
            if not sportello.is_close():
                mqtt_client.publish("sportello","1")
                allarm(mode=2)
                break
            if s_card.is_active():
                if s_card.is_pass():
                    schermo.print_sblocco_serratura_carta()
                    sleep_ms(2000)
                    serratura.s_open()
                    schermo.show_lucc_aperto()
                    tentativi_n=0
                    break
            tastiera.read(password)
            if password.is_correct():
                password.clear()
                schermo.print_pass_corretta()
                serratura.s_open()
                sleep_ms(1000)
                schermo.print_sblocco_serratura()
                tentativi_n=0
                mqtt_client.publish("tentativiEffettuati","r")
                break
            if password.is_not_correct():
                mqtt_client.publish("tentativiEffettuati","w"+ "".join(password.get_p()))
                password.clear()
                schermo.show_pass_sbagliata()
                sleep_ms(1000)
                schermo.print_pass_sbagliata()
                tentativi_n = tentativi_n+1
                mqtt_client.publish("tentativiRimasti",str(tentativi_tot-tentativi_n))
                schermo.show_txt("tentativi",str(tentativi_tot-tentativi_n))
                sleep_ms(1000)
                if(tentativi_tot == tentativi_n):
                    allarm(mode=3)
                break
                
    
    if not serratura.is_close() and sportello.is_close():
        mqtt_client.publish("sportello","0")
        mqtt_client.publish("serratura","false")
        schermo.print_inserisci_pass()
        while sportello.is_close() and not serratura.is_close():
            mqtt_client.check_msg()
            if not password.is_null():
                if s_card.is_active():
                    if s_card.is_pass():
                        schermo.print_carta_rilevata()
                        sleep_ms(1000)
                        serratura.s_close()
                        schermo.print_chiusura_con_carta()
                        sleep_ms(1000)
                        break
            tastiera.read(password)
            if password.is_null():
                if password.set_password():
                    mqtt_client.publish("password","".join(password.get_password()))
                    password.clear()
                    schermo.print_password_impostata()
                    sleep_ms(1000)
                    serratura.s_close()
                    schermo.print_serratura_bloccata()
                    sleep_ms(100)
                    break
            if password.is_correct():
                password.clear()
                schermo.print_pass_corretta()
                sleep_ms(1000)
                serratura.s_close()
                schermo.print_serratura_bloccata()
                break
            if password.is_not_correct():
                password.clear()
                schermo.print_pass_sbagliata()
                sleep_ms(1000)
                break
                
        
    if not serratura.is_close() and not sportello.is_close():
        mqtt_client.publish("sportello","1")
        mqtt_client.publish("serratura","false")
        schermo.print_chiudere_sportello()
        password.clear()
        while not sportello.is_close() and not serratura.is_close():
            mqtt_client.check_msg()
            if s_card.is_admin():
                password.reset()
                schermo.print_carta_amministratore_rilevata()
                sleep_ms(1000)
                break
            
            
                
            
            

            
            


