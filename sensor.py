import RPi.GPIO as GPIO
import time
class Sensor:
	GPIO_TRIGGER = 0
	GPIO_ECHO = 0
	GPIO_LED1 = 0
	def __init__(self,TRIGGER,ECHO,LED):
		GPIO.setmode(GPIO.BCM)
		self.GPIO_TRIGGER = TRIGGER
		self.GPIO_ECHO = ECHO
		self.GPIO_LED = LED
		GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
		GPIO.setup(self.GPIO_ECHO, GPIO.IN)
		GPIO.setup(self.GPIO_LED1,GPIO.OUT)

	def turnLED(self):
		GPIO.output(self.GPIO_LED1,True)
		time.sleep(0.001)
		GPIO.output(self.GPIO_LED1,False)
		
	def distance(self):
		GPIO.output(self.GPIO_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(self.GPIO_TRIGGER, False)
		StartTime = time.time()
		StopTime = time.time()
		while GPIO.input(self.GPIO_ECHO) == 0:
				StartTime = time.time()
		while GPIO.input(self.GPIO_ECHO) == 1:
				StopTime = time.time()
		TimeElapsed = StopTime - StartTime
		distance = (TimeElapsed * 34300) / 2
		return distance
		



