import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(0,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
while True:
	#Gelb und Rot aus, Gruen an
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(6,GPIO.HIGH)
	GPIO.output(0,GPIO.LOW)
	#Ampel 3 Sekunden lang gruen
	time.sleep(3)
	#Ampel gelb (gruen aus, gelb an)
	GPIO.output(0,GPIO.HIGH)
	GPIO.output(5,GPIO.LOW)
	#Eine Sekunde lang gelb
	time.sleep(1)
	# Gelb aus, Rot an
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(6,GPIO.LOW)
	# Drei Sekunden lang rot
	time.sleep(3)
	# Rot-Gelb Phase fuer eine Sekunde
	GPIO.output(5,GPIO.LOW)
	time.sleep(1)
