#!/usr/bin/env python

import time
from RPi import GPIO

LED_R = 36
LED_Y = 38
LED_B = 40
BUTTON = 32

try:
	while True:
		# Use the BOARD numbering system.
		GPIO.setmode(GPIO.BOARD)
		LEDS = [LED_R, LED_Y, LED_B]

		# Set up LED pins as output.
		for led in LEDS:
			GPIO.setup(led, GPIO.OUT)

		# Set up button pin as input with internal pull-up.
		# GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP).

		# Turn on LEDs with 0.5 second delay.
		for led in LEDS:
			GPIO.output(led, GPIO.HIGH)
			time.sleep(0.5)

		time.sleep(2)
		# Wait for button press
		# print('Waiting for button press...')
		# try:
		#    GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
		# except KeyboardInterrupt:
		#    print('Aborted.')
		#    pass

		# Turn off LEDs again with 1 second delay.
		for led in LEDS:
			GPIO.output(led, GPIO.LOW)
			time.sleep(0.5)

		time.sleep(2)
		LEDS.reverse()

		for led in LEDS:
			GPIO.output(led, GPIO.HIGH)
			time.sleep(1)

		for led in LEDS:
			GPIO.output(led, GPIO.LOW)
			time.sleep(1)

except KeyboardInterrupt:
	# Clean up.
	GPIO.cleanup()
