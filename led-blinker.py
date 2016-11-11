import time
import random
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO numbering verwenden
pin = 17 # this is the led pin

GPIO.setup(pin, GPIO.OUT) # use it as an output device 

pi = math.pi
led_time_on = 0.15
led_time_off = 0.2
wait_between_numbers = 0.5

# let the led blink n times
def blinker(n):
	for _ in range(n):
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(led_time_on)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(led_time_off)
		
# let the led blink the digits of pi
while pi > 0:
	print(pi)
	digit = int(pi) % 10
	blinker(digit);
	time.sleep(wait_between_numbers);

	# wind up
	pi -= digit
	pi = pi * 10;
