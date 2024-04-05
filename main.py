import RPI.GPIO as GPIO

pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.SETUP(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
GPIO.cleanup()
