#!/usr/bin/env python

import time
from RPi import GPIO

LED_R = 36
LED_Y = 38
LED_B = 40
BUTTON = 32

try:
	while True:
		# Use the BOARD numbering system
		GPIO.setmode(GPIO.BOARD)

		# Set up LED pins as output
		GPIO.setup(LED_R, GPIO.OUT)
		GPIO.setup(LED_Y, GPIO.OUT)
		GPIO.setup(LED_B, GPIO.OUT)

		# Set up button pin as input with internal pull-up
		GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		# Turn on LEDs with 1 second delay
		GPIO.output(LED_R, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_Y, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_B, GPIO.HIGH)
		time.sleep(1)

		# Wait for button press
		#print('Waiting for button press...')
		#try:
		#    GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
		#except KeyboardInterrupt:
		#    print('Aborted.')
		#    pass

		# Turn off LEDs again with 1 second delay
		GPIO.output(LED_R, GPIO.LOW)
		time.sleep(1)
		GPIO.output(LED_Y, GPIO.LOW)
		time.sleep(1)
		GPIO.output(LED_B, GPIO.LOW)
		time.sleep(1)

except KeyboardInterrupt:
	# Clean up
	GPIO.cleanup()
