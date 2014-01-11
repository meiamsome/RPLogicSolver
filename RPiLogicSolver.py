# RPiLogicSolver: Use the Raspberry Pi's GPIO pins to solve a system of logic gates
import RPiLogicAPI as API

try:
    inpt = raw_input
except:
    inpt = input

num = int(inpt("Number of Boolean outputs? "))


outputPins = []
for i in range(num):
    outputPins.append(int(inpt("Pin #{}: ".format(i))))

inputPin = inpt("Input pin: ")

truthtable = API.getTruthtable(outputPins, inputPin)
print(truthtable)
