import time
import RPi.GPIO as GPIO
import Freenove_DHT as DHT
import mongoconn as CONN
import raspsocket as SOCKK
import datetime
import json


#variabili
pin = [13,15]
DHTPin = 11
counter_cicle=0
dht = DHT.DHT(DHTPin)

#setup gpio
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ip = input("inserire ip\n")


for i in pin:
    GPIO.setup(i,GPIO.IN)

while True:
    counter_cicle+=1
    presenza_acqua=False
    presenza_luce=False
    temperatura=0
    umidita=0
    dht.readDHT11()

    #ottengo in input gpio i valori
    hum = GPIO.input(15)
    luce = GPIO.input(13)
    if dht.temperature != -999 and dht.humidity != -999:
        temperatura = dht.temperature
        umidita = dht.humidity

    #pongo true se == 0
    if hum == 0:
        presenza_acqua = True

    #pongo true se == 1
    if luce == 1:
       presenza_luce = True;

    now = datetime.datetime.now()
    actual_date  = now.strftime("%Y-%m-%d")
    actual_time = now.strftime("%H:%M")

    #creo oggetto dati
    dati = {
        'water' : presenza_acqua,
        'light' : presenza_luce,
        'temperature' : temperatura,
        'humidity': umidita,
        'date':actual_date,
        'time':actual_time,
        'code':'#123abc'
        }

    #print delle variabili
    print('Presenza acqua:',dati['water'],'\nPresenza luce:', dati['light'],
          '\nTemperatura-umidità esterna:',dati['temperature'],'C° - ',dati['humidity'],
          '%','\nCiclo num:',counter_cicle,'\n-------')

    ogg_json = json.dumps(dati)

    #invio dati al server
    SOCKK.invio_dati(ogg_json, ip)

    #salvataggio su db locale per backup in assenza di connessione
    CONN.insert_dati(dati)

    #time to wait for the next data extraction
    time.sleep(3600)

#pulizia gpio
GPIO.cleanup()
