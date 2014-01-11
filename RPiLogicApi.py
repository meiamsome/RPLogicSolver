#Uses RPi GPIO pins to generate a truthtable
#depends on RPi.GPIO

import RPi.GPIO as GPIO
import itertools
import time


def getTruthtable(outputPins, inputPin):
	GPIO.setmode(GPIO.BCM)
	truthtable = dict()

	for pin in outputPins:
		GPIO.setup(pin, GPIO.OUT)

	GPIO.setup(inputPin, GPIO.IN)

	vals = [True, False]
	carthProd = list(itertools.product(*[vals for i in range(len(outputPins))]))

	for oPinVals in carthProd:
		for i, val in enumerate(oPinVals):
			GPIO.output(outputPins[i], val)

		time.sleep(1)
		truthtable[oPinVals] = GPIO.input(inputPin)

	return truthtable
	GPIO.cleanup()

while(1): print (getTruthtable([9, 11], 10))
