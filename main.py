#Libraries
import RPi.GPIO as GPIO
import time
from sensor import Sensor
from keypad import Keypad
from servo import Servo

GPIO.setmode(GPIO.BCM)

def main():
	try:
		servo = Servo()
		sensor = Sensor(23,24,25)
		while True:
			digit = getObject()
			sensor.turnLED()
			servo.changeRotation()
			dist = sensor.distance()
			time.sleep(0.5)
			print ("Measured Distance = %.1f cm" % dist)
			print (digit)
			time.sleep(1)

		# Reset by pressing CTRL + C
	except KeyboardInterrupt:
			servo.stop()
			print("Measurement stopped by User")
			GPIO.cleanup()
			
def getObject():
	kp = Keypad()
	digit = None
    while digit == None:
		digit = kp.getKey()
    return digit

if __name__ == "__main__":
  main()

