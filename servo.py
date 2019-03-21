import time
import RPi.GPIO as GPIO
class Servo:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16, GPIO.OUT)

	p = GPIO.PWM(16, 50)  # channel=12 frequency=60Hz
	p.start(7.5)
	rotation = input("enter rotation: ")
	degree = 2.5/90
	inp = (rotation * degree)+7.5
	def changeRotation(self):
		try:
			p.ChangeDutyCycle(inp)
			rotation = input("enter rotation: ")
			inp = (rotation * degree)+7.5
		except KeyboardInterrupt:
			self.stop()

	def stop(self):
		p.ChangeDutyCycle(7.5)
		p.stop()
		GPIO.cleanup()

	
