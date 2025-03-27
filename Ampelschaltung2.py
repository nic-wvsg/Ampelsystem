import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

red = 6
yel = 5
gre = 0

geschwindigkeitszone = int(input("Zulässige Höchstgeschwindigkeit der Straße (in Kilometer pro Stunde): "))

if geschwindigkeitszone <= 30:
    y1 = 10
elif geschwindigkeitszone <= 50:
    y1 = 15
else:
    y1 = 20

if geschwindigkeitszone <= 50:
    y2 = 3
elif geschwindigkeitszone <= 60:
    y2 = 4
else:
    y2 = 5

z = 0
GPIO.output(yel, GPIO.HIGH) #Gelb aus
GPIO.output(red,GPIO.LOW) # Rot an
GPIO.output(gre,GPIO.HIGH) # Grün aus

while True:
   
    try:
        with open("verkehrsdaten.txt", "r") as f:
            data = f.read().strip()
            print(f"Read data: {data}")  # Debugging line
            anzahl_autos, bus_erkannt = map(int, data.split(","))
    except FileNotFoundError:
        anzahl_autos, bus_erkannt = 0, 0

    if bus_erkannt:
        print("Bus erkannt! Ampel schaltet sofort auf Grün.")
        time.sleep(1)
        GPIO.output(yel,GPIO.LOW)#Gelb-Rot Übergang
        time.sleep(2)
        GPIO.output(gre,GPIO.LOW) # Grün an
        GPIO.output(yel,GPIO.HIGH)# Gelb aus
        GPIO.output(red,GPIO.HIGH)# Rot aus
        time.sleep(1)  
        continue

    if GPIO.input(6) == GPIO.LOW:
        x = min(anzahl_autos // 2, 3)  
        z += x 

        if z > 3:
            print(f"Ampel schaltet auf GRÜN für {y1 + (anzahl_autos // 2)} Sekunden")
            time.sleep(1)           # Übergang von Rot zu Grün
            GPIO.output(yel,GPIO.LOW) # Gelb an
            GPIO.output(red,GPIO.LOW) # Rpt an
            time.sleep(2)
            GPIO.output(gre,GPIO.LOW) # Grün an
            GPIO.output(yel,GPIO.HIGH)# Gelb aus
            GPIO.output(red,GPIO.HIGH)# Rot aus
            time.sleep(y1 + (anzahl_autos // 2)) # Für festgelegte Zeit + nach Verkehrsaufkommen
            print(f"Ampel auf GELB für {y2} Sekunden") 
            GPIO.output(gre,GPIO.HIGH)
            GPIO.output(yel,GPIO.LOW) 
            time.sleep(y2) 
            print("Ampel auf ROT")
            GPIO.output(yel,GPIO.HIGH)
            GPIO.output(red,GPIO.LOW)
            z = 0  #Warteschlange zurücksetzten
        else:
            GPIO.output(red,GPIO.LOW) # Ampel bleibt rot
            GPIO.output(yel,GPIO.HIGH)
            GPIO.output(gre,GPIO.HIGH)

    time.sleep(1) 

    
GPIO.cleanup()
