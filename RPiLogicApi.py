#Uses RPi GPIO pins to generate a truthtable
#depends on RPi.GPIO

import RPi.GPIO as GPIO
import itertools
import time

GPIO.setmode(GPIO.BCM)

def getTruthtable(outputPins, inputPin):
	truthtable = dict()

	for pin in outputPins:
		GPIO.setup(pin, GPIO.OUT)

	GPIO.setup(input_pin, GPIO.IN)

	vals = [True, False]
	carthProd = list(itertools.product([vals for i in range(outputPins)]))

	for oPinVals in carthProd:
		for i, val in enumerate(oPinVals):
			GPIO.output(outputPins[i], val)

		time.sleep(0.001)
		truthtable[oPinVals] = GPIO.input(inputPin)

	return truthtable